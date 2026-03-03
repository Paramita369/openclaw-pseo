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
"btc-after-cpi-2024-08-14.md": {
	id: "btc-after-cpi-2024-08-14.md";
  slug: "btc-after-cpi-2024-08-14";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-after-fomc-2024-01-30.md": {
	id: "btc-after-fomc-2024-01-30.md";
  slug: "btc-after-fomc-2024-01-30";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-after-fomc-2024-04-30.md": {
	id: "btc-after-fomc-2024-04-30.md";
  slug: "btc-after-fomc-2024-04-30";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-after-nfp-2024-04-05.md": {
	id: "btc-after-nfp-2024-04-05.md";
  slug: "btc-after-nfp-2024-04-05";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"btc-after-nfp-2024-05-03.md": {
	id: "btc-after-nfp-2024-05-03.md";
  slug: "btc-after-nfp-2024-05-03";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-after-cpi-2024-06-12.md": {
	id: "eth-after-cpi-2024-06-12.md";
  slug: "eth-after-cpi-2024-06-12";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-after-cpi-2024-08-14.md": {
	id: "eth-after-cpi-2024-08-14.md";
  slug: "eth-after-cpi-2024-08-14";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-after-cpi-2025-02-12.md": {
	id: "eth-after-cpi-2025-02-12.md";
  slug: "eth-after-cpi-2025-02-12";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-after-fomc-2024-01-30.md": {
	id: "eth-after-fomc-2024-01-30.md";
  slug: "eth-after-fomc-2024-01-30";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-after-fomc-2024-04-30.md": {
	id: "eth-after-fomc-2024-04-30.md";
  slug: "eth-after-fomc-2024-04-30";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-after-fomc-2024-06-11.md": {
	id: "eth-after-fomc-2024-06-11.md";
  slug: "eth-after-fomc-2024-06-11";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"eth-after-nfp-2024-04-05.md": {
	id: "eth-after-nfp-2024-04-05.md";
  slug: "eth-after-nfp-2024-04-05";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-cpi-2024-02-20.md": {
	id: "gold-after-cpi-2024-02-20.md";
  slug: "gold-after-cpi-2024-02-20";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-cpi-2024-03-12.md": {
	id: "gold-after-cpi-2024-03-12.md";
  slug: "gold-after-cpi-2024-03-12";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-cpi-2024-05-15.md": {
	id: "gold-after-cpi-2024-05-15.md";
  slug: "gold-after-cpi-2024-05-15";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-cpi-2025-02-12.md": {
	id: "gold-after-cpi-2025-02-12.md";
  slug: "gold-after-cpi-2025-02-12";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-fomc-2024-01-30.md": {
	id: "gold-after-fomc-2024-01-30.md";
  slug: "gold-after-fomc-2024-01-30";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-fomc-2024-07-30.md": {
	id: "gold-after-fomc-2024-07-30.md";
  slug: "gold-after-fomc-2024-07-30";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-fomc-2024-11-06.md": {
	id: "gold-after-fomc-2024-11-06.md";
  slug: "gold-after-fomc-2024-11-06";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-nfp-2024-01-05.md": {
	id: "gold-after-nfp-2024-01-05.md";
  slug: "gold-after-nfp-2024-01-05";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-nfp-2024-03-01.md": {
	id: "gold-after-nfp-2024-03-01.md";
  slug: "gold-after-nfp-2024-03-01";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-nfp-2024-04-05.md": {
	id: "gold-after-nfp-2024-04-05.md";
  slug: "gold-after-nfp-2024-04-05";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-nfp-2024-05-03.md": {
	id: "gold-after-nfp-2024-05-03.md";
  slug: "gold-after-nfp-2024-05-03";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-nfp-2024-06-07.md": {
	id: "gold-after-nfp-2024-06-07.md";
  slug: "gold-after-nfp-2024-06-07";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-nfp-2024-08-02.md": {
	id: "gold-after-nfp-2024-08-02.md";
  slug: "gold-after-nfp-2024-08-02";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-nfp-2024-09-06.md": {
	id: "gold-after-nfp-2024-09-06.md";
  slug: "gold-after-nfp-2024-09-06";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-nfp-2024-10-04.md": {
	id: "gold-after-nfp-2024-10-04.md";
  slug: "gold-after-nfp-2024-10-04";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"gold-after-nfp-2025-01-10.md": {
	id: "gold-after-nfp-2025-01-10.md";
  slug: "gold-after-nfp-2025-01-10";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-cpi-2024-04-10.md": {
	id: "qqq-after-cpi-2024-04-10.md";
  slug: "qqq-after-cpi-2024-04-10";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-cpi-2024-05-15.md": {
	id: "qqq-after-cpi-2024-05-15.md";
  slug: "qqq-after-cpi-2024-05-15";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-cpi-2024-09-11.md": {
	id: "qqq-after-cpi-2024-09-11.md";
  slug: "qqq-after-cpi-2024-09-11";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-cpi-2024-10-10.md": {
	id: "qqq-after-cpi-2024-10-10.md";
  slug: "qqq-after-cpi-2024-10-10";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-cpi-2024-11-14.md": {
	id: "qqq-after-cpi-2024-11-14.md";
  slug: "qqq-after-cpi-2024-11-14";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-fomc-2024-01-30.md": {
	id: "qqq-after-fomc-2024-01-30.md";
  slug: "qqq-after-fomc-2024-01-30";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-fomc-2024-07-30.md": {
	id: "qqq-after-fomc-2024-07-30.md";
  slug: "qqq-after-fomc-2024-07-30";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-fomc-2024-12-17.md": {
	id: "qqq-after-fomc-2024-12-17.md";
  slug: "qqq-after-fomc-2024-12-17";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-nfp-2024-02-02.md": {
	id: "qqq-after-nfp-2024-02-02.md";
  slug: "qqq-after-nfp-2024-02-02";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-nfp-2024-08-02.md": {
	id: "qqq-after-nfp-2024-08-02.md";
  slug: "qqq-after-nfp-2024-08-02";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-nfp-2024-10-04.md": {
	id: "qqq-after-nfp-2024-10-04.md";
  slug: "qqq-after-nfp-2024-10-04";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-nfp-2024-12-06.md": {
	id: "qqq-after-nfp-2024-12-06.md";
  slug: "qqq-after-nfp-2024-12-06";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"qqq-after-nfp-2025-01-10.md": {
	id: "qqq-after-nfp-2025-01-10.md";
  slug: "qqq-after-nfp-2025-01-10";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-cpi-2024-03-12.md": {
	id: "spy-after-cpi-2024-03-12.md";
  slug: "spy-after-cpi-2024-03-12";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-cpi-2024-05-15.md": {
	id: "spy-after-cpi-2024-05-15.md";
  slug: "spy-after-cpi-2024-05-15";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-cpi-2024-07-11.md": {
	id: "spy-after-cpi-2024-07-11.md";
  slug: "spy-after-cpi-2024-07-11";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-cpi-2024-11-14.md": {
	id: "spy-after-cpi-2024-11-14.md";
  slug: "spy-after-cpi-2024-11-14";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-fomc-2024-01-30.md": {
	id: "spy-after-fomc-2024-01-30.md";
  slug: "spy-after-fomc-2024-01-30";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-fomc-2024-03-19.md": {
	id: "spy-after-fomc-2024-03-19.md";
  slug: "spy-after-fomc-2024-03-19";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-fomc-2024-07-30.md": {
	id: "spy-after-fomc-2024-07-30.md";
  slug: "spy-after-fomc-2024-07-30";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-fomc-2024-12-17.md": {
	id: "spy-after-fomc-2024-12-17.md";
  slug: "spy-after-fomc-2024-12-17";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-fomc-2025-01-29.md": {
	id: "spy-after-fomc-2025-01-29.md";
  slug: "spy-after-fomc-2025-01-29";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-nfp-2024-01-05.md": {
	id: "spy-after-nfp-2024-01-05.md";
  slug: "spy-after-nfp-2024-01-05";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-nfp-2024-02-02.md": {
	id: "spy-after-nfp-2024-02-02.md";
  slug: "spy-after-nfp-2024-02-02";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-nfp-2024-07-05.md": {
	id: "spy-after-nfp-2024-07-05.md";
  slug: "spy-after-nfp-2024-07-05";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-nfp-2024-08-02.md": {
	id: "spy-after-nfp-2024-08-02.md";
  slug: "spy-after-nfp-2024-08-02";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"spy-after-nfp-2024-10-04.md": {
	id: "spy-after-nfp-2024-10-04.md";
  slug: "spy-after-nfp-2024-10-04";
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
