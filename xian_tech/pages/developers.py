import reflex as rx

from ..components.common import page_layout, section
from ..data import _slugify
from ..theme import ACCENT, ACCENT_GLOW, ACCENT_SOFT, BORDER_COLOR, BORDER_BRIGHT, SURFACE, TEXT_MUTED, TEXT_PRIMARY


DEV_LINKS = [
    {
        "title": "Contracting Playground",
        "description": "Interactive IDE in the browser to build, test, and deploy contracts.",
        "href": "https://playground.xian.technology",
        "highlight": True,
    },
    {
        "title": "Contracting Hub",
        "description": "Curated, deploy-ready contracts with metadata and one-click launch into the playground.",
        "href": "https://hub.xian.technology",
    },
    {
        "title": "Documentation",
        "description": "Deep dives on contracting, node setup, BDS queries, and APIs.",
        "href": "https://docs.xian.technology",
    },
    {
        "title": "Tutorials & First Steps",
        "description": "Guides to get from zero to a running network and deployed contract.",
        "href": "/tutorials",
    },
    {
        "title": "Samples & SDKs",
        "description": "Code samples and SDK usage for Xian tooling.",
        "href": "/samples",
    },
    {
        "title": "Roadmap",
        "description": "Past, current, and upcoming milestones for the Xian stack.",
        "href": "/roadmap",
    },
    {
        "title": "Contact",
        "description": "Reach the foundation for support, reviews, or partnerships.",
        "href": "/contact",
    },
]

SEARCH_SECTIONS = [
    {
        "title": "Build with Xian",
        "subtitle": "Playground, curated contracts, docs, SDKs, and roadmap in one hub.",
        "category": "Developers",
        "badge": "Page",
        "href": "/developers",
        "keywords": ["Playground", "Contracts", "Docs", "SDKs"],
    },
    *[
        {
            "title": link["title"],
            "subtitle": link["description"],
            "category": "Developers",
            "badge": "Resource",
            "href": link["href"],
            "id": f"developers-resource-{_slugify(link['title'])}",
            "keywords": [link["title"]],
        }
        for link in DEV_LINKS
    ],
]


def _dev_card(link: dict) -> rx.Component:
    accent_border = f"1px solid {ACCENT_GLOW}" if link.get("highlight") else f"1px solid {BORDER_COLOR}"
    return rx.link(
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.heading(link["title"], size="5", color=TEXT_PRIMARY, weight="bold"),
                    rx.badge("Featured", color_scheme="green", variant="soft") if link.get("highlight") else rx.box(),
                    align_items="center",
                    gap="0.75rem",
                ),
                rx.text(link["description"], size="3", color=TEXT_MUTED, line_height="1.7"),
                spacing="3",
                align_items="start",
            ),
            padding="1.75rem",
            background=SURFACE,
            border=accent_border,
            border_radius="14px",
            box_shadow="0 6px 20px rgba(0,0,0,0.12)",
            transition="all 0.25s ease",
            _hover={
                "borderColor": BORDER_BRIGHT,
                "transform": "translateY(-4px)",
                "boxShadow": f"0 12px 28px {ACCENT_SOFT}",
            },
            height="100%",
        ),
        href=link["href"],
        _hover={"textDecoration": "none"},
    )


def developers_page() -> rx.Component:
    """Developer hub route."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("DEVELOPERS", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Build with Xian",
                    size="9",
                    color=TEXT_PRIMARY,
                    line_height="1.2",
                    weight="bold",
                ),
                rx.text(
                    "Everything you need to ship on the Xian stack: playground, curated contracts, docs, SDKs, and roadmap.",
                    size="4",
                    color=TEXT_MUTED,
                    max_width="800px",
                    line_height="1.7",
                ),
                spacing="6",
                align_items="start",
            ),
            padding_bottom="3rem",
        ),
        section(
            rx.grid(
                *[_dev_card(link) for link in DEV_LINKS],
                template_columns={"base": "repeat(1,  minmax(0, 1fr))", "md": "repeat(2, minmax(0, 1fr))"},
                gap="1.5rem",
            ),
            padding_top="0",
        ),
    )


__all__ = ["developers_page"]
