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
  }),
});

export const collections = { blog };
