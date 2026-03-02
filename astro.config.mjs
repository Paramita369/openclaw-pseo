import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://your-domain.com', // TODO: 替換為你的網域
  integrations: [
    mdx(),
    sitemap(),
    tailwind()
  ],
  markdown: {
    shikiConfig: {
      theme: 'github-dark'
    }
  }
});
