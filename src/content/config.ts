import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    event_type: z.string().min(1),
    source: z.string().min(1),
    offer_key: z.string().min(1),
    quality_score: z.number().min(0).max(100),
    tags: z.array(z.string()).min(1),
    metrics: z.object({
      sharpe_t7: z.number().finite(),
      mdd_t7: z.number().finite(),
      volatility: z.number().finite(),
      impact_t1_pct: z.number().finite(),
      impact_t7_pct: z.number().finite(),
    }),
    chartData: z.array(z.object({
      time: z.string(),
      open: z.number().finite(),
      high: z.number().finite(),
      low: z.number().finite(),
      close: z.number().finite(),
    })).optional().nullable(),
  }),
});

export const collections = { blog };
