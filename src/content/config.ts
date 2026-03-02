import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    pubDate: z.string().optional(),
    tags: z.array(z.string()).optional(),
    metrics: z.object({
      sharpe_t7: z.union([z.number(), z.string()]).optional().nullable(),
      mdd_t7: z.union([z.number(), z.string()]).optional().nullable(),
      volatility: z.union([z.number(), z.string()]).optional().nullable(),
    }).optional().nullable(),
    chartData: z.array(z.any()).optional().nullable(),
  }),
});

export const collections = { blog };
