import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

const manifestPath = path.join(process.cwd(), 'data', 'page_manifest.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8')) as { pages: Record<string, Record<string, unknown>> };

function pickSlugByCanonicalTarget(target: 'self' | 'hub' | 'none'): string {
  for (const [slug, page] of Object.entries(manifest.pages || {})) {
    if (String(page.canonical_target || '') === target) {
      return slug;
    }
  }
  throw new Error(`No slug found for canonical target ${target}`);
}

test('Tier C page must have noindex and no canonical', async ({ page }) => {
  const slug = pickSlugByCanonicalTarget('none');
  await page.goto(`/blog/${slug}`);
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'noindex,follow');
  await expect(page.locator('link[rel="canonical"]')).toHaveCount(0);
  await expect(page.locator('script[type="application/ld+json"]')).toHaveCount(1);
});

test('Canonical hub page must keep indexable robots and hub canonical', async ({ page, request }) => {
  const slug = pickSlugByCanonicalTarget('hub');
  await page.goto(`/blog/${slug}`);
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'index,follow');
  const canonicalHref = await page.locator('link[rel="canonical"]').getAttribute('href');
  expect(canonicalHref).toContain('/playbooks/');

  const sitemap = await request.get('/sitemap-blog-1.xml');
  const sitemapText = await sitemap.text();
  expect(sitemapText.includes(`/blog/${slug}`)).toBeFalsy();
});

test('Self canonical page must point to its own blog URL', async ({ page }) => {
  const slug = pickSlugByCanonicalTarget('self');
  await page.goto(`/blog/${slug}`);
  const canonicalHref = await page.locator('link[rel="canonical"]').getAttribute('href');
  expect(canonicalHref).toContain(`/blog/${slug}`);
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'index,follow');
});

test('Approved hub must expose Dataset schema and crawlable table', async ({ page }) => {
  await page.goto('/playbooks/btc/cpi');
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'index,follow');
  await expect(page.locator('script[type="application/ld+json"]')).toHaveCount(1);
  const scriptContent = await page.locator('script[type="application/ld+json"]').textContent();
  const schema = JSON.parse(scriptContent || '{}');
  const graph = Array.isArray(schema['@graph']) ? schema['@graph'] : [];
  expect(graph.some((node: Record<string, unknown>) => node['@type'] === 'Dataset')).toBeTruthy();
  await expect(page.locator('table').first()).toBeVisible();
});

test('Draft hub must stay noindex and out of playbooks sitemap', async ({ page, request }) => {
  await page.goto('/playbooks/eth/nfp');
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'noindex,follow');
  const sitemap = await request.get('/sitemap-playbooks.xml');
  const sitemapText = await sitemap.text();
  expect(sitemapText.includes('/playbooks/eth/nfp')).toBeFalsy();
  await expect(page.locator('script[type="application/ld+json"]')).toHaveCount(1);
});
