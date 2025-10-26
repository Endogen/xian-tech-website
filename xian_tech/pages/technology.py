import reflex as rx

from ..components.common import code_block, page_layout, section, terminal_prompt
from ..data import TECHNOLOGY_TRACKS
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_HOVER,
    ACCENT_SOFT,
    BORDER_BRIGHT,
    BORDER_COLOR,
    PRIMARY_BG,
    SURFACE,
    SURFACE_BRIGHT,
    SURFACE_HOVER,
    TEXT_MUTED,
    TEXT_PRIMARY,
)


def technology_card_detailed(track: dict) -> rx.Component:
    """Detailed technology card."""
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.text(track["icon"], size="8", line_height="1"),
                rx.heading(track["title"], size="6", color=TEXT_PRIMARY, weight="bold"),
                gap="1.25rem",
                align_items="center",
            ),
            rx.text(
                track["description"],
                size="4",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            rx.grid(
                *[
                    rx.flex(
                        rx.text("→", color=ACCENT, size="4"),
                        rx.text(point, size="3", color=TEXT_MUTED),
                        gap="1rem",
                        align_items="center",
                    )
                    for point in track["points"]
                ],
                template_columns={"base": "1fr", "md": "1fr"},
                gap="1rem",
            ),
            code_block(track["code_sample"]),
            spacing="6",
            align_items="start",
        ),
        padding="3.5rem",
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


def roadmap_section() -> rx.Component:
    """Roadmap section with cards."""
    return section(
        rx.link(
            rx.box(
                rx.vstack(
                    rx.heading("Xian Technology Roadmap", size="7", color=TEXT_PRIMARY, weight="bold"),
                    rx.text(
                        "Transparent milestones for the contracting library, node, and ecosystem tooling.",
                        size="4",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    rx.grid(
                        rx.box(
                            rx.vstack(
                                rx.text("🧱", size="7", line_height="1"),
                                rx.text("In Progress", size="4", weight="bold", color=TEXT_PRIMARY),
                                rx.text("Active engineering sprints", size="2", color=TEXT_MUTED, text_align="center"),
                                spacing="3",
                                align_items="center",
                            ),
                            padding="2rem",
                            background=SURFACE_BRIGHT,
                            border=f"1px solid {BORDER_BRIGHT}",
                            border_radius="10px",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text("🧪", size="7", line_height="1"),
                                rx.text("Testing", size="4", weight="bold", color=TEXT_PRIMARY),
                                rx.text("Formal verification & audits", size="2", color=TEXT_MUTED, text_align="center"),
                                spacing="3",
                                align_items="center",
                            ),
                            padding="2rem",
                            background=SURFACE_BRIGHT,
                            border=f"1px solid {BORDER_BRIGHT}",
                            border_radius="10px",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text("✅", size="7", line_height="1"),
                                rx.text("Completed", size="4", weight="bold", color=TEXT_PRIMARY),
                                rx.text("Shipped improvements", size="2", color=TEXT_MUTED, text_align="center"),
                                spacing="3",
                                align_items="center",
                            ),
                            padding="2rem",
                            background=SURFACE_BRIGHT,
                            border=f"1px solid {BORDER_BRIGHT}",
                            border_radius="10px",
                        ),
                        template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                        gap="1.5rem",
                        width="100%",
                    ),
                    rx.flex(
                        rx.flex(
                            rx.text("View Full Roadmap on GitHub", size="4", weight="medium", color=ACCENT),
                            rx.text("→", size="5", weight="bold", color=ACCENT),
                            gap="1rem",
                            align_items="center",
                        ),
                        justify="center",
                        width="100%",
                    ),
                    spacing="7",
                    align_items="start",
                    width="100%",
                ),
                padding="3.5rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
                width="100%",
                transition="all 0.3s ease",
                cursor="pointer",
                _hover={
                    "borderColor": ACCENT,
                    "backgroundColor": SURFACE_HOVER,
                    "transform": "translateY(-4px)",
                    "boxShadow": f"0 20px 40px {ACCENT_SOFT}",
                },
            ),
            href="https://github.com/orgs/xian-technology/projects/1",
            is_external=True,
            _hover={"textDecoration": "none"},
            width="100%",
        )
    )


def technology_page() -> rx.Component:
    """Technology route."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("TECHNOLOGY", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Building the Future of Python Blockchain",
                    size="9",
                    color=TEXT_PRIMARY,
                    line_height="1.2",
                    weight="bold",
                ),
                rx.text(
                    "Our teams extend the contracting library and node underpinning Xian Network, "
                    "keeping Python-native infrastructure performant, observable, and secure.",
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
            rx.vstack(
                *[technology_card_detailed(track) for track in TECHNOLOGY_TRACKS],
                spacing="9",
            ),
            style={"paddingTop": "0"},
        ),
        roadmap_section(),
        section(
            rx.box(
                rx.vstack(
                    rx.heading("Get Started", size="7", color=TEXT_PRIMARY, weight="bold"),
                    rx.text(
                        "Deploy your first smart contract on Xian Network",
                        size="4",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    rx.vstack(
                        terminal_prompt("pip install xian-py"),
                        terminal_prompt("xian init my-contract"),
                        terminal_prompt("xian deploy"),
                        spacing="3",
                        width="100%",
                    ),
                    rx.link(
                        rx.button(
                            "View Documentation",
                            size="4",
                            background_color=ACCENT,
                            color=PRIMARY_BG,
                            border_radius="10px",
                            padding="1.25rem 2rem",
                            cursor="pointer",
                            _hover={"backgroundColor": ACCENT_HOVER},
                        ),
                        href="https://xian.org",
                        is_external=True,
                    ),
                    spacing="6",
                    align_items="start",
                    width="100%",
                ),
                padding="3.5rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
            )
        ),
    )


__all__ = ["technology_page"]
