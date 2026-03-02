declare module 'astro:content' {
	interface Render {
		'.mdx': Promise<{
			Content: import('astro').MarkdownInstance<{}>['Content'];
			headings: import('astro').MarkdownHeading[];
			remarkPluginFrontmatter: Record<string, any>;
		}>;
	}
}

declare module 'astro:content' {
	interface RenderResult {
		Content: import('astro/runtime/server/index.js').AstroComponentFactory;
		headings: import('astro').MarkdownHeading[];
		remarkPluginFrontmatter: Record<string, any>;
	}
	interface Render {
		'.md': Promise<RenderResult>;
	}

	export interface RenderedContent {
		html: string;
		metadata?: {
			imagePaths: Array<string>;
			[key: string]: unknown;
		};
	}
}

declare module 'astro:content' {
	type Flatten<T> = T extends { [K: string]: infer U } ? U : never;

	export type CollectionKey = keyof AnyEntryMap;
	export type CollectionEntry<C extends CollectionKey> = Flatten<AnyEntryMap[C]>;

	export type ContentCollectionKey = keyof ContentEntryMap;
	export type DataCollectionKey = keyof DataEntryMap;

	type AllValuesOf<T> = T extends any ? T[keyof T] : never;
	type ValidContentEntrySlug<C extends keyof ContentEntryMap> = AllValuesOf<
		ContentEntryMap[C]
	>['slug'];

	/** @deprecated Use `getEntry` instead. */
	export function getEntryBySlug<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		// Note that this has to accept a regular string too, for SSR
		entrySlug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;

	/** @deprecated Use `getEntry` instead. */
	export function getDataEntryById<C extends keyof DataEntryMap, E extends keyof DataEntryMap[C]>(
		collection: C,
		entryId: E,
	): Promise<CollectionEntry<C>>;

	export function getCollection<C extends keyof AnyEntryMap, E extends CollectionEntry<C>>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => entry is E,
	): Promise<E[]>;
	export function getCollection<C extends keyof AnyEntryMap>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => unknown,
	): Promise<CollectionEntry<C>[]>;

	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(entry: {
		collection: C;
		slug: E;
	}): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(entry: {
		collection: C;
		id: E;
	}): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		slug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(
		collection: C,
		id: E,
	): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;

	/** Resolve an array of entry references from the same collection */
	export function getEntries<C extends keyof ContentEntryMap>(
		entries: {
			collection: C;
			slug: ValidContentEntrySlug<C>;
		}[],
	): Promise<CollectionEntry<C>[]>;
	export function getEntries<C extends keyof DataEntryMap>(
		entries: {
			collection: C;
			id: keyof DataEntryMap[C];
		}[],
	): Promise<CollectionEntry<C>[]>;

	export function render<C extends keyof AnyEntryMap>(
		entry: AnyEntryMap[C][string],
	): Promise<RenderResult>;

	export function reference<C extends keyof AnyEntryMap>(
		collection: C,
	): import('astro/zod').ZodEffects<
		import('astro/zod').ZodString,
		C extends keyof ContentEntryMap
			? {
					collection: C;
					slug: ValidContentEntrySlug<C>;
				}
			: {
					collection: C;
					id: keyof DataEntryMap[C];
				}
	>;
	// Allow generic `string` to avoid excessive type errors in the config
	// if `dev` is not running to update as you edit.
	// Invalid collection names will be caught at build time.
	export function reference<C extends string>(
		collection: C,
	): import('astro/zod').ZodEffects<import('astro/zod').ZodString, never>;

	type ReturnTypeOrOriginal<T> = T extends (...args: any[]) => infer R ? R : T;
	type InferEntrySchema<C extends keyof AnyEntryMap> = import('astro/zod').infer<
		ReturnTypeOrOriginal<Required<ContentConfig['collections'][C]>['schema']>
	>;

	type ContentEntryMap = {
		"blog": {
"btc-after-geopolitics.md": {
	id: "btc-after-geopolitics.md";
  slug: "btc-after-geopolitics";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-after-macro.md": {
	id: "btc-after-macro.md";
  slug: "btc-after-macro";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-cpi-release-1-day-vs-gold.md": {
	id: "btc-correlation-after-cpi-release-1-day-vs-gold.md";
  slug: "btc-correlation-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-cpi-release-1-day-vs-sp500.md": {
	id: "btc-correlation-after-cpi-release-1-day-vs-sp500.md";
  slug: "btc-correlation-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-cpi-release-1-day.md": {
	id: "btc-correlation-after-cpi-release-1-day.md";
  slug: "btc-correlation-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-cpi-release-7-day-vs-gold.md": {
	id: "btc-correlation-after-cpi-release-7-day-vs-gold.md";
  slug: "btc-correlation-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-cpi-release-7-day-vs-sp500.md": {
	id: "btc-correlation-after-cpi-release-7-day-vs-sp500.md";
  slug: "btc-correlation-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-cpi-release-7-day.md": {
	id: "btc-correlation-after-cpi-release-7-day.md";
  slug: "btc-correlation-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "btc-correlation-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "btc-correlation-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "btc-correlation-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "btc-correlation-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-fed-rate-cut-1-day.md": {
	id: "btc-correlation-after-fed-rate-cut-1-day.md";
  slug: "btc-correlation-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "btc-correlation-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "btc-correlation-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "btc-correlation-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "btc-correlation-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-fed-rate-cut-7-day.md": {
	id: "btc-correlation-after-fed-rate-cut-7-day.md";
  slug: "btc-correlation-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-gdp-report-1-day-vs-gold.md": {
	id: "btc-correlation-after-gdp-report-1-day-vs-gold.md";
  slug: "btc-correlation-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-gdp-report-1-day-vs-sp500.md": {
	id: "btc-correlation-after-gdp-report-1-day-vs-sp500.md";
  slug: "btc-correlation-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-gdp-report-1-day.md": {
	id: "btc-correlation-after-gdp-report-1-day.md";
  slug: "btc-correlation-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-gdp-report-7-day-vs-gold.md": {
	id: "btc-correlation-after-gdp-report-7-day-vs-gold.md";
  slug: "btc-correlation-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-gdp-report-7-day-vs-sp500.md": {
	id: "btc-correlation-after-gdp-report-7-day-vs-sp500.md";
  slug: "btc-correlation-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-gdp-report-7-day.md": {
	id: "btc-correlation-after-gdp-report-7-day.md";
  slug: "btc-correlation-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-inflation-rate-1-day-vs-gold.md": {
	id: "btc-correlation-after-inflation-rate-1-day-vs-gold.md";
  slug: "btc-correlation-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-inflation-rate-1-day-vs-sp500.md": {
	id: "btc-correlation-after-inflation-rate-1-day-vs-sp500.md";
  slug: "btc-correlation-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-inflation-rate-1-day.md": {
	id: "btc-correlation-after-inflation-rate-1-day.md";
  slug: "btc-correlation-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-inflation-rate-7-day-vs-gold.md": {
	id: "btc-correlation-after-inflation-rate-7-day-vs-gold.md";
  slug: "btc-correlation-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-inflation-rate-7-day-vs-sp500.md": {
	id: "btc-correlation-after-inflation-rate-7-day-vs-sp500.md";
  slug: "btc-correlation-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-inflation-rate-7-day.md": {
	id: "btc-correlation-after-inflation-rate-7-day.md";
  slug: "btc-correlation-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-nfp-data-1-day-vs-gold.md": {
	id: "btc-correlation-after-nfp-data-1-day-vs-gold.md";
  slug: "btc-correlation-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-nfp-data-1-day-vs-sp500.md": {
	id: "btc-correlation-after-nfp-data-1-day-vs-sp500.md";
  slug: "btc-correlation-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-nfp-data-1-day.md": {
	id: "btc-correlation-after-nfp-data-1-day.md";
  slug: "btc-correlation-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-nfp-data-7-day-vs-gold.md": {
	id: "btc-correlation-after-nfp-data-7-day-vs-gold.md";
  slug: "btc-correlation-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-nfp-data-7-day-vs-sp500.md": {
	id: "btc-correlation-after-nfp-data-7-day-vs-sp500.md";
  slug: "btc-correlation-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-correlation-after-nfp-data-7-day.md": {
	id: "btc-correlation-after-nfp-data-7-day.md";
  slug: "btc-correlation-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-cpi-release-1-day-vs-gold.md": {
	id: "btc-historical-performance-after-cpi-release-1-day-vs-gold.md";
  slug: "btc-historical-performance-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-cpi-release-1-day-vs-sp500.md": {
	id: "btc-historical-performance-after-cpi-release-1-day-vs-sp500.md";
  slug: "btc-historical-performance-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-cpi-release-1-day.md": {
	id: "btc-historical-performance-after-cpi-release-1-day.md";
  slug: "btc-historical-performance-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-cpi-release-7-day-vs-gold.md": {
	id: "btc-historical-performance-after-cpi-release-7-day-vs-gold.md";
  slug: "btc-historical-performance-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-cpi-release-7-day-vs-sp500.md": {
	id: "btc-historical-performance-after-cpi-release-7-day-vs-sp500.md";
  slug: "btc-historical-performance-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-cpi-release-7-day.md": {
	id: "btc-historical-performance-after-cpi-release-7-day.md";
  slug: "btc-historical-performance-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "btc-historical-performance-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "btc-historical-performance-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "btc-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "btc-historical-performance-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-fed-rate-cut-1-day.md": {
	id: "btc-historical-performance-after-fed-rate-cut-1-day.md";
  slug: "btc-historical-performance-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "btc-historical-performance-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "btc-historical-performance-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "btc-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "btc-historical-performance-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-fed-rate-cut-7-day.md": {
	id: "btc-historical-performance-after-fed-rate-cut-7-day.md";
  slug: "btc-historical-performance-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-gdp-report-1-day-vs-gold.md": {
	id: "btc-historical-performance-after-gdp-report-1-day-vs-gold.md";
  slug: "btc-historical-performance-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-gdp-report-1-day-vs-sp500.md": {
	id: "btc-historical-performance-after-gdp-report-1-day-vs-sp500.md";
  slug: "btc-historical-performance-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-gdp-report-1-day.md": {
	id: "btc-historical-performance-after-gdp-report-1-day.md";
  slug: "btc-historical-performance-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-gdp-report-7-day-vs-gold.md": {
	id: "btc-historical-performance-after-gdp-report-7-day-vs-gold.md";
  slug: "btc-historical-performance-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-gdp-report-7-day-vs-sp500.md": {
	id: "btc-historical-performance-after-gdp-report-7-day-vs-sp500.md";
  slug: "btc-historical-performance-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-gdp-report-7-day.md": {
	id: "btc-historical-performance-after-gdp-report-7-day.md";
  slug: "btc-historical-performance-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-inflation-rate-1-day-vs-gold.md": {
	id: "btc-historical-performance-after-inflation-rate-1-day-vs-gold.md";
  slug: "btc-historical-performance-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-inflation-rate-1-day-vs-sp500.md": {
	id: "btc-historical-performance-after-inflation-rate-1-day-vs-sp500.md";
  slug: "btc-historical-performance-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-inflation-rate-1-day.md": {
	id: "btc-historical-performance-after-inflation-rate-1-day.md";
  slug: "btc-historical-performance-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-inflation-rate-7-day-vs-gold.md": {
	id: "btc-historical-performance-after-inflation-rate-7-day-vs-gold.md";
  slug: "btc-historical-performance-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-inflation-rate-7-day-vs-sp500.md": {
	id: "btc-historical-performance-after-inflation-rate-7-day-vs-sp500.md";
  slug: "btc-historical-performance-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-inflation-rate-7-day.md": {
	id: "btc-historical-performance-after-inflation-rate-7-day.md";
  slug: "btc-historical-performance-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-nfp-data-1-day-vs-gold.md": {
	id: "btc-historical-performance-after-nfp-data-1-day-vs-gold.md";
  slug: "btc-historical-performance-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-nfp-data-1-day-vs-sp500.md": {
	id: "btc-historical-performance-after-nfp-data-1-day-vs-sp500.md";
  slug: "btc-historical-performance-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-nfp-data-1-day.md": {
	id: "btc-historical-performance-after-nfp-data-1-day.md";
  slug: "btc-historical-performance-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-nfp-data-7-day-vs-gold.md": {
	id: "btc-historical-performance-after-nfp-data-7-day-vs-gold.md";
  slug: "btc-historical-performance-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-nfp-data-7-day-vs-sp500.md": {
	id: "btc-historical-performance-after-nfp-data-7-day-vs-sp500.md";
  slug: "btc-historical-performance-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-historical-performance-after-nfp-data-7-day.md": {
	id: "btc-historical-performance-after-nfp-data-7-day.md";
  slug: "btc-historical-performance-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-cpi-release-1-day-vs-gold.md": {
	id: "btc-price-impact-after-cpi-release-1-day-vs-gold.md";
  slug: "btc-price-impact-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-cpi-release-1-day-vs-sp500.md": {
	id: "btc-price-impact-after-cpi-release-1-day-vs-sp500.md";
  slug: "btc-price-impact-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-cpi-release-1-day.md": {
	id: "btc-price-impact-after-cpi-release-1-day.md";
  slug: "btc-price-impact-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-cpi-release-7-day-vs-gold.md": {
	id: "btc-price-impact-after-cpi-release-7-day-vs-gold.md";
  slug: "btc-price-impact-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-cpi-release-7-day-vs-sp500.md": {
	id: "btc-price-impact-after-cpi-release-7-day-vs-sp500.md";
  slug: "btc-price-impact-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-cpi-release-7-day.md": {
	id: "btc-price-impact-after-cpi-release-7-day.md";
  slug: "btc-price-impact-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "btc-price-impact-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "btc-price-impact-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "btc-price-impact-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "btc-price-impact-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-fed-rate-cut-1-day.md": {
	id: "btc-price-impact-after-fed-rate-cut-1-day.md";
  slug: "btc-price-impact-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "btc-price-impact-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "btc-price-impact-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "btc-price-impact-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "btc-price-impact-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-fed-rate-cut-7-day.md": {
	id: "btc-price-impact-after-fed-rate-cut-7-day.md";
  slug: "btc-price-impact-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-gdp-report-1-day-vs-gold.md": {
	id: "btc-price-impact-after-gdp-report-1-day-vs-gold.md";
  slug: "btc-price-impact-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-gdp-report-1-day-vs-sp500.md": {
	id: "btc-price-impact-after-gdp-report-1-day-vs-sp500.md";
  slug: "btc-price-impact-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-gdp-report-1-day.md": {
	id: "btc-price-impact-after-gdp-report-1-day.md";
  slug: "btc-price-impact-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-gdp-report-7-day-vs-gold.md": {
	id: "btc-price-impact-after-gdp-report-7-day-vs-gold.md";
  slug: "btc-price-impact-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-gdp-report-7-day-vs-sp500.md": {
	id: "btc-price-impact-after-gdp-report-7-day-vs-sp500.md";
  slug: "btc-price-impact-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-gdp-report-7-day.md": {
	id: "btc-price-impact-after-gdp-report-7-day.md";
  slug: "btc-price-impact-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-inflation-rate-1-day-vs-gold.md": {
	id: "btc-price-impact-after-inflation-rate-1-day-vs-gold.md";
  slug: "btc-price-impact-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-inflation-rate-1-day-vs-sp500.md": {
	id: "btc-price-impact-after-inflation-rate-1-day-vs-sp500.md";
  slug: "btc-price-impact-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-inflation-rate-1-day.md": {
	id: "btc-price-impact-after-inflation-rate-1-day.md";
  slug: "btc-price-impact-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-inflation-rate-7-day-vs-gold.md": {
	id: "btc-price-impact-after-inflation-rate-7-day-vs-gold.md";
  slug: "btc-price-impact-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-inflation-rate-7-day-vs-sp500.md": {
	id: "btc-price-impact-after-inflation-rate-7-day-vs-sp500.md";
  slug: "btc-price-impact-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-inflation-rate-7-day.md": {
	id: "btc-price-impact-after-inflation-rate-7-day.md";
  slug: "btc-price-impact-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-nfp-data-1-day-vs-gold.md": {
	id: "btc-price-impact-after-nfp-data-1-day-vs-gold.md";
  slug: "btc-price-impact-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-nfp-data-1-day-vs-sp500.md": {
	id: "btc-price-impact-after-nfp-data-1-day-vs-sp500.md";
  slug: "btc-price-impact-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-nfp-data-1-day.md": {
	id: "btc-price-impact-after-nfp-data-1-day.md";
  slug: "btc-price-impact-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-nfp-data-7-day-vs-gold.md": {
	id: "btc-price-impact-after-nfp-data-7-day-vs-gold.md";
  slug: "btc-price-impact-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-nfp-data-7-day-vs-sp500.md": {
	id: "btc-price-impact-after-nfp-data-7-day-vs-sp500.md";
  slug: "btc-price-impact-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-price-impact-after-nfp-data-7-day.md": {
	id: "btc-price-impact-after-nfp-data-7-day.md";
  slug: "btc-price-impact-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-cpi-release-1-day-vs-gold.md": {
	id: "btc-volatility-after-cpi-release-1-day-vs-gold.md";
  slug: "btc-volatility-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-cpi-release-1-day-vs-sp500.md": {
	id: "btc-volatility-after-cpi-release-1-day-vs-sp500.md";
  slug: "btc-volatility-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-cpi-release-1-day.md": {
	id: "btc-volatility-after-cpi-release-1-day.md";
  slug: "btc-volatility-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-cpi-release-7-day-vs-gold.md": {
	id: "btc-volatility-after-cpi-release-7-day-vs-gold.md";
  slug: "btc-volatility-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-cpi-release-7-day-vs-sp500.md": {
	id: "btc-volatility-after-cpi-release-7-day-vs-sp500.md";
  slug: "btc-volatility-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-cpi-release-7-day.md": {
	id: "btc-volatility-after-cpi-release-7-day.md";
  slug: "btc-volatility-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "btc-volatility-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "btc-volatility-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "btc-volatility-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "btc-volatility-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-fed-rate-cut-1-day.md": {
	id: "btc-volatility-after-fed-rate-cut-1-day.md";
  slug: "btc-volatility-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "btc-volatility-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "btc-volatility-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "btc-volatility-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "btc-volatility-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-fed-rate-cut-7-day.md": {
	id: "btc-volatility-after-fed-rate-cut-7-day.md";
  slug: "btc-volatility-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-gdp-report-1-day-vs-gold.md": {
	id: "btc-volatility-after-gdp-report-1-day-vs-gold.md";
  slug: "btc-volatility-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-gdp-report-1-day-vs-sp500.md": {
	id: "btc-volatility-after-gdp-report-1-day-vs-sp500.md";
  slug: "btc-volatility-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-gdp-report-1-day.md": {
	id: "btc-volatility-after-gdp-report-1-day.md";
  slug: "btc-volatility-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-gdp-report-7-day-vs-gold.md": {
	id: "btc-volatility-after-gdp-report-7-day-vs-gold.md";
  slug: "btc-volatility-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-gdp-report-7-day-vs-sp500.md": {
	id: "btc-volatility-after-gdp-report-7-day-vs-sp500.md";
  slug: "btc-volatility-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-gdp-report-7-day.md": {
	id: "btc-volatility-after-gdp-report-7-day.md";
  slug: "btc-volatility-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-inflation-rate-1-day-vs-gold.md": {
	id: "btc-volatility-after-inflation-rate-1-day-vs-gold.md";
  slug: "btc-volatility-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-inflation-rate-1-day-vs-sp500.md": {
	id: "btc-volatility-after-inflation-rate-1-day-vs-sp500.md";
  slug: "btc-volatility-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-inflation-rate-1-day.md": {
	id: "btc-volatility-after-inflation-rate-1-day.md";
  slug: "btc-volatility-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-inflation-rate-7-day-vs-gold.md": {
	id: "btc-volatility-after-inflation-rate-7-day-vs-gold.md";
  slug: "btc-volatility-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-inflation-rate-7-day-vs-sp500.md": {
	id: "btc-volatility-after-inflation-rate-7-day-vs-sp500.md";
  slug: "btc-volatility-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-inflation-rate-7-day.md": {
	id: "btc-volatility-after-inflation-rate-7-day.md";
  slug: "btc-volatility-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-nfp-data-1-day-vs-gold.md": {
	id: "btc-volatility-after-nfp-data-1-day-vs-gold.md";
  slug: "btc-volatility-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-nfp-data-1-day-vs-sp500.md": {
	id: "btc-volatility-after-nfp-data-1-day-vs-sp500.md";
  slug: "btc-volatility-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-nfp-data-1-day.md": {
	id: "btc-volatility-after-nfp-data-1-day.md";
  slug: "btc-volatility-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-nfp-data-7-day-vs-gold.md": {
	id: "btc-volatility-after-nfp-data-7-day-vs-gold.md";
  slug: "btc-volatility-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-nfp-data-7-day-vs-sp500.md": {
	id: "btc-volatility-after-nfp-data-7-day-vs-sp500.md";
  slug: "btc-volatility-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-volatility-after-nfp-data-7-day.md": {
	id: "btc-volatility-after-nfp-data-7-day.md";
  slug: "btc-volatility-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-after-geopolitics.md": {
	id: "eth-after-geopolitics.md";
  slug: "eth-after-geopolitics";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-after-macro.md": {
	id: "eth-after-macro.md";
  slug: "eth-after-macro";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-cpi-release-1-day-vs-gold.md": {
	id: "eth-correlation-after-cpi-release-1-day-vs-gold.md";
  slug: "eth-correlation-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-cpi-release-1-day-vs-sp500.md": {
	id: "eth-correlation-after-cpi-release-1-day-vs-sp500.md";
  slug: "eth-correlation-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-cpi-release-1-day.md": {
	id: "eth-correlation-after-cpi-release-1-day.md";
  slug: "eth-correlation-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-cpi-release-7-day-vs-gold.md": {
	id: "eth-correlation-after-cpi-release-7-day-vs-gold.md";
  slug: "eth-correlation-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-cpi-release-7-day-vs-sp500.md": {
	id: "eth-correlation-after-cpi-release-7-day-vs-sp500.md";
  slug: "eth-correlation-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-cpi-release-7-day.md": {
	id: "eth-correlation-after-cpi-release-7-day.md";
  slug: "eth-correlation-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "eth-correlation-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "eth-correlation-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "eth-correlation-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "eth-correlation-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-fed-rate-cut-1-day.md": {
	id: "eth-correlation-after-fed-rate-cut-1-day.md";
  slug: "eth-correlation-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "eth-correlation-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "eth-correlation-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "eth-correlation-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "eth-correlation-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-fed-rate-cut-7-day.md": {
	id: "eth-correlation-after-fed-rate-cut-7-day.md";
  slug: "eth-correlation-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-gdp-report-1-day-vs-gold.md": {
	id: "eth-correlation-after-gdp-report-1-day-vs-gold.md";
  slug: "eth-correlation-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-gdp-report-1-day-vs-sp500.md": {
	id: "eth-correlation-after-gdp-report-1-day-vs-sp500.md";
  slug: "eth-correlation-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-gdp-report-1-day.md": {
	id: "eth-correlation-after-gdp-report-1-day.md";
  slug: "eth-correlation-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-gdp-report-7-day-vs-gold.md": {
	id: "eth-correlation-after-gdp-report-7-day-vs-gold.md";
  slug: "eth-correlation-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-gdp-report-7-day-vs-sp500.md": {
	id: "eth-correlation-after-gdp-report-7-day-vs-sp500.md";
  slug: "eth-correlation-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-gdp-report-7-day.md": {
	id: "eth-correlation-after-gdp-report-7-day.md";
  slug: "eth-correlation-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-inflation-rate-1-day-vs-gold.md": {
	id: "eth-correlation-after-inflation-rate-1-day-vs-gold.md";
  slug: "eth-correlation-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-inflation-rate-1-day-vs-sp500.md": {
	id: "eth-correlation-after-inflation-rate-1-day-vs-sp500.md";
  slug: "eth-correlation-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-inflation-rate-1-day.md": {
	id: "eth-correlation-after-inflation-rate-1-day.md";
  slug: "eth-correlation-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-inflation-rate-7-day-vs-gold.md": {
	id: "eth-correlation-after-inflation-rate-7-day-vs-gold.md";
  slug: "eth-correlation-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-inflation-rate-7-day-vs-sp500.md": {
	id: "eth-correlation-after-inflation-rate-7-day-vs-sp500.md";
  slug: "eth-correlation-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-inflation-rate-7-day.md": {
	id: "eth-correlation-after-inflation-rate-7-day.md";
  slug: "eth-correlation-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-nfp-data-1-day-vs-gold.md": {
	id: "eth-correlation-after-nfp-data-1-day-vs-gold.md";
  slug: "eth-correlation-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-nfp-data-1-day-vs-sp500.md": {
	id: "eth-correlation-after-nfp-data-1-day-vs-sp500.md";
  slug: "eth-correlation-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-nfp-data-1-day.md": {
	id: "eth-correlation-after-nfp-data-1-day.md";
  slug: "eth-correlation-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-nfp-data-7-day-vs-gold.md": {
	id: "eth-correlation-after-nfp-data-7-day-vs-gold.md";
  slug: "eth-correlation-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-nfp-data-7-day-vs-sp500.md": {
	id: "eth-correlation-after-nfp-data-7-day-vs-sp500.md";
  slug: "eth-correlation-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-correlation-after-nfp-data-7-day.md": {
	id: "eth-correlation-after-nfp-data-7-day.md";
  slug: "eth-correlation-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-cpi-release-1-day-vs-gold.md": {
	id: "eth-historical-performance-after-cpi-release-1-day-vs-gold.md";
  slug: "eth-historical-performance-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-cpi-release-1-day-vs-sp500.md": {
	id: "eth-historical-performance-after-cpi-release-1-day-vs-sp500.md";
  slug: "eth-historical-performance-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-cpi-release-1-day.md": {
	id: "eth-historical-performance-after-cpi-release-1-day.md";
  slug: "eth-historical-performance-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-cpi-release-7-day-vs-gold.md": {
	id: "eth-historical-performance-after-cpi-release-7-day-vs-gold.md";
  slug: "eth-historical-performance-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-cpi-release-7-day-vs-sp500.md": {
	id: "eth-historical-performance-after-cpi-release-7-day-vs-sp500.md";
  slug: "eth-historical-performance-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-cpi-release-7-day.md": {
	id: "eth-historical-performance-after-cpi-release-7-day.md";
  slug: "eth-historical-performance-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "eth-historical-performance-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "eth-historical-performance-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "eth-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "eth-historical-performance-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-fed-rate-cut-1-day.md": {
	id: "eth-historical-performance-after-fed-rate-cut-1-day.md";
  slug: "eth-historical-performance-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "eth-historical-performance-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "eth-historical-performance-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "eth-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "eth-historical-performance-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-fed-rate-cut-7-day.md": {
	id: "eth-historical-performance-after-fed-rate-cut-7-day.md";
  slug: "eth-historical-performance-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-gdp-report-1-day-vs-gold.md": {
	id: "eth-historical-performance-after-gdp-report-1-day-vs-gold.md";
  slug: "eth-historical-performance-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-gdp-report-1-day-vs-sp500.md": {
	id: "eth-historical-performance-after-gdp-report-1-day-vs-sp500.md";
  slug: "eth-historical-performance-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-gdp-report-1-day.md": {
	id: "eth-historical-performance-after-gdp-report-1-day.md";
  slug: "eth-historical-performance-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-gdp-report-7-day-vs-gold.md": {
	id: "eth-historical-performance-after-gdp-report-7-day-vs-gold.md";
  slug: "eth-historical-performance-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-gdp-report-7-day-vs-sp500.md": {
	id: "eth-historical-performance-after-gdp-report-7-day-vs-sp500.md";
  slug: "eth-historical-performance-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-gdp-report-7-day.md": {
	id: "eth-historical-performance-after-gdp-report-7-day.md";
  slug: "eth-historical-performance-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-inflation-rate-1-day-vs-gold.md": {
	id: "eth-historical-performance-after-inflation-rate-1-day-vs-gold.md";
  slug: "eth-historical-performance-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-inflation-rate-1-day-vs-sp500.md": {
	id: "eth-historical-performance-after-inflation-rate-1-day-vs-sp500.md";
  slug: "eth-historical-performance-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-inflation-rate-1-day.md": {
	id: "eth-historical-performance-after-inflation-rate-1-day.md";
  slug: "eth-historical-performance-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-inflation-rate-7-day-vs-gold.md": {
	id: "eth-historical-performance-after-inflation-rate-7-day-vs-gold.md";
  slug: "eth-historical-performance-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-inflation-rate-7-day-vs-sp500.md": {
	id: "eth-historical-performance-after-inflation-rate-7-day-vs-sp500.md";
  slug: "eth-historical-performance-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-inflation-rate-7-day.md": {
	id: "eth-historical-performance-after-inflation-rate-7-day.md";
  slug: "eth-historical-performance-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-nfp-data-1-day-vs-gold.md": {
	id: "eth-historical-performance-after-nfp-data-1-day-vs-gold.md";
  slug: "eth-historical-performance-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-nfp-data-1-day-vs-sp500.md": {
	id: "eth-historical-performance-after-nfp-data-1-day-vs-sp500.md";
  slug: "eth-historical-performance-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-nfp-data-1-day.md": {
	id: "eth-historical-performance-after-nfp-data-1-day.md";
  slug: "eth-historical-performance-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-nfp-data-7-day-vs-gold.md": {
	id: "eth-historical-performance-after-nfp-data-7-day-vs-gold.md";
  slug: "eth-historical-performance-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-nfp-data-7-day-vs-sp500.md": {
	id: "eth-historical-performance-after-nfp-data-7-day-vs-sp500.md";
  slug: "eth-historical-performance-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-historical-performance-after-nfp-data-7-day.md": {
	id: "eth-historical-performance-after-nfp-data-7-day.md";
  slug: "eth-historical-performance-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-cpi-release-1-day-vs-gold.md": {
	id: "eth-price-impact-after-cpi-release-1-day-vs-gold.md";
  slug: "eth-price-impact-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-cpi-release-1-day-vs-sp500.md": {
	id: "eth-price-impact-after-cpi-release-1-day-vs-sp500.md";
  slug: "eth-price-impact-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-cpi-release-1-day.md": {
	id: "eth-price-impact-after-cpi-release-1-day.md";
  slug: "eth-price-impact-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-cpi-release-7-day-vs-gold.md": {
	id: "eth-price-impact-after-cpi-release-7-day-vs-gold.md";
  slug: "eth-price-impact-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-cpi-release-7-day-vs-sp500.md": {
	id: "eth-price-impact-after-cpi-release-7-day-vs-sp500.md";
  slug: "eth-price-impact-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-cpi-release-7-day.md": {
	id: "eth-price-impact-after-cpi-release-7-day.md";
  slug: "eth-price-impact-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "eth-price-impact-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "eth-price-impact-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "eth-price-impact-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "eth-price-impact-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-fed-rate-cut-1-day.md": {
	id: "eth-price-impact-after-fed-rate-cut-1-day.md";
  slug: "eth-price-impact-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "eth-price-impact-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "eth-price-impact-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "eth-price-impact-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "eth-price-impact-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-fed-rate-cut-7-day.md": {
	id: "eth-price-impact-after-fed-rate-cut-7-day.md";
  slug: "eth-price-impact-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-gdp-report-1-day-vs-gold.md": {
	id: "eth-price-impact-after-gdp-report-1-day-vs-gold.md";
  slug: "eth-price-impact-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-gdp-report-1-day-vs-sp500.md": {
	id: "eth-price-impact-after-gdp-report-1-day-vs-sp500.md";
  slug: "eth-price-impact-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-gdp-report-1-day.md": {
	id: "eth-price-impact-after-gdp-report-1-day.md";
  slug: "eth-price-impact-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-gdp-report-7-day-vs-gold.md": {
	id: "eth-price-impact-after-gdp-report-7-day-vs-gold.md";
  slug: "eth-price-impact-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-gdp-report-7-day-vs-sp500.md": {
	id: "eth-price-impact-after-gdp-report-7-day-vs-sp500.md";
  slug: "eth-price-impact-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-gdp-report-7-day.md": {
	id: "eth-price-impact-after-gdp-report-7-day.md";
  slug: "eth-price-impact-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-inflation-rate-1-day-vs-gold.md": {
	id: "eth-price-impact-after-inflation-rate-1-day-vs-gold.md";
  slug: "eth-price-impact-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-inflation-rate-1-day-vs-sp500.md": {
	id: "eth-price-impact-after-inflation-rate-1-day-vs-sp500.md";
  slug: "eth-price-impact-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-inflation-rate-1-day.md": {
	id: "eth-price-impact-after-inflation-rate-1-day.md";
  slug: "eth-price-impact-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-inflation-rate-7-day-vs-gold.md": {
	id: "eth-price-impact-after-inflation-rate-7-day-vs-gold.md";
  slug: "eth-price-impact-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-inflation-rate-7-day-vs-sp500.md": {
	id: "eth-price-impact-after-inflation-rate-7-day-vs-sp500.md";
  slug: "eth-price-impact-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-inflation-rate-7-day.md": {
	id: "eth-price-impact-after-inflation-rate-7-day.md";
  slug: "eth-price-impact-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-nfp-data-1-day-vs-gold.md": {
	id: "eth-price-impact-after-nfp-data-1-day-vs-gold.md";
  slug: "eth-price-impact-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-nfp-data-1-day-vs-sp500.md": {
	id: "eth-price-impact-after-nfp-data-1-day-vs-sp500.md";
  slug: "eth-price-impact-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-nfp-data-1-day.md": {
	id: "eth-price-impact-after-nfp-data-1-day.md";
  slug: "eth-price-impact-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-nfp-data-7-day-vs-gold.md": {
	id: "eth-price-impact-after-nfp-data-7-day-vs-gold.md";
  slug: "eth-price-impact-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-nfp-data-7-day-vs-sp500.md": {
	id: "eth-price-impact-after-nfp-data-7-day-vs-sp500.md";
  slug: "eth-price-impact-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-price-impact-after-nfp-data-7-day.md": {
	id: "eth-price-impact-after-nfp-data-7-day.md";
  slug: "eth-price-impact-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-cpi-release-1-day-vs-gold.md": {
	id: "eth-volatility-after-cpi-release-1-day-vs-gold.md";
  slug: "eth-volatility-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-cpi-release-1-day-vs-sp500.md": {
	id: "eth-volatility-after-cpi-release-1-day-vs-sp500.md";
  slug: "eth-volatility-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-cpi-release-1-day.md": {
	id: "eth-volatility-after-cpi-release-1-day.md";
  slug: "eth-volatility-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-cpi-release-7-day-vs-gold.md": {
	id: "eth-volatility-after-cpi-release-7-day-vs-gold.md";
  slug: "eth-volatility-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-cpi-release-7-day-vs-sp500.md": {
	id: "eth-volatility-after-cpi-release-7-day-vs-sp500.md";
  slug: "eth-volatility-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-cpi-release-7-day.md": {
	id: "eth-volatility-after-cpi-release-7-day.md";
  slug: "eth-volatility-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "eth-volatility-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "eth-volatility-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "eth-volatility-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "eth-volatility-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-fed-rate-cut-1-day.md": {
	id: "eth-volatility-after-fed-rate-cut-1-day.md";
  slug: "eth-volatility-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "eth-volatility-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "eth-volatility-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "eth-volatility-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "eth-volatility-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-fed-rate-cut-7-day.md": {
	id: "eth-volatility-after-fed-rate-cut-7-day.md";
  slug: "eth-volatility-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-gdp-report-1-day-vs-gold.md": {
	id: "eth-volatility-after-gdp-report-1-day-vs-gold.md";
  slug: "eth-volatility-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-gdp-report-1-day-vs-sp500.md": {
	id: "eth-volatility-after-gdp-report-1-day-vs-sp500.md";
  slug: "eth-volatility-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-gdp-report-1-day.md": {
	id: "eth-volatility-after-gdp-report-1-day.md";
  slug: "eth-volatility-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-gdp-report-7-day-vs-gold.md": {
	id: "eth-volatility-after-gdp-report-7-day-vs-gold.md";
  slug: "eth-volatility-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-gdp-report-7-day-vs-sp500.md": {
	id: "eth-volatility-after-gdp-report-7-day-vs-sp500.md";
  slug: "eth-volatility-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-gdp-report-7-day.md": {
	id: "eth-volatility-after-gdp-report-7-day.md";
  slug: "eth-volatility-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-inflation-rate-1-day-vs-gold.md": {
	id: "eth-volatility-after-inflation-rate-1-day-vs-gold.md";
  slug: "eth-volatility-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-inflation-rate-1-day-vs-sp500.md": {
	id: "eth-volatility-after-inflation-rate-1-day-vs-sp500.md";
  slug: "eth-volatility-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-inflation-rate-1-day.md": {
	id: "eth-volatility-after-inflation-rate-1-day.md";
  slug: "eth-volatility-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-inflation-rate-7-day-vs-gold.md": {
	id: "eth-volatility-after-inflation-rate-7-day-vs-gold.md";
  slug: "eth-volatility-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-inflation-rate-7-day-vs-sp500.md": {
	id: "eth-volatility-after-inflation-rate-7-day-vs-sp500.md";
  slug: "eth-volatility-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-inflation-rate-7-day.md": {
	id: "eth-volatility-after-inflation-rate-7-day.md";
  slug: "eth-volatility-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-nfp-data-1-day-vs-gold.md": {
	id: "eth-volatility-after-nfp-data-1-day-vs-gold.md";
  slug: "eth-volatility-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-nfp-data-1-day-vs-sp500.md": {
	id: "eth-volatility-after-nfp-data-1-day-vs-sp500.md";
  slug: "eth-volatility-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-nfp-data-1-day.md": {
	id: "eth-volatility-after-nfp-data-1-day.md";
  slug: "eth-volatility-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-nfp-data-7-day-vs-gold.md": {
	id: "eth-volatility-after-nfp-data-7-day-vs-gold.md";
  slug: "eth-volatility-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-nfp-data-7-day-vs-sp500.md": {
	id: "eth-volatility-after-nfp-data-7-day-vs-sp500.md";
  slug: "eth-volatility-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-volatility-after-nfp-data-7-day.md": {
	id: "eth-volatility-after-nfp-data-7-day.md";
  slug: "eth-volatility-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-cpi-release-1-day-vs-gold.md": {
	id: "gold-correlation-after-cpi-release-1-day-vs-gold.md";
  slug: "gold-correlation-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-cpi-release-1-day-vs-sp500.md": {
	id: "gold-correlation-after-cpi-release-1-day-vs-sp500.md";
  slug: "gold-correlation-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-cpi-release-1-day.md": {
	id: "gold-correlation-after-cpi-release-1-day.md";
  slug: "gold-correlation-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-cpi-release-7-day-vs-gold.md": {
	id: "gold-correlation-after-cpi-release-7-day-vs-gold.md";
  slug: "gold-correlation-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-cpi-release-7-day-vs-sp500.md": {
	id: "gold-correlation-after-cpi-release-7-day-vs-sp500.md";
  slug: "gold-correlation-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-cpi-release-7-day.md": {
	id: "gold-correlation-after-cpi-release-7-day.md";
  slug: "gold-correlation-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "gold-correlation-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "gold-correlation-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "gold-correlation-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "gold-correlation-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-fed-rate-cut-1-day.md": {
	id: "gold-correlation-after-fed-rate-cut-1-day.md";
  slug: "gold-correlation-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "gold-correlation-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "gold-correlation-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "gold-correlation-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "gold-correlation-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-fed-rate-cut-7-day.md": {
	id: "gold-correlation-after-fed-rate-cut-7-day.md";
  slug: "gold-correlation-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-gdp-report-1-day-vs-gold.md": {
	id: "gold-correlation-after-gdp-report-1-day-vs-gold.md";
  slug: "gold-correlation-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-gdp-report-1-day-vs-sp500.md": {
	id: "gold-correlation-after-gdp-report-1-day-vs-sp500.md";
  slug: "gold-correlation-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-gdp-report-1-day.md": {
	id: "gold-correlation-after-gdp-report-1-day.md";
  slug: "gold-correlation-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-gdp-report-7-day-vs-gold.md": {
	id: "gold-correlation-after-gdp-report-7-day-vs-gold.md";
  slug: "gold-correlation-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-gdp-report-7-day-vs-sp500.md": {
	id: "gold-correlation-after-gdp-report-7-day-vs-sp500.md";
  slug: "gold-correlation-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-gdp-report-7-day.md": {
	id: "gold-correlation-after-gdp-report-7-day.md";
  slug: "gold-correlation-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-inflation-rate-1-day-vs-gold.md": {
	id: "gold-correlation-after-inflation-rate-1-day-vs-gold.md";
  slug: "gold-correlation-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-inflation-rate-1-day-vs-sp500.md": {
	id: "gold-correlation-after-inflation-rate-1-day-vs-sp500.md";
  slug: "gold-correlation-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-inflation-rate-1-day.md": {
	id: "gold-correlation-after-inflation-rate-1-day.md";
  slug: "gold-correlation-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-inflation-rate-7-day-vs-gold.md": {
	id: "gold-correlation-after-inflation-rate-7-day-vs-gold.md";
  slug: "gold-correlation-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-inflation-rate-7-day-vs-sp500.md": {
	id: "gold-correlation-after-inflation-rate-7-day-vs-sp500.md";
  slug: "gold-correlation-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-inflation-rate-7-day.md": {
	id: "gold-correlation-after-inflation-rate-7-day.md";
  slug: "gold-correlation-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-nfp-data-1-day-vs-gold.md": {
	id: "gold-correlation-after-nfp-data-1-day-vs-gold.md";
  slug: "gold-correlation-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-nfp-data-1-day-vs-sp500.md": {
	id: "gold-correlation-after-nfp-data-1-day-vs-sp500.md";
  slug: "gold-correlation-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-nfp-data-1-day.md": {
	id: "gold-correlation-after-nfp-data-1-day.md";
  slug: "gold-correlation-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-nfp-data-7-day-vs-gold.md": {
	id: "gold-correlation-after-nfp-data-7-day-vs-gold.md";
  slug: "gold-correlation-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-nfp-data-7-day-vs-sp500.md": {
	id: "gold-correlation-after-nfp-data-7-day-vs-sp500.md";
  slug: "gold-correlation-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-correlation-after-nfp-data-7-day.md": {
	id: "gold-correlation-after-nfp-data-7-day.md";
  slug: "gold-correlation-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-cpi-release-1-day-vs-gold.md": {
	id: "gold-historical-performance-after-cpi-release-1-day-vs-gold.md";
  slug: "gold-historical-performance-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-cpi-release-1-day-vs-sp500.md": {
	id: "gold-historical-performance-after-cpi-release-1-day-vs-sp500.md";
  slug: "gold-historical-performance-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-cpi-release-1-day.md": {
	id: "gold-historical-performance-after-cpi-release-1-day.md";
  slug: "gold-historical-performance-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-cpi-release-7-day-vs-gold.md": {
	id: "gold-historical-performance-after-cpi-release-7-day-vs-gold.md";
  slug: "gold-historical-performance-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-cpi-release-7-day-vs-sp500.md": {
	id: "gold-historical-performance-after-cpi-release-7-day-vs-sp500.md";
  slug: "gold-historical-performance-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-cpi-release-7-day.md": {
	id: "gold-historical-performance-after-cpi-release-7-day.md";
  slug: "gold-historical-performance-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "gold-historical-performance-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "gold-historical-performance-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "gold-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "gold-historical-performance-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-fed-rate-cut-1-day.md": {
	id: "gold-historical-performance-after-fed-rate-cut-1-day.md";
  slug: "gold-historical-performance-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "gold-historical-performance-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "gold-historical-performance-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "gold-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "gold-historical-performance-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-fed-rate-cut-7-day.md": {
	id: "gold-historical-performance-after-fed-rate-cut-7-day.md";
  slug: "gold-historical-performance-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-gdp-report-1-day-vs-gold.md": {
	id: "gold-historical-performance-after-gdp-report-1-day-vs-gold.md";
  slug: "gold-historical-performance-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-gdp-report-1-day-vs-sp500.md": {
	id: "gold-historical-performance-after-gdp-report-1-day-vs-sp500.md";
  slug: "gold-historical-performance-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-gdp-report-1-day.md": {
	id: "gold-historical-performance-after-gdp-report-1-day.md";
  slug: "gold-historical-performance-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-gdp-report-7-day-vs-gold.md": {
	id: "gold-historical-performance-after-gdp-report-7-day-vs-gold.md";
  slug: "gold-historical-performance-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-gdp-report-7-day-vs-sp500.md": {
	id: "gold-historical-performance-after-gdp-report-7-day-vs-sp500.md";
  slug: "gold-historical-performance-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-gdp-report-7-day.md": {
	id: "gold-historical-performance-after-gdp-report-7-day.md";
  slug: "gold-historical-performance-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-inflation-rate-1-day-vs-gold.md": {
	id: "gold-historical-performance-after-inflation-rate-1-day-vs-gold.md";
  slug: "gold-historical-performance-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-inflation-rate-1-day-vs-sp500.md": {
	id: "gold-historical-performance-after-inflation-rate-1-day-vs-sp500.md";
  slug: "gold-historical-performance-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-inflation-rate-1-day.md": {
	id: "gold-historical-performance-after-inflation-rate-1-day.md";
  slug: "gold-historical-performance-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-inflation-rate-7-day-vs-gold.md": {
	id: "gold-historical-performance-after-inflation-rate-7-day-vs-gold.md";
  slug: "gold-historical-performance-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-inflation-rate-7-day-vs-sp500.md": {
	id: "gold-historical-performance-after-inflation-rate-7-day-vs-sp500.md";
  slug: "gold-historical-performance-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-inflation-rate-7-day.md": {
	id: "gold-historical-performance-after-inflation-rate-7-day.md";
  slug: "gold-historical-performance-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-nfp-data-1-day-vs-gold.md": {
	id: "gold-historical-performance-after-nfp-data-1-day-vs-gold.md";
  slug: "gold-historical-performance-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-nfp-data-1-day-vs-sp500.md": {
	id: "gold-historical-performance-after-nfp-data-1-day-vs-sp500.md";
  slug: "gold-historical-performance-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-nfp-data-1-day.md": {
	id: "gold-historical-performance-after-nfp-data-1-day.md";
  slug: "gold-historical-performance-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-nfp-data-7-day-vs-gold.md": {
	id: "gold-historical-performance-after-nfp-data-7-day-vs-gold.md";
  slug: "gold-historical-performance-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-nfp-data-7-day-vs-sp500.md": {
	id: "gold-historical-performance-after-nfp-data-7-day-vs-sp500.md";
  slug: "gold-historical-performance-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-historical-performance-after-nfp-data-7-day.md": {
	id: "gold-historical-performance-after-nfp-data-7-day.md";
  slug: "gold-historical-performance-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-cpi-release-1-day-vs-gold.md": {
	id: "gold-price-impact-after-cpi-release-1-day-vs-gold.md";
  slug: "gold-price-impact-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-cpi-release-1-day-vs-sp500.md": {
	id: "gold-price-impact-after-cpi-release-1-day-vs-sp500.md";
  slug: "gold-price-impact-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-cpi-release-1-day.md": {
	id: "gold-price-impact-after-cpi-release-1-day.md";
  slug: "gold-price-impact-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-cpi-release-7-day-vs-gold.md": {
	id: "gold-price-impact-after-cpi-release-7-day-vs-gold.md";
  slug: "gold-price-impact-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-cpi-release-7-day-vs-sp500.md": {
	id: "gold-price-impact-after-cpi-release-7-day-vs-sp500.md";
  slug: "gold-price-impact-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-cpi-release-7-day.md": {
	id: "gold-price-impact-after-cpi-release-7-day.md";
  slug: "gold-price-impact-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "gold-price-impact-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "gold-price-impact-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "gold-price-impact-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "gold-price-impact-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-fed-rate-cut-1-day.md": {
	id: "gold-price-impact-after-fed-rate-cut-1-day.md";
  slug: "gold-price-impact-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "gold-price-impact-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "gold-price-impact-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "gold-price-impact-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "gold-price-impact-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-fed-rate-cut-7-day.md": {
	id: "gold-price-impact-after-fed-rate-cut-7-day.md";
  slug: "gold-price-impact-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-gdp-report-1-day-vs-gold.md": {
	id: "gold-price-impact-after-gdp-report-1-day-vs-gold.md";
  slug: "gold-price-impact-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-gdp-report-1-day-vs-sp500.md": {
	id: "gold-price-impact-after-gdp-report-1-day-vs-sp500.md";
  slug: "gold-price-impact-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-gdp-report-1-day.md": {
	id: "gold-price-impact-after-gdp-report-1-day.md";
  slug: "gold-price-impact-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-gdp-report-7-day-vs-gold.md": {
	id: "gold-price-impact-after-gdp-report-7-day-vs-gold.md";
  slug: "gold-price-impact-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-gdp-report-7-day-vs-sp500.md": {
	id: "gold-price-impact-after-gdp-report-7-day-vs-sp500.md";
  slug: "gold-price-impact-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-gdp-report-7-day.md": {
	id: "gold-price-impact-after-gdp-report-7-day.md";
  slug: "gold-price-impact-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-inflation-rate-1-day-vs-gold.md": {
	id: "gold-price-impact-after-inflation-rate-1-day-vs-gold.md";
  slug: "gold-price-impact-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-inflation-rate-1-day-vs-sp500.md": {
	id: "gold-price-impact-after-inflation-rate-1-day-vs-sp500.md";
  slug: "gold-price-impact-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-inflation-rate-1-day.md": {
	id: "gold-price-impact-after-inflation-rate-1-day.md";
  slug: "gold-price-impact-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-inflation-rate-7-day-vs-gold.md": {
	id: "gold-price-impact-after-inflation-rate-7-day-vs-gold.md";
  slug: "gold-price-impact-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-inflation-rate-7-day-vs-sp500.md": {
	id: "gold-price-impact-after-inflation-rate-7-day-vs-sp500.md";
  slug: "gold-price-impact-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-inflation-rate-7-day.md": {
	id: "gold-price-impact-after-inflation-rate-7-day.md";
  slug: "gold-price-impact-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-nfp-data-1-day-vs-gold.md": {
	id: "gold-price-impact-after-nfp-data-1-day-vs-gold.md";
  slug: "gold-price-impact-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-nfp-data-1-day-vs-sp500.md": {
	id: "gold-price-impact-after-nfp-data-1-day-vs-sp500.md";
  slug: "gold-price-impact-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-nfp-data-1-day.md": {
	id: "gold-price-impact-after-nfp-data-1-day.md";
  slug: "gold-price-impact-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-nfp-data-7-day-vs-gold.md": {
	id: "gold-price-impact-after-nfp-data-7-day-vs-gold.md";
  slug: "gold-price-impact-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-nfp-data-7-day-vs-sp500.md": {
	id: "gold-price-impact-after-nfp-data-7-day-vs-sp500.md";
  slug: "gold-price-impact-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-price-impact-after-nfp-data-7-day.md": {
	id: "gold-price-impact-after-nfp-data-7-day.md";
  slug: "gold-price-impact-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-cpi-release-1-day-vs-gold.md": {
	id: "gold-volatility-after-cpi-release-1-day-vs-gold.md";
  slug: "gold-volatility-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-cpi-release-1-day-vs-sp500.md": {
	id: "gold-volatility-after-cpi-release-1-day-vs-sp500.md";
  slug: "gold-volatility-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-cpi-release-1-day.md": {
	id: "gold-volatility-after-cpi-release-1-day.md";
  slug: "gold-volatility-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-cpi-release-7-day-vs-gold.md": {
	id: "gold-volatility-after-cpi-release-7-day-vs-gold.md";
  slug: "gold-volatility-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-cpi-release-7-day-vs-sp500.md": {
	id: "gold-volatility-after-cpi-release-7-day-vs-sp500.md";
  slug: "gold-volatility-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-cpi-release-7-day.md": {
	id: "gold-volatility-after-cpi-release-7-day.md";
  slug: "gold-volatility-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "gold-volatility-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "gold-volatility-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "gold-volatility-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "gold-volatility-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-fed-rate-cut-1-day.md": {
	id: "gold-volatility-after-fed-rate-cut-1-day.md";
  slug: "gold-volatility-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "gold-volatility-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "gold-volatility-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "gold-volatility-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "gold-volatility-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-fed-rate-cut-7-day.md": {
	id: "gold-volatility-after-fed-rate-cut-7-day.md";
  slug: "gold-volatility-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-gdp-report-1-day-vs-gold.md": {
	id: "gold-volatility-after-gdp-report-1-day-vs-gold.md";
  slug: "gold-volatility-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-gdp-report-1-day-vs-sp500.md": {
	id: "gold-volatility-after-gdp-report-1-day-vs-sp500.md";
  slug: "gold-volatility-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-gdp-report-1-day.md": {
	id: "gold-volatility-after-gdp-report-1-day.md";
  slug: "gold-volatility-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-gdp-report-7-day-vs-gold.md": {
	id: "gold-volatility-after-gdp-report-7-day-vs-gold.md";
  slug: "gold-volatility-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-gdp-report-7-day-vs-sp500.md": {
	id: "gold-volatility-after-gdp-report-7-day-vs-sp500.md";
  slug: "gold-volatility-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-gdp-report-7-day.md": {
	id: "gold-volatility-after-gdp-report-7-day.md";
  slug: "gold-volatility-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-inflation-rate-1-day-vs-gold.md": {
	id: "gold-volatility-after-inflation-rate-1-day-vs-gold.md";
  slug: "gold-volatility-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-inflation-rate-1-day-vs-sp500.md": {
	id: "gold-volatility-after-inflation-rate-1-day-vs-sp500.md";
  slug: "gold-volatility-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-inflation-rate-1-day.md": {
	id: "gold-volatility-after-inflation-rate-1-day.md";
  slug: "gold-volatility-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-inflation-rate-7-day-vs-gold.md": {
	id: "gold-volatility-after-inflation-rate-7-day-vs-gold.md";
  slug: "gold-volatility-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-inflation-rate-7-day-vs-sp500.md": {
	id: "gold-volatility-after-inflation-rate-7-day-vs-sp500.md";
  slug: "gold-volatility-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-inflation-rate-7-day.md": {
	id: "gold-volatility-after-inflation-rate-7-day.md";
  slug: "gold-volatility-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-nfp-data-1-day-vs-gold.md": {
	id: "gold-volatility-after-nfp-data-1-day-vs-gold.md";
  slug: "gold-volatility-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-nfp-data-1-day-vs-sp500.md": {
	id: "gold-volatility-after-nfp-data-1-day-vs-sp500.md";
  slug: "gold-volatility-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-nfp-data-1-day.md": {
	id: "gold-volatility-after-nfp-data-1-day.md";
  slug: "gold-volatility-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-nfp-data-7-day-vs-gold.md": {
	id: "gold-volatility-after-nfp-data-7-day-vs-gold.md";
  slug: "gold-volatility-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-nfp-data-7-day-vs-sp500.md": {
	id: "gold-volatility-after-nfp-data-7-day-vs-sp500.md";
  slug: "gold-volatility-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-volatility-after-nfp-data-7-day.md": {
	id: "gold-volatility-after-nfp-data-7-day.md";
  slug: "gold-volatility-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-cpi-release-1-day-vs-gold.md": {
	id: "nvda-correlation-after-cpi-release-1-day-vs-gold.md";
  slug: "nvda-correlation-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-cpi-release-1-day-vs-sp500.md": {
	id: "nvda-correlation-after-cpi-release-1-day-vs-sp500.md";
  slug: "nvda-correlation-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-cpi-release-1-day.md": {
	id: "nvda-correlation-after-cpi-release-1-day.md";
  slug: "nvda-correlation-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-cpi-release-7-day-vs-gold.md": {
	id: "nvda-correlation-after-cpi-release-7-day-vs-gold.md";
  slug: "nvda-correlation-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-cpi-release-7-day-vs-sp500.md": {
	id: "nvda-correlation-after-cpi-release-7-day-vs-sp500.md";
  slug: "nvda-correlation-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-cpi-release-7-day.md": {
	id: "nvda-correlation-after-cpi-release-7-day.md";
  slug: "nvda-correlation-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "nvda-correlation-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "nvda-correlation-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "nvda-correlation-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "nvda-correlation-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-fed-rate-cut-1-day.md": {
	id: "nvda-correlation-after-fed-rate-cut-1-day.md";
  slug: "nvda-correlation-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "nvda-correlation-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "nvda-correlation-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "nvda-correlation-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "nvda-correlation-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-fed-rate-cut-7-day.md": {
	id: "nvda-correlation-after-fed-rate-cut-7-day.md";
  slug: "nvda-correlation-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-gdp-report-1-day-vs-gold.md": {
	id: "nvda-correlation-after-gdp-report-1-day-vs-gold.md";
  slug: "nvda-correlation-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-gdp-report-1-day-vs-sp500.md": {
	id: "nvda-correlation-after-gdp-report-1-day-vs-sp500.md";
  slug: "nvda-correlation-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-gdp-report-1-day.md": {
	id: "nvda-correlation-after-gdp-report-1-day.md";
  slug: "nvda-correlation-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-gdp-report-7-day-vs-gold.md": {
	id: "nvda-correlation-after-gdp-report-7-day-vs-gold.md";
  slug: "nvda-correlation-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-gdp-report-7-day-vs-sp500.md": {
	id: "nvda-correlation-after-gdp-report-7-day-vs-sp500.md";
  slug: "nvda-correlation-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-gdp-report-7-day.md": {
	id: "nvda-correlation-after-gdp-report-7-day.md";
  slug: "nvda-correlation-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-inflation-rate-1-day-vs-gold.md": {
	id: "nvda-correlation-after-inflation-rate-1-day-vs-gold.md";
  slug: "nvda-correlation-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-inflation-rate-1-day-vs-sp500.md": {
	id: "nvda-correlation-after-inflation-rate-1-day-vs-sp500.md";
  slug: "nvda-correlation-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-inflation-rate-1-day.md": {
	id: "nvda-correlation-after-inflation-rate-1-day.md";
  slug: "nvda-correlation-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-inflation-rate-7-day-vs-gold.md": {
	id: "nvda-correlation-after-inflation-rate-7-day-vs-gold.md";
  slug: "nvda-correlation-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-inflation-rate-7-day-vs-sp500.md": {
	id: "nvda-correlation-after-inflation-rate-7-day-vs-sp500.md";
  slug: "nvda-correlation-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-inflation-rate-7-day.md": {
	id: "nvda-correlation-after-inflation-rate-7-day.md";
  slug: "nvda-correlation-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-nfp-data-1-day-vs-gold.md": {
	id: "nvda-correlation-after-nfp-data-1-day-vs-gold.md";
  slug: "nvda-correlation-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-nfp-data-1-day-vs-sp500.md": {
	id: "nvda-correlation-after-nfp-data-1-day-vs-sp500.md";
  slug: "nvda-correlation-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-nfp-data-1-day.md": {
	id: "nvda-correlation-after-nfp-data-1-day.md";
  slug: "nvda-correlation-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-nfp-data-7-day-vs-gold.md": {
	id: "nvda-correlation-after-nfp-data-7-day-vs-gold.md";
  slug: "nvda-correlation-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-nfp-data-7-day-vs-sp500.md": {
	id: "nvda-correlation-after-nfp-data-7-day-vs-sp500.md";
  slug: "nvda-correlation-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-correlation-after-nfp-data-7-day.md": {
	id: "nvda-correlation-after-nfp-data-7-day.md";
  slug: "nvda-correlation-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-cpi-release-1-day-vs-gold.md": {
	id: "nvda-historical-performance-after-cpi-release-1-day-vs-gold.md";
  slug: "nvda-historical-performance-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-cpi-release-1-day-vs-sp500.md": {
	id: "nvda-historical-performance-after-cpi-release-1-day-vs-sp500.md";
  slug: "nvda-historical-performance-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-cpi-release-1-day.md": {
	id: "nvda-historical-performance-after-cpi-release-1-day.md";
  slug: "nvda-historical-performance-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-cpi-release-7-day-vs-gold.md": {
	id: "nvda-historical-performance-after-cpi-release-7-day-vs-gold.md";
  slug: "nvda-historical-performance-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-cpi-release-7-day-vs-sp500.md": {
	id: "nvda-historical-performance-after-cpi-release-7-day-vs-sp500.md";
  slug: "nvda-historical-performance-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-cpi-release-7-day.md": {
	id: "nvda-historical-performance-after-cpi-release-7-day.md";
  slug: "nvda-historical-performance-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "nvda-historical-performance-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "nvda-historical-performance-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "nvda-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "nvda-historical-performance-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-fed-rate-cut-1-day.md": {
	id: "nvda-historical-performance-after-fed-rate-cut-1-day.md";
  slug: "nvda-historical-performance-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "nvda-historical-performance-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "nvda-historical-performance-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "nvda-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "nvda-historical-performance-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-fed-rate-cut-7-day.md": {
	id: "nvda-historical-performance-after-fed-rate-cut-7-day.md";
  slug: "nvda-historical-performance-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-gdp-report-1-day-vs-gold.md": {
	id: "nvda-historical-performance-after-gdp-report-1-day-vs-gold.md";
  slug: "nvda-historical-performance-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-gdp-report-1-day-vs-sp500.md": {
	id: "nvda-historical-performance-after-gdp-report-1-day-vs-sp500.md";
  slug: "nvda-historical-performance-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-gdp-report-1-day.md": {
	id: "nvda-historical-performance-after-gdp-report-1-day.md";
  slug: "nvda-historical-performance-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-gdp-report-7-day-vs-gold.md": {
	id: "nvda-historical-performance-after-gdp-report-7-day-vs-gold.md";
  slug: "nvda-historical-performance-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-gdp-report-7-day-vs-sp500.md": {
	id: "nvda-historical-performance-after-gdp-report-7-day-vs-sp500.md";
  slug: "nvda-historical-performance-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-gdp-report-7-day.md": {
	id: "nvda-historical-performance-after-gdp-report-7-day.md";
  slug: "nvda-historical-performance-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-inflation-rate-1-day-vs-gold.md": {
	id: "nvda-historical-performance-after-inflation-rate-1-day-vs-gold.md";
  slug: "nvda-historical-performance-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-inflation-rate-1-day-vs-sp500.md": {
	id: "nvda-historical-performance-after-inflation-rate-1-day-vs-sp500.md";
  slug: "nvda-historical-performance-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-inflation-rate-1-day.md": {
	id: "nvda-historical-performance-after-inflation-rate-1-day.md";
  slug: "nvda-historical-performance-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-inflation-rate-7-day-vs-gold.md": {
	id: "nvda-historical-performance-after-inflation-rate-7-day-vs-gold.md";
  slug: "nvda-historical-performance-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-inflation-rate-7-day-vs-sp500.md": {
	id: "nvda-historical-performance-after-inflation-rate-7-day-vs-sp500.md";
  slug: "nvda-historical-performance-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-inflation-rate-7-day.md": {
	id: "nvda-historical-performance-after-inflation-rate-7-day.md";
  slug: "nvda-historical-performance-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-nfp-data-1-day-vs-gold.md": {
	id: "nvda-historical-performance-after-nfp-data-1-day-vs-gold.md";
  slug: "nvda-historical-performance-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-nfp-data-1-day-vs-sp500.md": {
	id: "nvda-historical-performance-after-nfp-data-1-day-vs-sp500.md";
  slug: "nvda-historical-performance-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-nfp-data-1-day.md": {
	id: "nvda-historical-performance-after-nfp-data-1-day.md";
  slug: "nvda-historical-performance-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-nfp-data-7-day-vs-gold.md": {
	id: "nvda-historical-performance-after-nfp-data-7-day-vs-gold.md";
  slug: "nvda-historical-performance-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-nfp-data-7-day-vs-sp500.md": {
	id: "nvda-historical-performance-after-nfp-data-7-day-vs-sp500.md";
  slug: "nvda-historical-performance-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-historical-performance-after-nfp-data-7-day.md": {
	id: "nvda-historical-performance-after-nfp-data-7-day.md";
  slug: "nvda-historical-performance-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-cpi-release-1-day-vs-gold.md": {
	id: "nvda-price-impact-after-cpi-release-1-day-vs-gold.md";
  slug: "nvda-price-impact-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-cpi-release-1-day-vs-sp500.md": {
	id: "nvda-price-impact-after-cpi-release-1-day-vs-sp500.md";
  slug: "nvda-price-impact-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-cpi-release-1-day.md": {
	id: "nvda-price-impact-after-cpi-release-1-day.md";
  slug: "nvda-price-impact-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-cpi-release-7-day-vs-gold.md": {
	id: "nvda-price-impact-after-cpi-release-7-day-vs-gold.md";
  slug: "nvda-price-impact-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-cpi-release-7-day-vs-sp500.md": {
	id: "nvda-price-impact-after-cpi-release-7-day-vs-sp500.md";
  slug: "nvda-price-impact-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-cpi-release-7-day.md": {
	id: "nvda-price-impact-after-cpi-release-7-day.md";
  slug: "nvda-price-impact-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "nvda-price-impact-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "nvda-price-impact-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "nvda-price-impact-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "nvda-price-impact-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-fed-rate-cut-1-day.md": {
	id: "nvda-price-impact-after-fed-rate-cut-1-day.md";
  slug: "nvda-price-impact-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "nvda-price-impact-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "nvda-price-impact-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "nvda-price-impact-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "nvda-price-impact-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-fed-rate-cut-7-day.md": {
	id: "nvda-price-impact-after-fed-rate-cut-7-day.md";
  slug: "nvda-price-impact-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-gdp-report-1-day-vs-gold.md": {
	id: "nvda-price-impact-after-gdp-report-1-day-vs-gold.md";
  slug: "nvda-price-impact-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-gdp-report-1-day-vs-sp500.md": {
	id: "nvda-price-impact-after-gdp-report-1-day-vs-sp500.md";
  slug: "nvda-price-impact-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-gdp-report-1-day.md": {
	id: "nvda-price-impact-after-gdp-report-1-day.md";
  slug: "nvda-price-impact-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-gdp-report-7-day-vs-gold.md": {
	id: "nvda-price-impact-after-gdp-report-7-day-vs-gold.md";
  slug: "nvda-price-impact-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-gdp-report-7-day-vs-sp500.md": {
	id: "nvda-price-impact-after-gdp-report-7-day-vs-sp500.md";
  slug: "nvda-price-impact-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-gdp-report-7-day.md": {
	id: "nvda-price-impact-after-gdp-report-7-day.md";
  slug: "nvda-price-impact-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-inflation-rate-1-day-vs-gold.md": {
	id: "nvda-price-impact-after-inflation-rate-1-day-vs-gold.md";
  slug: "nvda-price-impact-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-inflation-rate-1-day-vs-sp500.md": {
	id: "nvda-price-impact-after-inflation-rate-1-day-vs-sp500.md";
  slug: "nvda-price-impact-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-inflation-rate-1-day.md": {
	id: "nvda-price-impact-after-inflation-rate-1-day.md";
  slug: "nvda-price-impact-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-inflation-rate-7-day-vs-gold.md": {
	id: "nvda-price-impact-after-inflation-rate-7-day-vs-gold.md";
  slug: "nvda-price-impact-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-inflation-rate-7-day-vs-sp500.md": {
	id: "nvda-price-impact-after-inflation-rate-7-day-vs-sp500.md";
  slug: "nvda-price-impact-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-inflation-rate-7-day.md": {
	id: "nvda-price-impact-after-inflation-rate-7-day.md";
  slug: "nvda-price-impact-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-nfp-data-1-day-vs-gold.md": {
	id: "nvda-price-impact-after-nfp-data-1-day-vs-gold.md";
  slug: "nvda-price-impact-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-nfp-data-1-day-vs-sp500.md": {
	id: "nvda-price-impact-after-nfp-data-1-day-vs-sp500.md";
  slug: "nvda-price-impact-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-nfp-data-1-day.md": {
	id: "nvda-price-impact-after-nfp-data-1-day.md";
  slug: "nvda-price-impact-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-nfp-data-7-day-vs-gold.md": {
	id: "nvda-price-impact-after-nfp-data-7-day-vs-gold.md";
  slug: "nvda-price-impact-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-nfp-data-7-day-vs-sp500.md": {
	id: "nvda-price-impact-after-nfp-data-7-day-vs-sp500.md";
  slug: "nvda-price-impact-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-price-impact-after-nfp-data-7-day.md": {
	id: "nvda-price-impact-after-nfp-data-7-day.md";
  slug: "nvda-price-impact-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-cpi-release-1-day-vs-gold.md": {
	id: "nvda-volatility-after-cpi-release-1-day-vs-gold.md";
  slug: "nvda-volatility-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-cpi-release-1-day-vs-sp500.md": {
	id: "nvda-volatility-after-cpi-release-1-day-vs-sp500.md";
  slug: "nvda-volatility-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-cpi-release-1-day.md": {
	id: "nvda-volatility-after-cpi-release-1-day.md";
  slug: "nvda-volatility-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-cpi-release-7-day-vs-gold.md": {
	id: "nvda-volatility-after-cpi-release-7-day-vs-gold.md";
  slug: "nvda-volatility-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-cpi-release-7-day-vs-sp500.md": {
	id: "nvda-volatility-after-cpi-release-7-day-vs-sp500.md";
  slug: "nvda-volatility-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-cpi-release-7-day.md": {
	id: "nvda-volatility-after-cpi-release-7-day.md";
  slug: "nvda-volatility-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "nvda-volatility-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "nvda-volatility-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "nvda-volatility-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "nvda-volatility-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-fed-rate-cut-1-day.md": {
	id: "nvda-volatility-after-fed-rate-cut-1-day.md";
  slug: "nvda-volatility-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "nvda-volatility-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "nvda-volatility-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "nvda-volatility-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "nvda-volatility-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-fed-rate-cut-7-day.md": {
	id: "nvda-volatility-after-fed-rate-cut-7-day.md";
  slug: "nvda-volatility-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-gdp-report-1-day-vs-gold.md": {
	id: "nvda-volatility-after-gdp-report-1-day-vs-gold.md";
  slug: "nvda-volatility-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-gdp-report-1-day-vs-sp500.md": {
	id: "nvda-volatility-after-gdp-report-1-day-vs-sp500.md";
  slug: "nvda-volatility-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-gdp-report-1-day.md": {
	id: "nvda-volatility-after-gdp-report-1-day.md";
  slug: "nvda-volatility-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-gdp-report-7-day-vs-gold.md": {
	id: "nvda-volatility-after-gdp-report-7-day-vs-gold.md";
  slug: "nvda-volatility-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-gdp-report-7-day-vs-sp500.md": {
	id: "nvda-volatility-after-gdp-report-7-day-vs-sp500.md";
  slug: "nvda-volatility-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-gdp-report-7-day.md": {
	id: "nvda-volatility-after-gdp-report-7-day.md";
  slug: "nvda-volatility-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-inflation-rate-1-day-vs-gold.md": {
	id: "nvda-volatility-after-inflation-rate-1-day-vs-gold.md";
  slug: "nvda-volatility-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-inflation-rate-1-day-vs-sp500.md": {
	id: "nvda-volatility-after-inflation-rate-1-day-vs-sp500.md";
  slug: "nvda-volatility-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-inflation-rate-1-day.md": {
	id: "nvda-volatility-after-inflation-rate-1-day.md";
  slug: "nvda-volatility-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-inflation-rate-7-day-vs-gold.md": {
	id: "nvda-volatility-after-inflation-rate-7-day-vs-gold.md";
  slug: "nvda-volatility-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-inflation-rate-7-day-vs-sp500.md": {
	id: "nvda-volatility-after-inflation-rate-7-day-vs-sp500.md";
  slug: "nvda-volatility-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-inflation-rate-7-day.md": {
	id: "nvda-volatility-after-inflation-rate-7-day.md";
  slug: "nvda-volatility-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-nfp-data-1-day-vs-gold.md": {
	id: "nvda-volatility-after-nfp-data-1-day-vs-gold.md";
  slug: "nvda-volatility-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-nfp-data-1-day-vs-sp500.md": {
	id: "nvda-volatility-after-nfp-data-1-day-vs-sp500.md";
  slug: "nvda-volatility-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-nfp-data-1-day.md": {
	id: "nvda-volatility-after-nfp-data-1-day.md";
  slug: "nvda-volatility-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-nfp-data-7-day-vs-gold.md": {
	id: "nvda-volatility-after-nfp-data-7-day-vs-gold.md";
  slug: "nvda-volatility-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-nfp-data-7-day-vs-sp500.md": {
	id: "nvda-volatility-after-nfp-data-7-day-vs-sp500.md";
  slug: "nvda-volatility-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"nvda-volatility-after-nfp-data-7-day.md": {
	id: "nvda-volatility-after-nfp-data-7-day.md";
  slug: "nvda-volatility-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-cpi-release-1-day-vs-gold.md": {
	id: "sol-correlation-after-cpi-release-1-day-vs-gold.md";
  slug: "sol-correlation-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-cpi-release-1-day-vs-sp500.md": {
	id: "sol-correlation-after-cpi-release-1-day-vs-sp500.md";
  slug: "sol-correlation-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-cpi-release-1-day.md": {
	id: "sol-correlation-after-cpi-release-1-day.md";
  slug: "sol-correlation-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-cpi-release-7-day-vs-gold.md": {
	id: "sol-correlation-after-cpi-release-7-day-vs-gold.md";
  slug: "sol-correlation-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-cpi-release-7-day-vs-sp500.md": {
	id: "sol-correlation-after-cpi-release-7-day-vs-sp500.md";
  slug: "sol-correlation-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-cpi-release-7-day.md": {
	id: "sol-correlation-after-cpi-release-7-day.md";
  slug: "sol-correlation-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "sol-correlation-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "sol-correlation-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "sol-correlation-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "sol-correlation-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-fed-rate-cut-1-day.md": {
	id: "sol-correlation-after-fed-rate-cut-1-day.md";
  slug: "sol-correlation-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "sol-correlation-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "sol-correlation-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "sol-correlation-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "sol-correlation-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-fed-rate-cut-7-day.md": {
	id: "sol-correlation-after-fed-rate-cut-7-day.md";
  slug: "sol-correlation-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-gdp-report-1-day-vs-gold.md": {
	id: "sol-correlation-after-gdp-report-1-day-vs-gold.md";
  slug: "sol-correlation-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-gdp-report-1-day-vs-sp500.md": {
	id: "sol-correlation-after-gdp-report-1-day-vs-sp500.md";
  slug: "sol-correlation-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-gdp-report-1-day.md": {
	id: "sol-correlation-after-gdp-report-1-day.md";
  slug: "sol-correlation-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-gdp-report-7-day-vs-gold.md": {
	id: "sol-correlation-after-gdp-report-7-day-vs-gold.md";
  slug: "sol-correlation-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-gdp-report-7-day-vs-sp500.md": {
	id: "sol-correlation-after-gdp-report-7-day-vs-sp500.md";
  slug: "sol-correlation-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-gdp-report-7-day.md": {
	id: "sol-correlation-after-gdp-report-7-day.md";
  slug: "sol-correlation-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-inflation-rate-1-day-vs-gold.md": {
	id: "sol-correlation-after-inflation-rate-1-day-vs-gold.md";
  slug: "sol-correlation-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-inflation-rate-1-day-vs-sp500.md": {
	id: "sol-correlation-after-inflation-rate-1-day-vs-sp500.md";
  slug: "sol-correlation-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-inflation-rate-1-day.md": {
	id: "sol-correlation-after-inflation-rate-1-day.md";
  slug: "sol-correlation-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-inflation-rate-7-day-vs-gold.md": {
	id: "sol-correlation-after-inflation-rate-7-day-vs-gold.md";
  slug: "sol-correlation-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-inflation-rate-7-day-vs-sp500.md": {
	id: "sol-correlation-after-inflation-rate-7-day-vs-sp500.md";
  slug: "sol-correlation-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-inflation-rate-7-day.md": {
	id: "sol-correlation-after-inflation-rate-7-day.md";
  slug: "sol-correlation-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-nfp-data-1-day-vs-gold.md": {
	id: "sol-correlation-after-nfp-data-1-day-vs-gold.md";
  slug: "sol-correlation-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-nfp-data-1-day-vs-sp500.md": {
	id: "sol-correlation-after-nfp-data-1-day-vs-sp500.md";
  slug: "sol-correlation-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-nfp-data-1-day.md": {
	id: "sol-correlation-after-nfp-data-1-day.md";
  slug: "sol-correlation-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-nfp-data-7-day-vs-gold.md": {
	id: "sol-correlation-after-nfp-data-7-day-vs-gold.md";
  slug: "sol-correlation-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-nfp-data-7-day-vs-sp500.md": {
	id: "sol-correlation-after-nfp-data-7-day-vs-sp500.md";
  slug: "sol-correlation-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-correlation-after-nfp-data-7-day.md": {
	id: "sol-correlation-after-nfp-data-7-day.md";
  slug: "sol-correlation-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-cpi-release-1-day-vs-gold.md": {
	id: "sol-historical-performance-after-cpi-release-1-day-vs-gold.md";
  slug: "sol-historical-performance-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-cpi-release-1-day-vs-sp500.md": {
	id: "sol-historical-performance-after-cpi-release-1-day-vs-sp500.md";
  slug: "sol-historical-performance-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-cpi-release-1-day.md": {
	id: "sol-historical-performance-after-cpi-release-1-day.md";
  slug: "sol-historical-performance-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-cpi-release-7-day-vs-gold.md": {
	id: "sol-historical-performance-after-cpi-release-7-day-vs-gold.md";
  slug: "sol-historical-performance-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-cpi-release-7-day-vs-sp500.md": {
	id: "sol-historical-performance-after-cpi-release-7-day-vs-sp500.md";
  slug: "sol-historical-performance-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-cpi-release-7-day.md": {
	id: "sol-historical-performance-after-cpi-release-7-day.md";
  slug: "sol-historical-performance-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "sol-historical-performance-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "sol-historical-performance-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "sol-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "sol-historical-performance-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-fed-rate-cut-1-day.md": {
	id: "sol-historical-performance-after-fed-rate-cut-1-day.md";
  slug: "sol-historical-performance-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "sol-historical-performance-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "sol-historical-performance-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "sol-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "sol-historical-performance-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-fed-rate-cut-7-day.md": {
	id: "sol-historical-performance-after-fed-rate-cut-7-day.md";
  slug: "sol-historical-performance-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-gdp-report-1-day-vs-gold.md": {
	id: "sol-historical-performance-after-gdp-report-1-day-vs-gold.md";
  slug: "sol-historical-performance-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-gdp-report-1-day-vs-sp500.md": {
	id: "sol-historical-performance-after-gdp-report-1-day-vs-sp500.md";
  slug: "sol-historical-performance-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-gdp-report-1-day.md": {
	id: "sol-historical-performance-after-gdp-report-1-day.md";
  slug: "sol-historical-performance-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-gdp-report-7-day-vs-gold.md": {
	id: "sol-historical-performance-after-gdp-report-7-day-vs-gold.md";
  slug: "sol-historical-performance-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-gdp-report-7-day-vs-sp500.md": {
	id: "sol-historical-performance-after-gdp-report-7-day-vs-sp500.md";
  slug: "sol-historical-performance-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-gdp-report-7-day.md": {
	id: "sol-historical-performance-after-gdp-report-7-day.md";
  slug: "sol-historical-performance-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-inflation-rate-1-day-vs-gold.md": {
	id: "sol-historical-performance-after-inflation-rate-1-day-vs-gold.md";
  slug: "sol-historical-performance-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-inflation-rate-1-day-vs-sp500.md": {
	id: "sol-historical-performance-after-inflation-rate-1-day-vs-sp500.md";
  slug: "sol-historical-performance-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-inflation-rate-1-day.md": {
	id: "sol-historical-performance-after-inflation-rate-1-day.md";
  slug: "sol-historical-performance-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-inflation-rate-7-day-vs-gold.md": {
	id: "sol-historical-performance-after-inflation-rate-7-day-vs-gold.md";
  slug: "sol-historical-performance-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-inflation-rate-7-day-vs-sp500.md": {
	id: "sol-historical-performance-after-inflation-rate-7-day-vs-sp500.md";
  slug: "sol-historical-performance-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-inflation-rate-7-day.md": {
	id: "sol-historical-performance-after-inflation-rate-7-day.md";
  slug: "sol-historical-performance-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-nfp-data-1-day-vs-gold.md": {
	id: "sol-historical-performance-after-nfp-data-1-day-vs-gold.md";
  slug: "sol-historical-performance-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-nfp-data-1-day-vs-sp500.md": {
	id: "sol-historical-performance-after-nfp-data-1-day-vs-sp500.md";
  slug: "sol-historical-performance-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-nfp-data-1-day.md": {
	id: "sol-historical-performance-after-nfp-data-1-day.md";
  slug: "sol-historical-performance-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-nfp-data-7-day-vs-gold.md": {
	id: "sol-historical-performance-after-nfp-data-7-day-vs-gold.md";
  slug: "sol-historical-performance-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-nfp-data-7-day-vs-sp500.md": {
	id: "sol-historical-performance-after-nfp-data-7-day-vs-sp500.md";
  slug: "sol-historical-performance-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-historical-performance-after-nfp-data-7-day.md": {
	id: "sol-historical-performance-after-nfp-data-7-day.md";
  slug: "sol-historical-performance-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-cpi-release-1-day-vs-gold.md": {
	id: "sol-price-impact-after-cpi-release-1-day-vs-gold.md";
  slug: "sol-price-impact-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-cpi-release-1-day-vs-sp500.md": {
	id: "sol-price-impact-after-cpi-release-1-day-vs-sp500.md";
  slug: "sol-price-impact-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-cpi-release-1-day.md": {
	id: "sol-price-impact-after-cpi-release-1-day.md";
  slug: "sol-price-impact-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-cpi-release-7-day-vs-gold.md": {
	id: "sol-price-impact-after-cpi-release-7-day-vs-gold.md";
  slug: "sol-price-impact-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-cpi-release-7-day-vs-sp500.md": {
	id: "sol-price-impact-after-cpi-release-7-day-vs-sp500.md";
  slug: "sol-price-impact-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-cpi-release-7-day.md": {
	id: "sol-price-impact-after-cpi-release-7-day.md";
  slug: "sol-price-impact-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "sol-price-impact-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "sol-price-impact-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "sol-price-impact-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "sol-price-impact-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-fed-rate-cut-1-day.md": {
	id: "sol-price-impact-after-fed-rate-cut-1-day.md";
  slug: "sol-price-impact-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "sol-price-impact-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "sol-price-impact-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "sol-price-impact-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "sol-price-impact-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-fed-rate-cut-7-day.md": {
	id: "sol-price-impact-after-fed-rate-cut-7-day.md";
  slug: "sol-price-impact-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-gdp-report-1-day-vs-gold.md": {
	id: "sol-price-impact-after-gdp-report-1-day-vs-gold.md";
  slug: "sol-price-impact-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-gdp-report-1-day-vs-sp500.md": {
	id: "sol-price-impact-after-gdp-report-1-day-vs-sp500.md";
  slug: "sol-price-impact-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-gdp-report-1-day.md": {
	id: "sol-price-impact-after-gdp-report-1-day.md";
  slug: "sol-price-impact-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-gdp-report-7-day-vs-gold.md": {
	id: "sol-price-impact-after-gdp-report-7-day-vs-gold.md";
  slug: "sol-price-impact-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-gdp-report-7-day-vs-sp500.md": {
	id: "sol-price-impact-after-gdp-report-7-day-vs-sp500.md";
  slug: "sol-price-impact-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-gdp-report-7-day.md": {
	id: "sol-price-impact-after-gdp-report-7-day.md";
  slug: "sol-price-impact-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-inflation-rate-1-day-vs-gold.md": {
	id: "sol-price-impact-after-inflation-rate-1-day-vs-gold.md";
  slug: "sol-price-impact-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-inflation-rate-1-day-vs-sp500.md": {
	id: "sol-price-impact-after-inflation-rate-1-day-vs-sp500.md";
  slug: "sol-price-impact-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-inflation-rate-1-day.md": {
	id: "sol-price-impact-after-inflation-rate-1-day.md";
  slug: "sol-price-impact-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-inflation-rate-7-day-vs-gold.md": {
	id: "sol-price-impact-after-inflation-rate-7-day-vs-gold.md";
  slug: "sol-price-impact-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-inflation-rate-7-day-vs-sp500.md": {
	id: "sol-price-impact-after-inflation-rate-7-day-vs-sp500.md";
  slug: "sol-price-impact-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-inflation-rate-7-day.md": {
	id: "sol-price-impact-after-inflation-rate-7-day.md";
  slug: "sol-price-impact-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-nfp-data-1-day-vs-gold.md": {
	id: "sol-price-impact-after-nfp-data-1-day-vs-gold.md";
  slug: "sol-price-impact-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-nfp-data-1-day-vs-sp500.md": {
	id: "sol-price-impact-after-nfp-data-1-day-vs-sp500.md";
  slug: "sol-price-impact-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-nfp-data-1-day.md": {
	id: "sol-price-impact-after-nfp-data-1-day.md";
  slug: "sol-price-impact-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-nfp-data-7-day-vs-gold.md": {
	id: "sol-price-impact-after-nfp-data-7-day-vs-gold.md";
  slug: "sol-price-impact-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-nfp-data-7-day-vs-sp500.md": {
	id: "sol-price-impact-after-nfp-data-7-day-vs-sp500.md";
  slug: "sol-price-impact-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-price-impact-after-nfp-data-7-day.md": {
	id: "sol-price-impact-after-nfp-data-7-day.md";
  slug: "sol-price-impact-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-cpi-release-1-day-vs-gold.md": {
	id: "sol-volatility-after-cpi-release-1-day-vs-gold.md";
  slug: "sol-volatility-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-cpi-release-1-day-vs-sp500.md": {
	id: "sol-volatility-after-cpi-release-1-day-vs-sp500.md";
  slug: "sol-volatility-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-cpi-release-1-day.md": {
	id: "sol-volatility-after-cpi-release-1-day.md";
  slug: "sol-volatility-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-cpi-release-7-day-vs-gold.md": {
	id: "sol-volatility-after-cpi-release-7-day-vs-gold.md";
  slug: "sol-volatility-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-cpi-release-7-day-vs-sp500.md": {
	id: "sol-volatility-after-cpi-release-7-day-vs-sp500.md";
  slug: "sol-volatility-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-cpi-release-7-day.md": {
	id: "sol-volatility-after-cpi-release-7-day.md";
  slug: "sol-volatility-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "sol-volatility-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "sol-volatility-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "sol-volatility-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "sol-volatility-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-fed-rate-cut-1-day.md": {
	id: "sol-volatility-after-fed-rate-cut-1-day.md";
  slug: "sol-volatility-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "sol-volatility-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "sol-volatility-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "sol-volatility-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "sol-volatility-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-fed-rate-cut-7-day.md": {
	id: "sol-volatility-after-fed-rate-cut-7-day.md";
  slug: "sol-volatility-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-gdp-report-1-day-vs-gold.md": {
	id: "sol-volatility-after-gdp-report-1-day-vs-gold.md";
  slug: "sol-volatility-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-gdp-report-1-day-vs-sp500.md": {
	id: "sol-volatility-after-gdp-report-1-day-vs-sp500.md";
  slug: "sol-volatility-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-gdp-report-1-day.md": {
	id: "sol-volatility-after-gdp-report-1-day.md";
  slug: "sol-volatility-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-gdp-report-7-day-vs-gold.md": {
	id: "sol-volatility-after-gdp-report-7-day-vs-gold.md";
  slug: "sol-volatility-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-gdp-report-7-day-vs-sp500.md": {
	id: "sol-volatility-after-gdp-report-7-day-vs-sp500.md";
  slug: "sol-volatility-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-gdp-report-7-day.md": {
	id: "sol-volatility-after-gdp-report-7-day.md";
  slug: "sol-volatility-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-inflation-rate-1-day-vs-gold.md": {
	id: "sol-volatility-after-inflation-rate-1-day-vs-gold.md";
  slug: "sol-volatility-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-inflation-rate-1-day-vs-sp500.md": {
	id: "sol-volatility-after-inflation-rate-1-day-vs-sp500.md";
  slug: "sol-volatility-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-inflation-rate-1-day.md": {
	id: "sol-volatility-after-inflation-rate-1-day.md";
  slug: "sol-volatility-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-inflation-rate-7-day-vs-gold.md": {
	id: "sol-volatility-after-inflation-rate-7-day-vs-gold.md";
  slug: "sol-volatility-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-inflation-rate-7-day-vs-sp500.md": {
	id: "sol-volatility-after-inflation-rate-7-day-vs-sp500.md";
  slug: "sol-volatility-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-inflation-rate-7-day.md": {
	id: "sol-volatility-after-inflation-rate-7-day.md";
  slug: "sol-volatility-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-nfp-data-1-day-vs-gold.md": {
	id: "sol-volatility-after-nfp-data-1-day-vs-gold.md";
  slug: "sol-volatility-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-nfp-data-1-day-vs-sp500.md": {
	id: "sol-volatility-after-nfp-data-1-day-vs-sp500.md";
  slug: "sol-volatility-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-nfp-data-1-day.md": {
	id: "sol-volatility-after-nfp-data-1-day.md";
  slug: "sol-volatility-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-nfp-data-7-day-vs-gold.md": {
	id: "sol-volatility-after-nfp-data-7-day-vs-gold.md";
  slug: "sol-volatility-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-nfp-data-7-day-vs-sp500.md": {
	id: "sol-volatility-after-nfp-data-7-day-vs-sp500.md";
  slug: "sol-volatility-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"sol-volatility-after-nfp-data-7-day.md": {
	id: "sol-volatility-after-nfp-data-7-day.md";
  slug: "sol-volatility-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-cpi-release-1-day-vs-gold.md": {
	id: "spy-correlation-after-cpi-release-1-day-vs-gold.md";
  slug: "spy-correlation-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-cpi-release-1-day-vs-sp500.md": {
	id: "spy-correlation-after-cpi-release-1-day-vs-sp500.md";
  slug: "spy-correlation-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-cpi-release-1-day.md": {
	id: "spy-correlation-after-cpi-release-1-day.md";
  slug: "spy-correlation-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-cpi-release-7-day-vs-gold.md": {
	id: "spy-correlation-after-cpi-release-7-day-vs-gold.md";
  slug: "spy-correlation-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-cpi-release-7-day-vs-sp500.md": {
	id: "spy-correlation-after-cpi-release-7-day-vs-sp500.md";
  slug: "spy-correlation-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-cpi-release-7-day.md": {
	id: "spy-correlation-after-cpi-release-7-day.md";
  slug: "spy-correlation-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "spy-correlation-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "spy-correlation-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "spy-correlation-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "spy-correlation-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-fed-rate-cut-1-day.md": {
	id: "spy-correlation-after-fed-rate-cut-1-day.md";
  slug: "spy-correlation-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "spy-correlation-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "spy-correlation-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "spy-correlation-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "spy-correlation-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-fed-rate-cut-7-day.md": {
	id: "spy-correlation-after-fed-rate-cut-7-day.md";
  slug: "spy-correlation-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-gdp-report-1-day-vs-gold.md": {
	id: "spy-correlation-after-gdp-report-1-day-vs-gold.md";
  slug: "spy-correlation-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-gdp-report-1-day-vs-sp500.md": {
	id: "spy-correlation-after-gdp-report-1-day-vs-sp500.md";
  slug: "spy-correlation-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-gdp-report-1-day.md": {
	id: "spy-correlation-after-gdp-report-1-day.md";
  slug: "spy-correlation-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-gdp-report-7-day-vs-gold.md": {
	id: "spy-correlation-after-gdp-report-7-day-vs-gold.md";
  slug: "spy-correlation-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-gdp-report-7-day-vs-sp500.md": {
	id: "spy-correlation-after-gdp-report-7-day-vs-sp500.md";
  slug: "spy-correlation-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-gdp-report-7-day.md": {
	id: "spy-correlation-after-gdp-report-7-day.md";
  slug: "spy-correlation-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-inflation-rate-1-day-vs-gold.md": {
	id: "spy-correlation-after-inflation-rate-1-day-vs-gold.md";
  slug: "spy-correlation-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-inflation-rate-1-day-vs-sp500.md": {
	id: "spy-correlation-after-inflation-rate-1-day-vs-sp500.md";
  slug: "spy-correlation-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-inflation-rate-1-day.md": {
	id: "spy-correlation-after-inflation-rate-1-day.md";
  slug: "spy-correlation-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-inflation-rate-7-day-vs-gold.md": {
	id: "spy-correlation-after-inflation-rate-7-day-vs-gold.md";
  slug: "spy-correlation-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-inflation-rate-7-day-vs-sp500.md": {
	id: "spy-correlation-after-inflation-rate-7-day-vs-sp500.md";
  slug: "spy-correlation-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-inflation-rate-7-day.md": {
	id: "spy-correlation-after-inflation-rate-7-day.md";
  slug: "spy-correlation-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-nfp-data-1-day-vs-gold.md": {
	id: "spy-correlation-after-nfp-data-1-day-vs-gold.md";
  slug: "spy-correlation-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-nfp-data-1-day-vs-sp500.md": {
	id: "spy-correlation-after-nfp-data-1-day-vs-sp500.md";
  slug: "spy-correlation-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-nfp-data-1-day.md": {
	id: "spy-correlation-after-nfp-data-1-day.md";
  slug: "spy-correlation-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-nfp-data-7-day-vs-gold.md": {
	id: "spy-correlation-after-nfp-data-7-day-vs-gold.md";
  slug: "spy-correlation-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-nfp-data-7-day-vs-sp500.md": {
	id: "spy-correlation-after-nfp-data-7-day-vs-sp500.md";
  slug: "spy-correlation-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-correlation-after-nfp-data-7-day.md": {
	id: "spy-correlation-after-nfp-data-7-day.md";
  slug: "spy-correlation-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-cpi-release-1-day-vs-gold.md": {
	id: "spy-historical-performance-after-cpi-release-1-day-vs-gold.md";
  slug: "spy-historical-performance-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-cpi-release-1-day-vs-sp500.md": {
	id: "spy-historical-performance-after-cpi-release-1-day-vs-sp500.md";
  slug: "spy-historical-performance-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-cpi-release-1-day.md": {
	id: "spy-historical-performance-after-cpi-release-1-day.md";
  slug: "spy-historical-performance-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-cpi-release-7-day-vs-gold.md": {
	id: "spy-historical-performance-after-cpi-release-7-day-vs-gold.md";
  slug: "spy-historical-performance-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-cpi-release-7-day-vs-sp500.md": {
	id: "spy-historical-performance-after-cpi-release-7-day-vs-sp500.md";
  slug: "spy-historical-performance-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-cpi-release-7-day.md": {
	id: "spy-historical-performance-after-cpi-release-7-day.md";
  slug: "spy-historical-performance-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "spy-historical-performance-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "spy-historical-performance-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "spy-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "spy-historical-performance-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-fed-rate-cut-1-day.md": {
	id: "spy-historical-performance-after-fed-rate-cut-1-day.md";
  slug: "spy-historical-performance-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "spy-historical-performance-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "spy-historical-performance-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "spy-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "spy-historical-performance-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-fed-rate-cut-7-day.md": {
	id: "spy-historical-performance-after-fed-rate-cut-7-day.md";
  slug: "spy-historical-performance-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-gdp-report-1-day-vs-gold.md": {
	id: "spy-historical-performance-after-gdp-report-1-day-vs-gold.md";
  slug: "spy-historical-performance-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-gdp-report-1-day-vs-sp500.md": {
	id: "spy-historical-performance-after-gdp-report-1-day-vs-sp500.md";
  slug: "spy-historical-performance-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-gdp-report-1-day.md": {
	id: "spy-historical-performance-after-gdp-report-1-day.md";
  slug: "spy-historical-performance-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-gdp-report-7-day-vs-gold.md": {
	id: "spy-historical-performance-after-gdp-report-7-day-vs-gold.md";
  slug: "spy-historical-performance-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-gdp-report-7-day-vs-sp500.md": {
	id: "spy-historical-performance-after-gdp-report-7-day-vs-sp500.md";
  slug: "spy-historical-performance-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-gdp-report-7-day.md": {
	id: "spy-historical-performance-after-gdp-report-7-day.md";
  slug: "spy-historical-performance-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-inflation-rate-1-day-vs-gold.md": {
	id: "spy-historical-performance-after-inflation-rate-1-day-vs-gold.md";
  slug: "spy-historical-performance-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-inflation-rate-1-day-vs-sp500.md": {
	id: "spy-historical-performance-after-inflation-rate-1-day-vs-sp500.md";
  slug: "spy-historical-performance-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-inflation-rate-1-day.md": {
	id: "spy-historical-performance-after-inflation-rate-1-day.md";
  slug: "spy-historical-performance-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-inflation-rate-7-day-vs-gold.md": {
	id: "spy-historical-performance-after-inflation-rate-7-day-vs-gold.md";
  slug: "spy-historical-performance-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-inflation-rate-7-day-vs-sp500.md": {
	id: "spy-historical-performance-after-inflation-rate-7-day-vs-sp500.md";
  slug: "spy-historical-performance-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-inflation-rate-7-day.md": {
	id: "spy-historical-performance-after-inflation-rate-7-day.md";
  slug: "spy-historical-performance-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-nfp-data-1-day-vs-gold.md": {
	id: "spy-historical-performance-after-nfp-data-1-day-vs-gold.md";
  slug: "spy-historical-performance-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-nfp-data-1-day-vs-sp500.md": {
	id: "spy-historical-performance-after-nfp-data-1-day-vs-sp500.md";
  slug: "spy-historical-performance-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-nfp-data-1-day.md": {
	id: "spy-historical-performance-after-nfp-data-1-day.md";
  slug: "spy-historical-performance-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-nfp-data-7-day-vs-gold.md": {
	id: "spy-historical-performance-after-nfp-data-7-day-vs-gold.md";
  slug: "spy-historical-performance-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-nfp-data-7-day-vs-sp500.md": {
	id: "spy-historical-performance-after-nfp-data-7-day-vs-sp500.md";
  slug: "spy-historical-performance-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-historical-performance-after-nfp-data-7-day.md": {
	id: "spy-historical-performance-after-nfp-data-7-day.md";
  slug: "spy-historical-performance-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-cpi-release-1-day-vs-gold.md": {
	id: "spy-price-impact-after-cpi-release-1-day-vs-gold.md";
  slug: "spy-price-impact-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-cpi-release-1-day-vs-sp500.md": {
	id: "spy-price-impact-after-cpi-release-1-day-vs-sp500.md";
  slug: "spy-price-impact-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-cpi-release-1-day.md": {
	id: "spy-price-impact-after-cpi-release-1-day.md";
  slug: "spy-price-impact-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-cpi-release-7-day-vs-gold.md": {
	id: "spy-price-impact-after-cpi-release-7-day-vs-gold.md";
  slug: "spy-price-impact-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-cpi-release-7-day-vs-sp500.md": {
	id: "spy-price-impact-after-cpi-release-7-day-vs-sp500.md";
  slug: "spy-price-impact-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-cpi-release-7-day.md": {
	id: "spy-price-impact-after-cpi-release-7-day.md";
  slug: "spy-price-impact-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "spy-price-impact-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "spy-price-impact-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "spy-price-impact-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "spy-price-impact-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-fed-rate-cut-1-day.md": {
	id: "spy-price-impact-after-fed-rate-cut-1-day.md";
  slug: "spy-price-impact-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "spy-price-impact-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "spy-price-impact-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "spy-price-impact-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "spy-price-impact-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-fed-rate-cut-7-day.md": {
	id: "spy-price-impact-after-fed-rate-cut-7-day.md";
  slug: "spy-price-impact-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-gdp-report-1-day-vs-gold.md": {
	id: "spy-price-impact-after-gdp-report-1-day-vs-gold.md";
  slug: "spy-price-impact-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-gdp-report-1-day-vs-sp500.md": {
	id: "spy-price-impact-after-gdp-report-1-day-vs-sp500.md";
  slug: "spy-price-impact-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-gdp-report-1-day.md": {
	id: "spy-price-impact-after-gdp-report-1-day.md";
  slug: "spy-price-impact-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-gdp-report-7-day-vs-gold.md": {
	id: "spy-price-impact-after-gdp-report-7-day-vs-gold.md";
  slug: "spy-price-impact-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-gdp-report-7-day-vs-sp500.md": {
	id: "spy-price-impact-after-gdp-report-7-day-vs-sp500.md";
  slug: "spy-price-impact-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-gdp-report-7-day.md": {
	id: "spy-price-impact-after-gdp-report-7-day.md";
  slug: "spy-price-impact-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-inflation-rate-1-day-vs-gold.md": {
	id: "spy-price-impact-after-inflation-rate-1-day-vs-gold.md";
  slug: "spy-price-impact-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-inflation-rate-1-day-vs-sp500.md": {
	id: "spy-price-impact-after-inflation-rate-1-day-vs-sp500.md";
  slug: "spy-price-impact-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-inflation-rate-1-day.md": {
	id: "spy-price-impact-after-inflation-rate-1-day.md";
  slug: "spy-price-impact-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-inflation-rate-7-day-vs-gold.md": {
	id: "spy-price-impact-after-inflation-rate-7-day-vs-gold.md";
  slug: "spy-price-impact-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-inflation-rate-7-day-vs-sp500.md": {
	id: "spy-price-impact-after-inflation-rate-7-day-vs-sp500.md";
  slug: "spy-price-impact-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-inflation-rate-7-day.md": {
	id: "spy-price-impact-after-inflation-rate-7-day.md";
  slug: "spy-price-impact-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-nfp-data-1-day-vs-gold.md": {
	id: "spy-price-impact-after-nfp-data-1-day-vs-gold.md";
  slug: "spy-price-impact-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-nfp-data-1-day-vs-sp500.md": {
	id: "spy-price-impact-after-nfp-data-1-day-vs-sp500.md";
  slug: "spy-price-impact-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-nfp-data-1-day.md": {
	id: "spy-price-impact-after-nfp-data-1-day.md";
  slug: "spy-price-impact-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-nfp-data-7-day-vs-gold.md": {
	id: "spy-price-impact-after-nfp-data-7-day-vs-gold.md";
  slug: "spy-price-impact-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-nfp-data-7-day-vs-sp500.md": {
	id: "spy-price-impact-after-nfp-data-7-day-vs-sp500.md";
  slug: "spy-price-impact-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-price-impact-after-nfp-data-7-day.md": {
	id: "spy-price-impact-after-nfp-data-7-day.md";
  slug: "spy-price-impact-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-cpi-release-1-day-vs-gold.md": {
	id: "spy-volatility-after-cpi-release-1-day-vs-gold.md";
  slug: "spy-volatility-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-cpi-release-1-day-vs-sp500.md": {
	id: "spy-volatility-after-cpi-release-1-day-vs-sp500.md";
  slug: "spy-volatility-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-cpi-release-1-day.md": {
	id: "spy-volatility-after-cpi-release-1-day.md";
  slug: "spy-volatility-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-cpi-release-7-day-vs-gold.md": {
	id: "spy-volatility-after-cpi-release-7-day-vs-gold.md";
  slug: "spy-volatility-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-cpi-release-7-day-vs-sp500.md": {
	id: "spy-volatility-after-cpi-release-7-day-vs-sp500.md";
  slug: "spy-volatility-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-cpi-release-7-day.md": {
	id: "spy-volatility-after-cpi-release-7-day.md";
  slug: "spy-volatility-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "spy-volatility-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "spy-volatility-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "spy-volatility-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "spy-volatility-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-fed-rate-cut-1-day.md": {
	id: "spy-volatility-after-fed-rate-cut-1-day.md";
  slug: "spy-volatility-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "spy-volatility-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "spy-volatility-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "spy-volatility-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "spy-volatility-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-fed-rate-cut-7-day.md": {
	id: "spy-volatility-after-fed-rate-cut-7-day.md";
  slug: "spy-volatility-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-gdp-report-1-day-vs-gold.md": {
	id: "spy-volatility-after-gdp-report-1-day-vs-gold.md";
  slug: "spy-volatility-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-gdp-report-1-day-vs-sp500.md": {
	id: "spy-volatility-after-gdp-report-1-day-vs-sp500.md";
  slug: "spy-volatility-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-gdp-report-1-day.md": {
	id: "spy-volatility-after-gdp-report-1-day.md";
  slug: "spy-volatility-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-gdp-report-7-day-vs-gold.md": {
	id: "spy-volatility-after-gdp-report-7-day-vs-gold.md";
  slug: "spy-volatility-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-gdp-report-7-day-vs-sp500.md": {
	id: "spy-volatility-after-gdp-report-7-day-vs-sp500.md";
  slug: "spy-volatility-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-gdp-report-7-day.md": {
	id: "spy-volatility-after-gdp-report-7-day.md";
  slug: "spy-volatility-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-inflation-rate-1-day-vs-gold.md": {
	id: "spy-volatility-after-inflation-rate-1-day-vs-gold.md";
  slug: "spy-volatility-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-inflation-rate-1-day-vs-sp500.md": {
	id: "spy-volatility-after-inflation-rate-1-day-vs-sp500.md";
  slug: "spy-volatility-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-inflation-rate-1-day.md": {
	id: "spy-volatility-after-inflation-rate-1-day.md";
  slug: "spy-volatility-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-inflation-rate-7-day-vs-gold.md": {
	id: "spy-volatility-after-inflation-rate-7-day-vs-gold.md";
  slug: "spy-volatility-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-inflation-rate-7-day-vs-sp500.md": {
	id: "spy-volatility-after-inflation-rate-7-day-vs-sp500.md";
  slug: "spy-volatility-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-inflation-rate-7-day.md": {
	id: "spy-volatility-after-inflation-rate-7-day.md";
  slug: "spy-volatility-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-nfp-data-1-day-vs-gold.md": {
	id: "spy-volatility-after-nfp-data-1-day-vs-gold.md";
  slug: "spy-volatility-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-nfp-data-1-day-vs-sp500.md": {
	id: "spy-volatility-after-nfp-data-1-day-vs-sp500.md";
  slug: "spy-volatility-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-nfp-data-1-day.md": {
	id: "spy-volatility-after-nfp-data-1-day.md";
  slug: "spy-volatility-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-nfp-data-7-day-vs-gold.md": {
	id: "spy-volatility-after-nfp-data-7-day-vs-gold.md";
  slug: "spy-volatility-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-nfp-data-7-day-vs-sp500.md": {
	id: "spy-volatility-after-nfp-data-7-day-vs-sp500.md";
  slug: "spy-volatility-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-volatility-after-nfp-data-7-day.md": {
	id: "spy-volatility-after-nfp-data-7-day.md";
  slug: "spy-volatility-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-cpi-release-1-day-vs-gold.md": {
	id: "tsla-correlation-after-cpi-release-1-day-vs-gold.md";
  slug: "tsla-correlation-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-cpi-release-1-day-vs-sp500.md": {
	id: "tsla-correlation-after-cpi-release-1-day-vs-sp500.md";
  slug: "tsla-correlation-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-cpi-release-1-day.md": {
	id: "tsla-correlation-after-cpi-release-1-day.md";
  slug: "tsla-correlation-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-cpi-release-7-day-vs-gold.md": {
	id: "tsla-correlation-after-cpi-release-7-day-vs-gold.md";
  slug: "tsla-correlation-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-cpi-release-7-day-vs-sp500.md": {
	id: "tsla-correlation-after-cpi-release-7-day-vs-sp500.md";
  slug: "tsla-correlation-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-cpi-release-7-day.md": {
	id: "tsla-correlation-after-cpi-release-7-day.md";
  slug: "tsla-correlation-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "tsla-correlation-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "tsla-correlation-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "tsla-correlation-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "tsla-correlation-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-fed-rate-cut-1-day.md": {
	id: "tsla-correlation-after-fed-rate-cut-1-day.md";
  slug: "tsla-correlation-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "tsla-correlation-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "tsla-correlation-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "tsla-correlation-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "tsla-correlation-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-fed-rate-cut-7-day.md": {
	id: "tsla-correlation-after-fed-rate-cut-7-day.md";
  slug: "tsla-correlation-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-gdp-report-1-day-vs-gold.md": {
	id: "tsla-correlation-after-gdp-report-1-day-vs-gold.md";
  slug: "tsla-correlation-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-gdp-report-1-day-vs-sp500.md": {
	id: "tsla-correlation-after-gdp-report-1-day-vs-sp500.md";
  slug: "tsla-correlation-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-gdp-report-1-day.md": {
	id: "tsla-correlation-after-gdp-report-1-day.md";
  slug: "tsla-correlation-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-gdp-report-7-day-vs-gold.md": {
	id: "tsla-correlation-after-gdp-report-7-day-vs-gold.md";
  slug: "tsla-correlation-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-gdp-report-7-day-vs-sp500.md": {
	id: "tsla-correlation-after-gdp-report-7-day-vs-sp500.md";
  slug: "tsla-correlation-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-gdp-report-7-day.md": {
	id: "tsla-correlation-after-gdp-report-7-day.md";
  slug: "tsla-correlation-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-inflation-rate-1-day-vs-gold.md": {
	id: "tsla-correlation-after-inflation-rate-1-day-vs-gold.md";
  slug: "tsla-correlation-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-inflation-rate-1-day-vs-sp500.md": {
	id: "tsla-correlation-after-inflation-rate-1-day-vs-sp500.md";
  slug: "tsla-correlation-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-inflation-rate-1-day.md": {
	id: "tsla-correlation-after-inflation-rate-1-day.md";
  slug: "tsla-correlation-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-inflation-rate-7-day-vs-gold.md": {
	id: "tsla-correlation-after-inflation-rate-7-day-vs-gold.md";
  slug: "tsla-correlation-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-inflation-rate-7-day-vs-sp500.md": {
	id: "tsla-correlation-after-inflation-rate-7-day-vs-sp500.md";
  slug: "tsla-correlation-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-inflation-rate-7-day.md": {
	id: "tsla-correlation-after-inflation-rate-7-day.md";
  slug: "tsla-correlation-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-nfp-data-1-day-vs-gold.md": {
	id: "tsla-correlation-after-nfp-data-1-day-vs-gold.md";
  slug: "tsla-correlation-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-nfp-data-1-day-vs-sp500.md": {
	id: "tsla-correlation-after-nfp-data-1-day-vs-sp500.md";
  slug: "tsla-correlation-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-nfp-data-1-day.md": {
	id: "tsla-correlation-after-nfp-data-1-day.md";
  slug: "tsla-correlation-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-nfp-data-7-day-vs-gold.md": {
	id: "tsla-correlation-after-nfp-data-7-day-vs-gold.md";
  slug: "tsla-correlation-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-nfp-data-7-day-vs-sp500.md": {
	id: "tsla-correlation-after-nfp-data-7-day-vs-sp500.md";
  slug: "tsla-correlation-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-correlation-after-nfp-data-7-day.md": {
	id: "tsla-correlation-after-nfp-data-7-day.md";
  slug: "tsla-correlation-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-cpi-release-1-day-vs-gold.md": {
	id: "tsla-historical-performance-after-cpi-release-1-day-vs-gold.md";
  slug: "tsla-historical-performance-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-cpi-release-1-day-vs-sp500.md": {
	id: "tsla-historical-performance-after-cpi-release-1-day-vs-sp500.md";
  slug: "tsla-historical-performance-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-cpi-release-1-day.md": {
	id: "tsla-historical-performance-after-cpi-release-1-day.md";
  slug: "tsla-historical-performance-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-cpi-release-7-day-vs-gold.md": {
	id: "tsla-historical-performance-after-cpi-release-7-day-vs-gold.md";
  slug: "tsla-historical-performance-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-cpi-release-7-day-vs-sp500.md": {
	id: "tsla-historical-performance-after-cpi-release-7-day-vs-sp500.md";
  slug: "tsla-historical-performance-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-cpi-release-7-day.md": {
	id: "tsla-historical-performance-after-cpi-release-7-day.md";
  slug: "tsla-historical-performance-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "tsla-historical-performance-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "tsla-historical-performance-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "tsla-historical-performance-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "tsla-historical-performance-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-fed-rate-cut-1-day.md": {
	id: "tsla-historical-performance-after-fed-rate-cut-1-day.md";
  slug: "tsla-historical-performance-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "tsla-historical-performance-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "tsla-historical-performance-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "tsla-historical-performance-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "tsla-historical-performance-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-fed-rate-cut-7-day.md": {
	id: "tsla-historical-performance-after-fed-rate-cut-7-day.md";
  slug: "tsla-historical-performance-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-gdp-report-1-day-vs-gold.md": {
	id: "tsla-historical-performance-after-gdp-report-1-day-vs-gold.md";
  slug: "tsla-historical-performance-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-gdp-report-1-day-vs-sp500.md": {
	id: "tsla-historical-performance-after-gdp-report-1-day-vs-sp500.md";
  slug: "tsla-historical-performance-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-gdp-report-1-day.md": {
	id: "tsla-historical-performance-after-gdp-report-1-day.md";
  slug: "tsla-historical-performance-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-gdp-report-7-day-vs-gold.md": {
	id: "tsla-historical-performance-after-gdp-report-7-day-vs-gold.md";
  slug: "tsla-historical-performance-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-gdp-report-7-day-vs-sp500.md": {
	id: "tsla-historical-performance-after-gdp-report-7-day-vs-sp500.md";
  slug: "tsla-historical-performance-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-gdp-report-7-day.md": {
	id: "tsla-historical-performance-after-gdp-report-7-day.md";
  slug: "tsla-historical-performance-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-inflation-rate-1-day-vs-gold.md": {
	id: "tsla-historical-performance-after-inflation-rate-1-day-vs-gold.md";
  slug: "tsla-historical-performance-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-inflation-rate-1-day-vs-sp500.md": {
	id: "tsla-historical-performance-after-inflation-rate-1-day-vs-sp500.md";
  slug: "tsla-historical-performance-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-inflation-rate-1-day.md": {
	id: "tsla-historical-performance-after-inflation-rate-1-day.md";
  slug: "tsla-historical-performance-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-inflation-rate-7-day-vs-gold.md": {
	id: "tsla-historical-performance-after-inflation-rate-7-day-vs-gold.md";
  slug: "tsla-historical-performance-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-inflation-rate-7-day-vs-sp500.md": {
	id: "tsla-historical-performance-after-inflation-rate-7-day-vs-sp500.md";
  slug: "tsla-historical-performance-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-inflation-rate-7-day.md": {
	id: "tsla-historical-performance-after-inflation-rate-7-day.md";
  slug: "tsla-historical-performance-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-nfp-data-1-day-vs-gold.md": {
	id: "tsla-historical-performance-after-nfp-data-1-day-vs-gold.md";
  slug: "tsla-historical-performance-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-nfp-data-1-day-vs-sp500.md": {
	id: "tsla-historical-performance-after-nfp-data-1-day-vs-sp500.md";
  slug: "tsla-historical-performance-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-nfp-data-1-day.md": {
	id: "tsla-historical-performance-after-nfp-data-1-day.md";
  slug: "tsla-historical-performance-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-nfp-data-7-day-vs-gold.md": {
	id: "tsla-historical-performance-after-nfp-data-7-day-vs-gold.md";
  slug: "tsla-historical-performance-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-nfp-data-7-day-vs-sp500.md": {
	id: "tsla-historical-performance-after-nfp-data-7-day-vs-sp500.md";
  slug: "tsla-historical-performance-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-historical-performance-after-nfp-data-7-day.md": {
	id: "tsla-historical-performance-after-nfp-data-7-day.md";
  slug: "tsla-historical-performance-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-cpi-release-1-day-vs-gold.md": {
	id: "tsla-price-impact-after-cpi-release-1-day-vs-gold.md";
  slug: "tsla-price-impact-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-cpi-release-1-day-vs-sp500.md": {
	id: "tsla-price-impact-after-cpi-release-1-day-vs-sp500.md";
  slug: "tsla-price-impact-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-cpi-release-1-day.md": {
	id: "tsla-price-impact-after-cpi-release-1-day.md";
  slug: "tsla-price-impact-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-cpi-release-7-day-vs-gold.md": {
	id: "tsla-price-impact-after-cpi-release-7-day-vs-gold.md";
  slug: "tsla-price-impact-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-cpi-release-7-day-vs-sp500.md": {
	id: "tsla-price-impact-after-cpi-release-7-day-vs-sp500.md";
  slug: "tsla-price-impact-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-cpi-release-7-day.md": {
	id: "tsla-price-impact-after-cpi-release-7-day.md";
  slug: "tsla-price-impact-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "tsla-price-impact-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "tsla-price-impact-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "tsla-price-impact-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "tsla-price-impact-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-fed-rate-cut-1-day.md": {
	id: "tsla-price-impact-after-fed-rate-cut-1-day.md";
  slug: "tsla-price-impact-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "tsla-price-impact-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "tsla-price-impact-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "tsla-price-impact-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "tsla-price-impact-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-fed-rate-cut-7-day.md": {
	id: "tsla-price-impact-after-fed-rate-cut-7-day.md";
  slug: "tsla-price-impact-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-gdp-report-1-day-vs-gold.md": {
	id: "tsla-price-impact-after-gdp-report-1-day-vs-gold.md";
  slug: "tsla-price-impact-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-gdp-report-1-day-vs-sp500.md": {
	id: "tsla-price-impact-after-gdp-report-1-day-vs-sp500.md";
  slug: "tsla-price-impact-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-gdp-report-1-day.md": {
	id: "tsla-price-impact-after-gdp-report-1-day.md";
  slug: "tsla-price-impact-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-gdp-report-7-day-vs-gold.md": {
	id: "tsla-price-impact-after-gdp-report-7-day-vs-gold.md";
  slug: "tsla-price-impact-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-gdp-report-7-day-vs-sp500.md": {
	id: "tsla-price-impact-after-gdp-report-7-day-vs-sp500.md";
  slug: "tsla-price-impact-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-gdp-report-7-day.md": {
	id: "tsla-price-impact-after-gdp-report-7-day.md";
  slug: "tsla-price-impact-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-inflation-rate-1-day-vs-gold.md": {
	id: "tsla-price-impact-after-inflation-rate-1-day-vs-gold.md";
  slug: "tsla-price-impact-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-inflation-rate-1-day-vs-sp500.md": {
	id: "tsla-price-impact-after-inflation-rate-1-day-vs-sp500.md";
  slug: "tsla-price-impact-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-inflation-rate-1-day.md": {
	id: "tsla-price-impact-after-inflation-rate-1-day.md";
  slug: "tsla-price-impact-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-inflation-rate-7-day-vs-gold.md": {
	id: "tsla-price-impact-after-inflation-rate-7-day-vs-gold.md";
  slug: "tsla-price-impact-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-inflation-rate-7-day-vs-sp500.md": {
	id: "tsla-price-impact-after-inflation-rate-7-day-vs-sp500.md";
  slug: "tsla-price-impact-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-inflation-rate-7-day.md": {
	id: "tsla-price-impact-after-inflation-rate-7-day.md";
  slug: "tsla-price-impact-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-nfp-data-1-day-vs-gold.md": {
	id: "tsla-price-impact-after-nfp-data-1-day-vs-gold.md";
  slug: "tsla-price-impact-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-nfp-data-1-day-vs-sp500.md": {
	id: "tsla-price-impact-after-nfp-data-1-day-vs-sp500.md";
  slug: "tsla-price-impact-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-nfp-data-1-day.md": {
	id: "tsla-price-impact-after-nfp-data-1-day.md";
  slug: "tsla-price-impact-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-nfp-data-7-day-vs-gold.md": {
	id: "tsla-price-impact-after-nfp-data-7-day-vs-gold.md";
  slug: "tsla-price-impact-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-nfp-data-7-day-vs-sp500.md": {
	id: "tsla-price-impact-after-nfp-data-7-day-vs-sp500.md";
  slug: "tsla-price-impact-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-price-impact-after-nfp-data-7-day.md": {
	id: "tsla-price-impact-after-nfp-data-7-day.md";
  slug: "tsla-price-impact-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-cpi-release-1-day-vs-gold.md": {
	id: "tsla-volatility-after-cpi-release-1-day-vs-gold.md";
  slug: "tsla-volatility-after-cpi-release-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-cpi-release-1-day-vs-sp500.md": {
	id: "tsla-volatility-after-cpi-release-1-day-vs-sp500.md";
  slug: "tsla-volatility-after-cpi-release-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-cpi-release-1-day.md": {
	id: "tsla-volatility-after-cpi-release-1-day.md";
  slug: "tsla-volatility-after-cpi-release-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-cpi-release-7-day-vs-gold.md": {
	id: "tsla-volatility-after-cpi-release-7-day-vs-gold.md";
  slug: "tsla-volatility-after-cpi-release-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-cpi-release-7-day-vs-sp500.md": {
	id: "tsla-volatility-after-cpi-release-7-day-vs-sp500.md";
  slug: "tsla-volatility-after-cpi-release-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-cpi-release-7-day.md": {
	id: "tsla-volatility-after-cpi-release-7-day.md";
  slug: "tsla-volatility-after-cpi-release-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-fed-rate-cut-1-day-vs-gold.md": {
	id: "tsla-volatility-after-fed-rate-cut-1-day-vs-gold.md";
  slug: "tsla-volatility-after-fed-rate-cut-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-fed-rate-cut-1-day-vs-sp500.md": {
	id: "tsla-volatility-after-fed-rate-cut-1-day-vs-sp500.md";
  slug: "tsla-volatility-after-fed-rate-cut-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-fed-rate-cut-1-day.md": {
	id: "tsla-volatility-after-fed-rate-cut-1-day.md";
  slug: "tsla-volatility-after-fed-rate-cut-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-fed-rate-cut-7-day-vs-gold.md": {
	id: "tsla-volatility-after-fed-rate-cut-7-day-vs-gold.md";
  slug: "tsla-volatility-after-fed-rate-cut-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-fed-rate-cut-7-day-vs-sp500.md": {
	id: "tsla-volatility-after-fed-rate-cut-7-day-vs-sp500.md";
  slug: "tsla-volatility-after-fed-rate-cut-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-fed-rate-cut-7-day.md": {
	id: "tsla-volatility-after-fed-rate-cut-7-day.md";
  slug: "tsla-volatility-after-fed-rate-cut-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-gdp-report-1-day-vs-gold.md": {
	id: "tsla-volatility-after-gdp-report-1-day-vs-gold.md";
  slug: "tsla-volatility-after-gdp-report-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-gdp-report-1-day-vs-sp500.md": {
	id: "tsla-volatility-after-gdp-report-1-day-vs-sp500.md";
  slug: "tsla-volatility-after-gdp-report-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-gdp-report-1-day.md": {
	id: "tsla-volatility-after-gdp-report-1-day.md";
  slug: "tsla-volatility-after-gdp-report-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-gdp-report-7-day-vs-gold.md": {
	id: "tsla-volatility-after-gdp-report-7-day-vs-gold.md";
  slug: "tsla-volatility-after-gdp-report-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-gdp-report-7-day-vs-sp500.md": {
	id: "tsla-volatility-after-gdp-report-7-day-vs-sp500.md";
  slug: "tsla-volatility-after-gdp-report-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-gdp-report-7-day.md": {
	id: "tsla-volatility-after-gdp-report-7-day.md";
  slug: "tsla-volatility-after-gdp-report-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-inflation-rate-1-day-vs-gold.md": {
	id: "tsla-volatility-after-inflation-rate-1-day-vs-gold.md";
  slug: "tsla-volatility-after-inflation-rate-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-inflation-rate-1-day-vs-sp500.md": {
	id: "tsla-volatility-after-inflation-rate-1-day-vs-sp500.md";
  slug: "tsla-volatility-after-inflation-rate-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-inflation-rate-1-day.md": {
	id: "tsla-volatility-after-inflation-rate-1-day.md";
  slug: "tsla-volatility-after-inflation-rate-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-inflation-rate-7-day-vs-gold.md": {
	id: "tsla-volatility-after-inflation-rate-7-day-vs-gold.md";
  slug: "tsla-volatility-after-inflation-rate-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-inflation-rate-7-day-vs-sp500.md": {
	id: "tsla-volatility-after-inflation-rate-7-day-vs-sp500.md";
  slug: "tsla-volatility-after-inflation-rate-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-inflation-rate-7-day.md": {
	id: "tsla-volatility-after-inflation-rate-7-day.md";
  slug: "tsla-volatility-after-inflation-rate-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-nfp-data-1-day-vs-gold.md": {
	id: "tsla-volatility-after-nfp-data-1-day-vs-gold.md";
  slug: "tsla-volatility-after-nfp-data-1-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-nfp-data-1-day-vs-sp500.md": {
	id: "tsla-volatility-after-nfp-data-1-day-vs-sp500.md";
  slug: "tsla-volatility-after-nfp-data-1-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-nfp-data-1-day.md": {
	id: "tsla-volatility-after-nfp-data-1-day.md";
  slug: "tsla-volatility-after-nfp-data-1-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-nfp-data-7-day-vs-gold.md": {
	id: "tsla-volatility-after-nfp-data-7-day-vs-gold.md";
  slug: "tsla-volatility-after-nfp-data-7-day-vs-gold";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-nfp-data-7-day-vs-sp500.md": {
	id: "tsla-volatility-after-nfp-data-7-day-vs-sp500.md";
  slug: "tsla-volatility-after-nfp-data-7-day-vs-sp500";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"tsla-volatility-after-nfp-data-7-day.md": {
	id: "tsla-volatility-after-nfp-data-7-day.md";
  slug: "tsla-volatility-after-nfp-data-7-day";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
};

	};

	type DataEntryMap = {
		
	};

	type AnyEntryMap = ContentEntryMap & DataEntryMap;

	export type ContentConfig = typeof import("../../src/content/config.js");
}
