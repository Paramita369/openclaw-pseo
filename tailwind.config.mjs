import typography from '@tailwindcss/typography';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      fontFamily: {
        heading: ['Poppins', 'sans-serif'],
        body: ['Open Sans', 'sans-serif'],
      },
      colors: {
        // Fintech/Crypto palette
        primary: '#F59E0B',
        secondary: '#FBBF24',
        accent: '#8B5CF6',
        dark: {
          bg: '#0F172A',
          surface: '#1E293B',
          border: '#334155',
        },
        profit: '#22C55E',
        loss: '#EF4444',
      },
    },
  },
  plugins: [
    typography,
  ],
}
