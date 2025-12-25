import reflex as rx

from ..components.common import page_layout, section
from ..theme import ACCENT, ACCENT_GLOW, ACCENT_SOFT, TEXT_MUTED, TEXT_PRIMARY


def team_page() -> rx.Component:
    """Placeholder team page."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("TEAM", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Meet the Team",
                    size="8",
                    color=TEXT_PRIMARY,
                    weight="bold",
                    line_height="1.2",
                ),
                rx.text(
                    "This page will introduce the contributors and roles behind the Xian Technology Foundation.",
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


__all__ = ["team_page"]
