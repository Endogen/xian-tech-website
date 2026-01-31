import reflex as rx

from ..components.common import linked_heading, page_layout, section
from ..data import COMMUNITY_STREAMS
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_HOVER,
    ACCENT_SOFT,
    BORDER_COLOR,
    BORDER_BRIGHT,
    PRIMARY_BG,
    SURFACE,
    SURFACE_HOVER,
    TEXT_ACCENT,
    TEXT_MUTED,
    TEXT_PRIMARY,
)

SEARCH_SECTIONS = [
    {
        "title": "Join the Xian Network Community",
        "subtitle": "Coordinate upgrades, stress tests, and community missions.",
        "category": "Community",
        "badge": "Page",
        "href": "/community",
        "keywords": ["Community", "Contribute", "Missions"],
    },
    {
        "title": "How to Contribute",
        "subtitle": "Programs for builders, operators, and educators.",
        "category": "Community",
        "badge": "Section",
        "href": "/community",
        "keywords": ["Contribute", "Programs"],
    },
    *[
        {
            "title": stream["title"],
            "subtitle": stream["description"],
            "category": "Community",
            "badge": "Program",
            "href": "/community",
            "keywords": [stream["title"]],
        }
        for stream in COMMUNITY_STREAMS
    ],
    {
        "title": "Developer Resources",
        "subtitle": "Documentation, tutorials, and tools to build on Xian.",
        "category": "Community",
        "badge": "Resource",
        "href": "/community",
        "keywords": ["Documentation", "Tutorials", "Tools"],
    },
]


def community_card_detailed(item: dict) -> rx.Component:
    """Community program card."""
    return rx.box(
        rx.vstack(
            rx.heading(item["title"], size="5", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                item["description"],
                size="3",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            spacing="4",
            align_items="start",
        ),
        padding="2.5rem",
        background=SURFACE,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="14px",
        border_left=f"4px solid {ACCENT}",
        transition="all 0.3s ease",
        _hover={
            "borderColor": BORDER_BRIGHT,
            "backgroundColor": SURFACE_HOVER,
        },
    )


def community_page() -> rx.Component:
    """Community route."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("COMMUNITY", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Join the Xian Network Community",
                    size="9",
                    color=TEXT_PRIMARY,
                    line_height="1.2",
                    weight="bold",
                ),
                rx.text(
                    "Enhance existing contracts, stress test upgrades, and coordinate rollouts "
                    "with a foundation that values precision engineering over hype.",
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
            rx.vstack(
                linked_heading("How to Contribute", size="7", color=TEXT_PRIMARY, weight="bold"),
                rx.grid(
                    *[community_card_detailed(item) for item in COMMUNITY_STREAMS],
                    template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                    gap="2rem",
                ),
                spacing="6",
                align_items="start",
                width="100%",
            ),
            padding_top="0",
        ),
        section(
            rx.grid(
                rx.box(
                    rx.vstack(
                        linked_heading("Developer Resources", size="6", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Access documentation, tutorials, and tools to build on Xian Network.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        rx.vstack(
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="book_open", size=16),
                                    rx.text("Documentation", size="3"),
                                    align_items="center",
                                    gap="0.5rem",
                                ),
                                href="https://xian.org",
                                is_external=True,
                                color=TEXT_ACCENT,
                                _hover={"textDecoration": "none", "color": ACCENT},
                            ),
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="github", size=16),
                                    rx.text("GitHub Repository", size="3"),
                                    align_items="center",
                                    gap="0.5rem",
                                ),
                                href="https://github.com/xian-network",
                                is_external=True,
                                color=TEXT_ACCENT,
                                _hover={"textDecoration": "none", "color": ACCENT},
                            ),
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="graduation_cap", size=16),
                                    rx.text("Tutorials & Guides", size="3"),
                                    align_items="center",
                                    gap="0.5rem",
                                ),
                                href="https://xian.org",
                                is_external=True,
                                color=TEXT_ACCENT,
                                _hover={"textDecoration": "none", "color": ACCENT},
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                        spacing="5",
                        align_items="start",
                    ),
                    padding="3rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                rx.box(
                    rx.vstack(
                        linked_heading("Get in Touch", size="6", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Have questions or want to collaborate? Reach out to our team.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        rx.link(
                            rx.button(
                                "Contact Foundation",
                                size="4",
                                background_color=ACCENT,
                                color=PRIMARY_BG,
                                border_radius="10px",
                                padding="1.25rem 2rem",
                                width="100%",
                                cursor="pointer",
                                _hover={"backgroundColor": ACCENT_HOVER},
                            ),
                            href="mailto:foundation@xian.technology",
                        ),
                        spacing="5",
                        align_items="start",
                    ),
                    padding="3rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
                gap="2rem",
            )
        ),
    )


__all__ = ["community_page"]
