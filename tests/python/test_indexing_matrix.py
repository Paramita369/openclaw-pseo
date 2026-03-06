from __future__ import annotations

from content_features import CORE_WINDOW_DAYS, is_core_page_for_window


def test_recent_self_canonical_page_is_core() -> None:
    assert is_core_page_for_window(
        event_date='2026-02-12',
        as_of_date='2026-03-06',
        canonical_target='self',
        robots_directive='index,follow',
        in_blog_sitemap=True,
        window_days=CORE_WINDOW_DAYS,
    )


def test_old_or_nonself_page_is_not_core() -> None:
    assert not is_core_page_for_window(
        event_date='2025-08-01',
        as_of_date='2026-03-06',
        canonical_target='hub',
        robots_directive='index,follow',
        in_blog_sitemap=False,
        window_days=CORE_WINDOW_DAYS,
    )


def test_noindex_page_is_not_core() -> None:
    assert not is_core_page_for_window(
        event_date='2026-02-12',
        as_of_date='2026-03-06',
        canonical_target='none',
        robots_directive='noindex,follow',
        in_blog_sitemap=False,
        window_days=CORE_WINDOW_DAYS,
    )
