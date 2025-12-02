import reflex as rx

from ..components.common import feature_card, page_layout, section, terminal_prompt
from ..data import STACK_COMPONENTS
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_HOVER,
    ACCENT_SOFT,
    BORDER_COLOR,
    CODE_BG,
    PRIMARY_BG,
    SURFACE,
    SURFACE_BRIGHT,
    SURFACE_HOVER,
    TEXT_MUTED,
    TEXT_PRIMARY,
)


def hero_section() -> rx.Component:
    """Hero section for the landing page."""
    return section(
        rx.vstack(
            rx.box(
                rx.text(
                    "XIAN_TECHNOLOGY_FOUNDATION",
                    size="2",
                    letter_spacing="0.15em",
                    color=ACCENT,
                    weight="medium",
                ),
                padding="0.625rem 1.25rem",
                background=ACCENT_SOFT,
                border=f"1px solid {ACCENT_GLOW}",
                border_radius="8px",
            ),
            rx.heading(
                "Python-Native Contracting on a CometBFT Backbone.",
                size="9",
                line_height="1.1",
                color=TEXT_PRIMARY,
                max_width="900px",
                text_align="center",
                weight="bold",
            ),
            rx.text(
                "Xian is a CometBFT-backed blockchain with a pure Python contracting engine. "
                "Write native Python contracts—no transpilers—while combining fast consensus with the simplicity and power of Python.",
                size="5",
                color=TEXT_MUTED,
                max_width="700px",
                text_align="center",
                line_height="1.7",
            ),
            rx.flex(
                rx.link(
                    rx.button(
                        rx.flex(
                            rx.text("Explore Technology", size="3", weight="medium"),
                            rx.text("→", weight="bold", size="4"),
                            gap="0.75rem",
                            align_items="center",
                        ),
                        size="4",
                        background_color=ACCENT,
                        color=PRIMARY_BG,
                        border_radius="10px",
                        cursor="pointer",
                        padding="1.25rem 2rem",
                        _hover={
                            "backgroundColor": ACCENT_HOVER,
                            "transform": "translateY(-2px)",
                        },
                        style={"transition": "all 0.2s ease"},
                    ),
                    href="/technology",
                ),
                rx.link(
                    rx.button(
                        "View on GitHub",
                        variant="outline",
                        size="4",
                        border_color=BORDER_COLOR,
                        color=TEXT_PRIMARY,
                        background_color="transparent",
                        border_radius="10px",
                        padding="1.25rem 2rem",
                        cursor="pointer",
                        _hover={
                            "backgroundColor": SURFACE,
                            "borderColor": TEXT_MUTED,
                        },
                        style={"transition": "all 0.2s ease"},
                    ),
                    href="https://github.com/xian-network",
                    is_external=True,
                ),
                gap="1.5rem",
                wrap="wrap",
                justify="center",
            ),
            spacing="8",
            align_items="center",
            width="100%",
        ),
        style={"paddingTop": "8rem", "paddingBottom": "8rem"},
    )


def stack_overview() -> rx.Component:
    """Stack overview grid."""
    return section(
        rx.vstack(
            rx.text(
                "A streamlined stack that pairs CometBFT consensus with a pure Python execution layer and tooling.",
                size="4",
                color=TEXT_MUTED,
                max_width="820px",
                line_height="1.7",
                text_align="center",
            ),
            rx.flex(
                *[
                    rx.link(
                        rx.box(
                            rx.vstack(
                                rx.text(item["icon"], size="8", line_height="1"),
                                rx.heading(item["title"], size="5", weight="bold", color=TEXT_PRIMARY),
                                rx.text(item["description"], size="3", color=TEXT_MUTED, line_height="1.7"),
                                spacing="3",
                                align_items="start",
                            ),
                            padding="2.5rem",
                            background=SURFACE,
                            border=f"1px solid {BORDER_COLOR}",
                            border_radius="14px",
                            transition="background-position 0.4s ease, box-shadow 0.3s ease, border-color 0.2s ease",
                            height="100%",
                            min_width="260px",
                            max_width="260px",
                            style={
                                "backgroundImage": "linear-gradient(135deg, rgba(0, 179, 92, 0.08), rgba(0, 179, 92, 0))",
                                "backgroundSize": "200% 200%",
                                "backgroundPosition": "left center",
                            },
                            _hover={
                                "borderColor": ACCENT,
                                "backgroundColor": SURFACE_HOVER,
                                "boxShadow": f"0 18px 32px {ACCENT_SOFT}",
                                "backgroundPosition": "right center",
                            },
                        ),
                        href=item["href"],
                        _hover={"textDecoration": "none"},
                    )
                    for item in STACK_COMPONENTS
                ],
                spacing="4",
                width="100%",
                wrap="nowrap",
                overflow_x="auto",
            ),
            spacing="6",
            align_items="center",
        ),
        style={"paddingTop": "3rem", "paddingBottom": "3rem"},
    )


def stats_grid() -> rx.Component:
    """Stats snapshot for the foundation."""
    return section(
        rx.grid(
            rx.box(
                rx.vstack(
                    rx.text("100%", size="9", weight="bold", color=ACCENT, line_height="1"),
                    rx.text("Python", size="5", weight="bold", color=TEXT_PRIMARY),
                    rx.text(
                        "Pure Python contracts, tooling, and node",
                        size="3",
                        color=TEXT_MUTED,
                        text_align="center",
                        line_height="1.6",
                    ),
                    spacing="3",
                    align_items="center",
                ),
                padding="2.5rem",
                background=CODE_BG,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
                text_align="center",
            ),
            rx.box(
                rx.vstack(
                    rx.text("Live Mainnet", size="5", weight="bold", color=TEXT_PRIMARY),
                    rx.text(
                        "Xian Network showcases production deployments today",
                        size="3",
                        color=TEXT_MUTED,
                        text_align="center",
                        line_height="1.6",
                    ),
                    spacing="3",
                    align_items="center",
                ),
                padding="2.5rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
                text_align="center",
            ),
            rx.box(
                rx.vstack(
                    rx.text("Contributor-First", size="5", weight="bold", color=TEXT_PRIMARY),
                    rx.text(
                        "Pathways for researchers, builders, and operators",
                        size="3",
                        color=TEXT_MUTED,
                        text_align="center",
                        line_height="1.6",
                    ),
                    spacing="3",
                    align_items="center",
                ),
                padding="2.5rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
                text_align="center",
            ),
            template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
            gap="2rem",
        )
    )


def quick_features() -> rx.Component:
    """Feature callouts."""
    return section(
        rx.vstack(
            rx.heading("Why Xian Technology", size="7", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                "A foundation dedicated to advancing Python-native blockchain infrastructure.",
                size="4",
                color=TEXT_MUTED,
                max_width="720px",
                line_height="1.7",
            ),
            rx.grid(
                feature_card(
                    "Deterministic Python",
                    "Pure Python smart contracts with predictable execution and strong safety rails.",
                    "🧠",
                ),
                feature_card(
                    "Production Network",
                    "Xian Network acts as a live showcase for tooling, governance, and upgrades.",
                    "🚀",
                ),
                feature_card(
                    "Community of Builders",
                    "Tightly aligned researchers, operators, and engineers iterating in the open.",
                    "🤝",
                ),
                template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                gap="2rem",
            ),
            spacing="6",
            align_items="start",
        )
    )


def cta_section() -> rx.Component:
    """Call to action with onboarding commands."""
    return section(
        rx.box(
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.heading("Ready to build?", size="7", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Install the SDK, scaffold contracts, and deploy to the Xian Network mainnet.",
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
                        spacing="6",
                        align_items="start",
                    ),
                    padding="3rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("Foundation Support", size="6", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Need architecture guidance or audits? Partner with our research and builder guilds.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        rx.link(
                            rx.button(
                                "Request a Brief",
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
                        spacing="5",
                        align_items="start",
                    ),
                    padding="3rem",
                    background=SURFACE_BRIGHT,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
                gap="2rem",
            )
        )
    )


def home_page() -> rx.Component:
    """Landing page entry point."""
    return page_layout(
        hero_section(),
        stack_overview(),
        stats_grid(),
        quick_features(),
        cta_section(),
    )


__all__ = ["home_page"]
