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
    PRIMARY_BG,
    SURFACE,
    TEXT_MUTED,
    TEXT_PRIMARY,
)

# Solid (non-transparent) background colors for cards
LIGHT_CARD_BG = "#f8f9fa"
LIGHT_CARD_BG_BRIGHT = "#ffffff"
DARK_CARD_BG = "#0f141c"
DARK_CARD_BG_BRIGHT = "#192330"

HISTORY_EVENTS = [
    {
        "date": "2021",
        "title": "Foundation charter drafted",
        "detail": "Defined stewardship boundaries and the mission to keep the Xian stack simple, durable, and production-ready.",
    },
    {
        "date": "2022",
        "title": "Architecture aligned",
        "detail": "CometBFT consensus paired with a Python ABCI and contracting engine to deliver deterministic execution.",
    },
    {
        "date": "2023",
        "title": "Contracting engine hardened",
        "detail": "Focused on auditability, predictable upgrades, and tooling that keeps contract behavior consistent.",
    },
    {
        "date": "2024",
        "title": "Tooling & services expanded",
        "detail": "CLI, SDKs, and the Blockchain Data Service matured to support developers and operators.",
    },
    {
        "date": "2025",
        "title": "Network validates the stack",
        "detail": "Xian Network demonstrates the technology in a live environment with real-world usage.",
    },
]


def _history_item(event: dict[str, str]) -> rx.Component:
    """Single timeline entry with expandable detail."""
    hover_shadow = rx.color_mode_cond(
        light="0 12px 28px rgba(80, 177, 101, 0.16)",
        dark="0 12px 28px rgba(0, 255, 136, 0.18)",
    )
    marker_glow = rx.color_mode_cond(
        light="0 0 0 6px rgba(80, 177, 101, 0.12)",
        dark="0 0 0 6px rgba(0, 255, 136, 0.16)",
    )

    return rx.box(
        rx.box(
            width="12px",
            height="12px",
            border_radius="999px",
            background=PRIMARY_BG,
            border_width="2px",
            border_style="solid",
            border_color=ACCENT,
            box_shadow=marker_glow,
            position="absolute",
            left="-2.1rem",
            top="50%",
            transform="translateY(-50%)",
            z_index="1",
        ),
        rx.box(
            rx.accordion.root(
                rx.accordion.item(
                    rx.accordion.header(
                        rx.accordion.trigger(
                            rx.hstack(
                                rx.hstack(
                                    rx.text(
                                        event["date"],
                                        size="4",
                                        weight="bold",
                                        color=ACCENT,
                                        letter_spacing="0.08em",
                                    ),
                                    rx.text(
                                        event["title"],
                                        size="4",
                                        weight="bold",
                                        color=TEXT_PRIMARY,
                                    ),
                                    spacing="3",
                                    align_items="baseline",
                                ),
                                rx.accordion.icon(color=TEXT_MUTED),
                                justify="between",
                                align_items="center",
                                width="100%",
                            ),
                            padding="1.5rem",
                            background="transparent",
                            box_shadow="none",
                            color=TEXT_PRIMARY,
                            cursor="pointer",
                            width="100%",
                            _hover={"backgroundColor": "transparent"},
                        )
                    ),
                    rx.accordion.content(
                        rx.box(
                            rx.text(
                                event["detail"],
                                size="3",
                                color=TEXT_MUTED,
                                line_height="1.7",
                            ),
                            padding_left="1.5rem",
                            padding_right="1.5rem",
                            padding_bottom="1.5rem",
                        ),
                        color=TEXT_MUTED,
                    ),
                    value=f"history-{event['date']}",
                    width="100%",
                ),
                type="single",
                collapsible=True,
                variant="ghost",
                width="100%",
            ),
            background=SURFACE,
            border_radius="14px",
            border_width="1px",
            border_style="solid",
            border_color=BORDER_COLOR,
            transition="all 0.2s ease",
            _hover={
                "borderColor": ACCENT,
                "boxShadow": hover_shadow,
            },
        ),
        position="relative",
        width="100%",
    )


def history_section() -> rx.Component:
    """Timeline of notable foundation milestones."""
    return section(
        rx.vstack(
            rx.heading("History", size="7", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                "Notable milestones that mark the evolution of the foundation and the Xian stack.",
                size="4",
                color=TEXT_MUTED,
                line_height="1.7",
                max_width="900px",
            ),
            rx.box(
                rx.box(
                    width="2px",
                    background=ACCENT_GLOW,
                    border_radius="999px",
                    position="absolute",
                    top="0",
                    bottom="0",
                    left="1.25rem",
                ),
                rx.vstack(
                    *[_history_item(event) for event in HISTORY_EVENTS],
                    spacing="5",
                    align_items="stretch",
                    width="100%",
                ),
                position="relative",
                padding_left="3rem",
                width="100%",
            ),
            spacing="6",
            align_items="start",
            width="100%",
        ),
        padding_top="3rem",
    )


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
            stroke=rx.color_mode_cond(light=stroke_light, dark=stroke_dark),
            stroke_width="2",
            fill="none",
            stroke_linecap="round",
        )

    def make_glow_path(d: str) -> rx.Component:
        return rx.el.svg.path(
            d=d,
            stroke=rx.color_mode_cond(light=glow_light, dark=glow_dark),
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
        display=rx.breakpoints(initial="none", lg="block"),
    )


def _term_card(title: str, body: str, highlight: bool = False) -> rx.Component:
    """Reusable card for terminology entries."""
    # Use solid backgrounds (non-transparent)
    card_bg = rx.color_mode_cond(
        light=LIGHT_CARD_BG_BRIGHT if highlight else LIGHT_CARD_BG,
        dark=DARK_CARD_BG_BRIGHT if highlight else DARK_CARD_BG,
    )
    return rx.box(
        rx.vstack(
            rx.text(title, size="4", weight="bold", color=TEXT_PRIMARY),
            rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
            spacing="3",
            align_items="start",
        ),
        padding="1.75rem",
        background=card_bg,
        border=f"1px solid {ACCENT_GLOW}" if highlight else f"1px solid {BORDER_COLOR}",
        border_radius="16px",
        box_shadow=rx.cond(
            highlight,
            f"0 12px 28px {ACCENT_SOFT}",
            "0 6px 18px rgba(0,0,0,0.12)",
        ),
        transition="all 0.25s ease",
        _hover={
            "borderColor": ACCENT,
            "boxShadow": f"0 14px 32px {ACCENT_SOFT}",
        },
        height="100%",
    )


def about_page() -> rx.Component:
    """Explain key Xian terms and their relationship."""
    foundation = _term_card(
        "Xian Foundation",
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
        grid_column=rx.breakpoints(initial="1", lg="2"),
        grid_row=rx.breakpoints(initial="1", lg="1"),
    )
    technology_node = rx.box(
        technology,
        grid_column=rx.breakpoints(initial="1", lg="1"),
        grid_row=rx.breakpoints(initial="2", lg="2"),
    )
    network_node = rx.box(
        network,
        grid_column=rx.breakpoints(initial="1", lg="3"),
        grid_row=rx.breakpoints(initial="3", lg="2"),
    )

    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("ABOUT", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "About us",
                    size="8",
                    color=TEXT_PRIMARY,
                    weight="bold",
                    line_height="1.2",
                ),
                rx.text(
                    "This page will outline the foundation's mission, focus areas, and the role we play in the Xian ecosystem.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    max_width="900px",
                ),
            ),
            padding_bottom="3rem",
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
                        grid_template_columns=rx.breakpoints(
                            initial="1fr",
                            lg="repeat(3, minmax(0, 1fr))",
                        ),
                        grid_template_rows=rx.breakpoints(
                            initial="repeat(3, auto)",
                            lg="repeat(2, auto)",
                        ),
                    ),
                    position="relative",
                    width="100%",
                ),
                align_items="start",
            ),
            padding_top="0",
        ),
        history_section(),
    )


__all__ = ["about_page"]
