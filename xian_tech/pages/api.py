import reflex as rx

from ..components.common import page_layout, section
from ..theme import ACCENT, ACCENT_GLOW, ACCENT_SOFT, TEXT_MUTED, TEXT_PRIMARY

SEARCH_SECTIONS = [
    {
        "title": "API References",
        "subtitle": "Reference endpoints for BDS, transactions, and contracts.",
        "category": "Developers",
        "badge": "Page",
        "href": "/api",
        "keywords": ["API", "References", "BDS", "Endpoints"],
    }
]


def api_page() -> rx.Component:
    """API references page."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("API REFERENCES", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "API References",
                    size="8",
                    color=TEXT_PRIMARY,
                    weight="bold",
                    line_height="1.2",
                ),
                rx.text(
                    "This page will document the core API endpoints for chain data, transactions, and smart contracts.",
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


__all__ = ["api_page"]
