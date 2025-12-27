import reflex as rx

from ..components.common import page_layout, section
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_HOVER,
    ACCENT_SOFT,
    BORDER_COLOR,
    PRIMARY_BG,
    SURFACE,
    TEXT_MUTED,
    TEXT_PRIMARY,
)


def not_found_page() -> rx.Component:
    """Branded 404 page for unknown routes."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("404", size="2", letter_spacing="0.2em", color=ACCENT, weight="medium"),
                    padding="0.5rem 1rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="999px",
                ),
                rx.heading(
                    "Page not found",
                    size="8",
                    color=TEXT_PRIMARY,
                    weight="bold",
                    line_height="1.1",
                    text_align="center",
                ),
                rx.text(
                    "We could not find that page. It may have moved or the URL may be misspelled.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    max_width="720px",
                    text_align="center",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Back to home",
                            size="4",
                            background_color=ACCENT,
                            color=PRIMARY_BG,
                            border_radius="10px",
                            padding="1rem 1.75rem",
                            transition="all 0.2s ease",
                            _hover={
                                "backgroundColor": ACCENT_HOVER,
                                "transform": "translateY(-2px)",
                            },
                        ),
                        href="/",
                        _hover={"textDecoration": "none"},
                    ),
                    rx.link(
                        rx.button(
                            "Contact the foundation",
                            size="4",
                            variant="outline",
                            border_color=BORDER_COLOR,
                            color=TEXT_PRIMARY,
                            background_color="transparent",
                            border_radius="10px",
                            padding="1rem 1.75rem",
                            transition="all 0.2s ease",
                            _hover={
                                "backgroundColor": SURFACE,
                                "borderColor": TEXT_MUTED,
                            },
                        ),
                        href="/contact",
                        _hover={"textDecoration": "none"},
                    ),
                    spacing="3",
                    wrap="wrap",
                    justify="center",
                ),
                spacing="5",
                align_items="center",
                width="100%",
            ),
        )
    )


__all__ = ["not_found_page"]
