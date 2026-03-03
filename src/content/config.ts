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
    source: z.string().min(1),
    offer_key: z.string().min(1),
    signal: z.enum(['Bullish', 'Neutral', 'Bearish']),
    confidence_level: z.enum(['low', 'normal']),
    quality_score: z.number().min(0).max(100),
    sample_size: z.number().int().nonnegative(),
    freshness_days: z.number().int().nonnegative(),
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
