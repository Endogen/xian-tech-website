import reflex as rx

from ..components.common import page_layout, section
from ..theme import ACCENT, ACCENT_GLOW, ACCENT_SOFT, TEXT_MUTED, TEXT_PRIMARY

SEARCH_SECTIONS = [
    {
        "title": "Tutorials & First Steps",
        "subtitle": "Step-by-step guides for building on the Xian stack.",
        "category": "Developers",
        "badge": "Page",
        "href": "/tutorials",
        "keywords": ["Tutorials", "Getting Started", "Guides", "Developers"],
    }
]


def tutorials_page() -> rx.Component:
    """Tutorials page."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("TUTORIALS", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Tutorials & First Steps",
                    size="8",
                    color=TEXT_PRIMARY,
                    weight="bold",
                    line_height="1.2",
                ),
                rx.text(
                    "This page will collect starter tutorials, walkthroughs, and first deployments on Xian.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    max_width="900px",
                ),
                spacing="6",
                align_items="start",
            )
        )
    )


__all__ = ["tutorials_page"]
