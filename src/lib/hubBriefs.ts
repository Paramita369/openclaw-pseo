import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

export const HUB_ASSETS = ['BTC', 'ETH', 'GOLD', 'QQQ', 'SPY'] as const;
export const HUB_EVENTS = ['CPI', 'NFP', 'FOMC'] as const;

export type HubAsset = (typeof HUB_ASSETS)[number];
export type HubEvent = (typeof HUB_EVENTS)[number];
export type HubStatus = 'draft' | 'approved';
export type HubIndexing = 'index' | 'noindex';

export type HubBrief = {
  asset: HubAsset;
  event_type: HubEvent;
  thesis: string;
  what_changed_recently: string;
  risk_watchouts: string;
  execution_checklist: string[];
  reviewed_at: string;
  status: HubStatus;
  indexing: HubIndexing;
};

type PartialHubBrief = Partial<HubBrief> & Record<string, unknown>;

const HUB_KEY_SET = new Set(HUB_ASSETS.flatMap((asset) => HUB_EVENTS.map((eventType) => `${asset}_${eventType}`)));

function parseScalar(raw: string): string {
  const text = String(raw || '').trim();
  if ((text.startsWith('"') && text.endsWith('"')) || (text.startsWith("'") && text.endsWith("'"))) {
    return text.slice(1, -1);
  }
  return text;
}

function parseHubBriefsFallback(content: string): Record<string, PartialHubBrief> {
  const payload: Record<string, PartialHubBrief> = {};
  let currentKey = '';
  let inChecklist = false;

  for (const rawLine of content.split(/\r?\n/)) {
    const line = rawLine.replace(/\s+$/, '');
    const stripped = line.trim();
    if (!stripped || stripped.startsWith('#')) continue;

    if (!line.startsWith(' ') && stripped.endsWith(':')) {
      const key = stripped.slice(0, -1).trim();
      if (!key) continue;
      currentKey = key;
      payload[currentKey] = {};
      inChecklist = false;
      continue;
    }

    if (!currentKey || !payload[currentKey]) continue;

    if (inChecklist && stripped.startsWith('- ')) {
      const item = parseScalar(stripped.slice(2));
      const existing = payload[currentKey].execution_checklist;
      if (!Array.isArray(existing)) {
        payload[currentKey].execution_checklist = [item];
      } else {
        existing.push(item);
      }
      continue;
    }

    if (line.startsWith('  ') && stripped.includes(':')) {
      const [rawKey, ...rest] = stripped.split(':');
      const key = rawKey.trim();
      const value = rest.join(':').trim();
      if (!key) continue;
      if (key === 'execution_checklist') {
        payload[currentKey].execution_checklist = [];
        inChecklist = true;
      } else {
        payload[currentKey][key] = parseScalar(value);
        inChecklist = false;
      }
    }
  }

  return payload;
}

function normalizeBrief(key: string, value: PartialHubBrief | undefined): HubBrief {
  const [assetRaw, eventRaw] = key.split('_');
  const asset = HUB_ASSETS.includes(assetRaw as HubAsset) ? (assetRaw as HubAsset) : 'BTC';
  const eventType = HUB_EVENTS.includes(eventRaw as HubEvent) ? (eventRaw as HubEvent) : 'CPI';
  const checklist = Array.isArray(value?.execution_checklist)
    ? value.execution_checklist.map((item) => String(item || '').trim()).filter(Boolean)
    : [];
  const nonEmptyChecklist = checklist.length >= 3
    ? checklist
    : [
        'Review cross-asset context before execution.',
        'Use predefined risk limits and position sizing.',
        'Wait for confirmation and avoid first impulse entries.',
      ];

  const rawStatus = String(value?.status || 'draft').toLowerCase();
  const status: HubStatus = rawStatus === 'approved' ? 'approved' : 'draft';
  const rawIndexing = String(value?.indexing || '').toLowerCase();
  const indexing: HubIndexing =
    rawIndexing === 'index' || rawIndexing === 'noindex'
      ? (rawIndexing as HubIndexing)
      : status === 'approved'
        ? 'index'
        : 'noindex';

  return {
    asset,
    event_type: eventType,
    thesis: String(value?.thesis || `${asset} ${eventType} event thesis is in draft; refine with validated market context.`),
    what_changed_recently: String(
      value?.what_changed_recently ||
        'Recent regime shifts changed cross-asset transmission speed; keep this section updated each review cycle.'
    ),
    risk_watchouts: String(
      value?.risk_watchouts ||
        'Watch liquidity shocks, macro headline revisions, and policy communication tone changes.'
    ),
    execution_checklist: nonEmptyChecklist,
    reviewed_at: String(value?.reviewed_at || new Date().toISOString().slice(0, 10)),
    status,
    indexing,
  };
}

export function loadHubBriefs(): Record<string, HubBrief> {
  const path = resolve(process.cwd(), 'data/hub_briefs.yaml');
  const raw = readFileSync(path, 'utf-8');
  const parsed = parseHubBriefsFallback(raw);

  const normalized: Record<string, HubBrief> = {};
  for (const key of HUB_KEY_SET) {
    normalized[key] = normalizeBrief(key, parsed[key]);
  }
  return normalized;
}

export function listHubRoutes(): Array<{ asset: HubAsset; event: HubEvent; key: string }> {
  return HUB_ASSETS.flatMap((asset) =>
    HUB_EVENTS.map((eventType) => ({
      asset,
      event: eventType,
      key: `${asset}_${eventType}`,
    }))
  );
}
