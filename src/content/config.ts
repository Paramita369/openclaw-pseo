import { defineCollection, z } from 'astro:content';

const probabilityWindow = z.object({
  up: z.number().min(0).max(100),
  down: z.number().min(0).max(100),
  median: z.number().finite(),
  mean: z.number().finite(),
  sample: z.number().int().nonnegative(),
});

const conditionalProbability = z.object({
  basis: z.literal('event_direction'),
  direction: z.enum(['up', 'down', 'flat']),
  sample_size: z.number().int().nonnegative(),
  t1: probabilityWindow,
  t7: probabilityWindow,
});

const relatedEventItem = z.object({
  slug: z.string().min(1),
  title: z.string().min(1),
  event_date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
  event_type: z.enum(['CPI', 'NFP', 'FOMC']),
  signal: z.enum(['Bullish', 'Neutral', 'Bearish']),
  sharpe_t7: z.number().finite(),
  median_t7_pct: z.number().finite(),
  sample_size: z.number().int().nonnegative(),
});

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    event_type: z.enum(['CPI', 'NFP', 'FOMC']),
    event_label: z.string().min(1),
    event_slug: z.string().min(1),
    event_date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    asof_date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    event_direction: z.enum(['up', 'down', 'flat']),
    event_actual: z.number().finite(),
    event_previous: z.number().finite(),
    event_delta: z.number().finite(),
    direction_basis: z.literal('vs_previous'),
    outcome_status: z.enum(['ok', 'pending']),
    source: z.string().min(1),
    offer_key: z.string().min(1),
    signal: z.enum(['Bullish', 'Neutral', 'Bearish']),
    raw_signal_score: z.number().finite(),
    robust_score: z.number().finite(),
    penalties: z.object({
      sample: z.number().finite().min(0),
      freshness: z.number().finite().min(0),
      confidence: z.number().finite().min(0),
      outcome: z.number().finite().min(0),
    }),
    confidence_level: z.enum(['low', 'normal']),
    quality_score: z.number().min(0).max(100),
    sample_size: z.number().int().nonnegative(),
    freshness_days: z.number().int().nonnegative(),
    freshness_status: z.enum(['fresh', 'stale']).optional(),
    data_last_updated_at: z.string().min(10).optional(),
    index_tier: z.enum(['A', 'B', 'C']).optional(),
    is_recent_90d: z.boolean().optional(),
    is_core_page: z.boolean(),
    core_window_days: z.number().int().positive(),
    body_variant_family: z.string().min(1),
    hub_baseline_mean_t7: z.number().finite(),
    hub_baseline_median_t7: z.number().finite(),
    hub_baseline_std_t7: z.number().finite(),
    hub_baseline_delta: z.number().finite(),
    z_score_t7: z.number().finite(),
    percentile_t7: z.number().finite().min(0).max(100),
    narrative_trigger: z.enum([
      'extreme_outperformance',
      'moderate_outperformance',
      'strict_median_norm',
      'moderate_underperformance',
      'extreme_underperformance',
      'low_context',
    ]),
    narrative_rank_band: z.enum(['extreme', 'moderate', 'median', 'low_context']),
    narrative_direction_band: z.enum(['positive', 'negative', 'neutral', 'unknown']),
    canonical_target: z.enum(['self', 'hub', 'none']).optional(),
    canonical_url: z.string().optional(),
    robots_directive: z.enum(['index,follow', 'noindex,follow']).optional(),
    in_blog_sitemap: z.boolean().optional(),
    tags: z.array(z.string()).min(1),
    metrics: z.object({
      sharpe_t7: z.number().finite(),
      mdd_t7: z.number().finite(),
      volatility: z.number().finite(),
      impact_t1_pct: z.number().finite(),
      impact_t7_pct: z.number().finite(),
    }),
    probabilities: z.object({
      t1: probabilityWindow,
      t7: probabilityWindow,
      conditional: conditionalProbability,
      sample_size: z.number().int().nonnegative(),
    }),
    related_events: z.array(relatedEventItem).max(3).optional(),
    chartData: z
      .array(
        z.object({
          time: z.string(),
          open: z.number().finite(),
          high: z.number().finite(),
          low: z.number().finite(),
          close: z.number().finite(),
        })
      )
      .optional()
      .nullable(),
  }),
});

export const collections = { blog };
