import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    pubDate: z.string().optional(),
    tags: z.array(z.string()).optional(),
    metrics: z.object({
      sharpe_t7: z.number().optional(),
      mdd_t7: z.number().optional(),
      volatility: z.number().optional(),
    }).optional(),
    chartData: z.array(z.object({
      time: z.string(),
      open: z.number(),
      high: z.number(),
      low: z.number(),
      close: z.number(),
    })).optional(),
  }),
});

export const collections = { blog };
