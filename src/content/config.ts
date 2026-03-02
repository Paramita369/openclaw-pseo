import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    pubDate: z.string().optional(),
    tags: z.array(z.string()).optional(),
    metrics: z.object({
      sharpe_t7: z.number().optional().nullable(),
      mdd_t7: z.number().optional().nullable(),
      volatility: z.number().optional().nullable(),
    }).optional().nullable(),
    chartData: z.array(z.object({
      time: z.string(),
      open: z.number(),
      high: z.number(),
      low: z.number(),
      close: z.number(),
    })).optional().nullable(),
  }),
});

export const collections = { blog };
