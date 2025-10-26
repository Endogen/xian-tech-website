import reflex as rx

from ..components.common import page_layout, section
from ..data import ECOSYSTEM_INITIATIVES
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_HOVER,
    ACCENT_SOFT,
    BORDER_COLOR,
    BORDER_BRIGHT,
    PRIMARY_BG,
    SURFACE,
    TEXT_MUTED,
    TEXT_PRIMARY,
)


def ecosystem_card_detailed(item: dict) -> rx.Component:
    """Detailed ecosystem card."""
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.text(item["emoji"], size="8", line_height="1"),
                rx.heading(item["title"], size="6", color=TEXT_PRIMARY, weight="bold"),
                gap="1.25rem",
                align_items="center",
            ),
            rx.text(
                item["description"],
                size="3",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            rx.vstack(
                *[
                    rx.flex(
                        rx.text("→", color=ACCENT, size="4"),
                        rx.text(link, size="3", color=TEXT_PRIMARY),
                        gap="1rem",
                        align_items="center",
                    )
                    for link in item["links"]
                ],
                spacing="3",
                align_items="start",
                width="100%",
            ),
            spacing="6",
            align_items="start",
        ),
        padding="3rem",
        background=SURFACE,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="14px",
        transition="all 0.3s ease",
        _hover={
            "borderColor": BORDER_BRIGHT,
            "transform": "translateY(-4px)",
        },
        height="100%",
    )


def ecosystem_page() -> rx.Component:
    """Ecosystem route."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("ECOSYSTEM", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Supporting the Python Blockchain Community",
                    size="9",
                    color=TEXT_PRIMARY,
                    line_height="1.2",
                    weight="bold",
                ),
                rx.text(
                    "We maintain an open collaboration model with researchers, builders, and operators. "
                    "Explore the pathways to shape the future of Python-powered decentralized systems.",
                    size="4",
                    color=TEXT_MUTED,
                    max_width="800px",
                    line_height="1.7",
                ),
                spacing="6",
                align_items="start",
            ),
            style={"paddingBottom": "3rem"},
        ),
        section(
            rx.grid(
                *[ecosystem_card_detailed(item) for item in ECOSYSTEM_INITIATIVES],
                template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                gap="2rem",
            ),
            style={"paddingTop": "0"},
        ),
        section(
            rx.box(
                rx.vstack(
                    rx.heading("Partner With Us", size="7", color=TEXT_PRIMARY, weight="bold"),
                    rx.text(
                        "Whether you're a researcher, builder, or educator, we'd love to collaborate.",
                        size="4",
                        color=TEXT_MUTED,
                        max_width="600px",
                        text_align="center",
                        line_height="1.7",
                    ),
                    rx.link(
                        rx.button(
                            "Request Partnership",
                            size="4",
                            background_color=ACCENT,
                            color=PRIMARY_BG,
                            border_radius="10px",
                            padding="1.25rem 2rem",
                            cursor="pointer",
                            _hover={"backgroundColor": ACCENT_HOVER},
                        ),
                        href="mailto:foundation@xian.technology",
                    ),
                    spacing="6",
                    align_items="center",
                ),
                padding="5rem 3rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
                text_align="center",
            )
        ),
    )


__all__ = ["ecosystem_page"]
