import reflex as rx

from ..components.common import hover_icon_chip, icon_watermark_hover_card, page_layout, section
from ..theme import ACCENT, ACCENT_GLOW, ACCENT_SOFT, BORDER_COLOR, BORDER_BRIGHT, TEXT_MUTED, TEXT_PRIMARY
from ..data import _slugify


DEV_LINKS = [
    {
        "title": "Contracting Playground",
        "description": "Interactive IDE in the browser to build, test, and deploy contracts.",
        "href": "https://playground.xian.technology",
        "icon": "flask_conical",
        "highlight": True,
    },
    {
        "title": "Contracting Hub",
        "description": "Curated, deploy-ready contracts with metadata and one-click launch into the playground.",
        "href": "https://hub.xian.technology",
        "icon": "folder_open",
    },
    {
        "title": "Documentation",
        "description": "Deep dives on contracting, node setup, BDS queries, and APIs.",
        "href": "https://docs.xian.technology",
        "icon": "book_open",
    },
    {
        "title": "Tutorials & First Steps",
        "description": "Guides to get from zero to a running network and deployed contract.",
        "href": "/tutorials",
        "icon": "graduation_cap",
    },
    {
        "title": "Samples & SDKs",
        "description": "Code samples and SDK usage for Xian tooling.",
        "href": "/samples",
        "icon": "code",
    },
    {
        "title": "Roadmap",
        "description": "Past, current, and upcoming milestones for the Xian stack.",
        "href": "/roadmap",
        "icon": "route",
    },
    {
        "title": "Contact",
        "description": "Reach the foundation for support, reviews, or partnerships.",
        "href": "/contact",
        "icon": "mail",
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
    icon = link.get("icon", "sparkles")
    accent_border = f"1px solid {ACCENT_GLOW}" if link.get("highlight") else f"1px solid {BORDER_COLOR}"
    return rx.link(
        icon_watermark_hover_card(
            rx.flex(
                hover_icon_chip(icon),
                rx.hstack(
                    rx.heading(link["title"], size="5", color=TEXT_PRIMARY, weight="bold"),
                    rx.badge("Featured", color_scheme="green", variant="soft")
                    if link.get("highlight")
                    else rx.box(),
                    align_items="center",
                    gap="0.75rem",
                    wrap="wrap",
                    width="100%",
                ),
                direction={"base": "column", "lg": "row"},
                align={"base": "start", "lg": "center"},
                spacing="3",
                width="100%",
            ),
            rx.text(link["description"], size="3", color=TEXT_MUTED, line_height="1.7"),
            icon=icon,
            padding="1.75rem",
            border=accent_border,
            box_shadow="0 6px 20px rgba(0,0,0,0.12)",
            _hover={
                "borderColor": BORDER_BRIGHT,
                "boxShadow": f"0 0 0 1px {ACCENT_GLOW}, 0 0 12px {ACCENT_SOFT}",
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
