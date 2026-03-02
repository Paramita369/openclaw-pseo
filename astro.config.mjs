import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwind from '@astrojs/tailwind';
import rehypeRaw from 'rehype-raw';

export default defineConfig({
  site: 'https://quantmacro.vercel.app',
  integrations: [mdx(), tailwind()],
  markdown: {
    rehypePlugins: [rehypeRaw],
    shikiConfig: {
      theme: 'github-dark'
    }
  }
});
