import reflex as rx

from ..components.common import page_layout, section
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_SOFT,
    BORDER_COLOR,
    DARK_ACCENT,
    DARK_ACCENT_GLOW,
    LIGHT_ACCENT,
    LIGHT_ACCENT_GLOW,
    SURFACE,
    SURFACE_BRIGHT,
    TEXT_MUTED,
    TEXT_PRIMARY,
)
from ..state import State

MD_MEDIA = "@media (min-width: 1024px)"


def _connectors_svg() -> rx.Component:
    """SVG connectors showing Foundation connecting to Technology and Network."""
    # Colors need to be static strings for SVG attributes
    stroke_light = LIGHT_ACCENT
    stroke_dark = DARK_ACCENT
    glow_light = LIGHT_ACCENT_GLOW
    glow_dark = DARK_ACCENT_GLOW

    # Path from Foundation (center-bottom) to Technology (middle of card)
    # Using quadratic bezier: M=move, Q=quadratic curve
    # SVG is behind cards, so paths go to card centers
    path_left = "M 50 43 Q 50 59, 16.67 78"

    # Path from Foundation (center-bottom) to Network (middle of card)
    path_right = "M 50 43 Q 50 59, 83.33 78"

    def make_path(d: str) -> rx.Component:
        return rx.el.svg.path(
            d=d,
            stroke=rx.cond(State.theme_mode == "light", stroke_light, stroke_dark),
            stroke_width="2",
            fill="none",
            stroke_linecap="round",
        )

    def make_glow_path(d: str) -> rx.Component:
        return rx.el.svg.path(
            d=d,
            stroke=rx.cond(State.theme_mode == "light", glow_light, glow_dark),
            stroke_width="8",
            fill="none",
            stroke_linecap="round",
            opacity="0.4",
        )

    return rx.el.svg(
        # Glow layers (behind main paths)
        make_glow_path(path_left),
        make_glow_path(path_right),
        # Main paths
        make_path(path_left),
        make_path(path_right),
        view_box="0 0 100 100",
        preserve_aspect_ratio="none",
        position="absolute",
        top="0",
        left="0",
        width="100%",
        height="100%",
        z_index="0",
        pointer_events="none",
        style={
            "display": "none",
            MD_MEDIA: {"display": "block"},
        },
    )


def _term_card(title: str, body: str, highlight: bool = False) -> rx.Component:
    """Reusable card for terminology entries."""
    return rx.box(
        rx.vstack(
            rx.text(title, size="4", weight="bold", color=TEXT_PRIMARY),
            rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
            spacing="3",
            align_items="start",
        ),
        padding="1.75rem",
        background=rx.cond(highlight, SURFACE_BRIGHT, SURFACE),
        border=f"1px solid {ACCENT_GLOW}" if highlight else f"1px solid {BORDER_COLOR}",
        border_radius="16px",
        box_shadow=rx.cond(
            highlight,
            f"0 12px 28px {ACCENT_SOFT}",
            "0 6px 18px rgba(0,0,0,0.12)",
        ),
        transition="all 0.25s ease",
        _hover={
            "transform": "translateY(-4px)",
            "borderColor": ACCENT,
            "boxShadow": f"0 14px 32px {ACCENT_SOFT}",
        },
        height="100%",
    )


def terminology_page() -> rx.Component:
    """Explain key Xian terms and their relationship."""
    foundation = _term_card(
        "Xian Technology Foundation",
        "An independent group advancing the Xian Technology stack, led by one of the three core developers; separate from the live Xian Network.",
        highlight=True,
    )
    technology = _term_card(
        "Xian Technology",
        "The stack combining CometBFT consensus, a custom Python ABCI, the Python contracting engine, and Python tooling to run robust blockchain networks.",
    )
    network = _term_card(
        "Xian Network",
        "A production blockchain demonstrating the Xian Technology stack in real-world use.",
    )

    connectors = _connectors_svg()

    foundation_node = rx.box(
        foundation,
        style={
            "gridColumn": "1",
            "gridRow": "1",
            MD_MEDIA: {"gridColumn": "2", "gridRow": "1"},
        },
    )
    technology_node = rx.box(
        technology,
        style={
            "gridColumn": "1",
            "gridRow": "2",
            MD_MEDIA: {"gridColumn": "1", "gridRow": "2"},
        },
    )
    network_node = rx.box(
        network,
        style={
            "gridColumn": "1",
            "gridRow": "3",
            MD_MEDIA: {"gridColumn": "3", "gridRow": "2"},
        },
    )

    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("TERMINOLOGY", size="2", letter_spacing="0.18em", color=ACCENT, weight="medium"),
                    padding="0.6rem 1.1rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="10px",
                ),
                rx.heading(
                    "Who is who in Xian",
                    size="8",
                    color=TEXT_PRIMARY,
                    weight="bold",
                    line_height="1.2",
                ),
                rx.text(
                    "Keep the distinctions clear: the technology stack, the foundation stewarding it, and the production network that proves it works.",
                    size="4",
                    color=TEXT_MUTED,
                    max_width="860px",
                    line_height="1.7",
                ),
                spacing="5",
                align_items="start",
            ),
            style={"paddingBottom": "3rem"},
        ),
        section(
            rx.vstack(
                rx.box(
                    connectors,
                    rx.box(
                        foundation_node,
                        technology_node,
                        network_node,
                        display="grid",
                        gap="1.5rem",
                        align_items="start",
                        position="relative",
                        z_index="1",
                        style={
                            "gridTemplateColumns": "1fr",
                            "gridTemplateRows": "repeat(3, auto)",
                            MD_MEDIA: {
                                "gridTemplateColumns": "repeat(3, minmax(0, 1fr))",
                                "gridTemplateRows": "repeat(2, auto)",
                            },
                        },
                    ),
                    position="relative",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="20px",
                    padding="2rem",
                    box_shadow="0 18px 42px rgba(0,0,0,0.18)",
                ),
                rx.vstack(
                    rx.text("At a glance", size="3", weight="bold", color=TEXT_PRIMARY),
                    rx.vstack(
                        _term_card(
                            "Xian Technology",
                            "CometBFT consensus + custom Python ABCI + Python contracting engine + tooling for running robust blockchain networks.",
                        ),
                        _term_card(
                            "Xian Technology Foundation",
                            "Independent group advancing the stack; not the same as the production Xian Network.",
                        ),
                        _term_card(
                            "Xian Network",
                            "Live blockchain that proves the stack in real-world deployments.",
                        ),
                        spacing="3",
                        align_items="start",
                    ),
                    spacing="3",
                    align_items="start",
                ),
                spacing="5",
                align_items="start",
            ),
            style={"paddingTop": "0"},
        ),
    )


__all__ = ["terminology_page"]
