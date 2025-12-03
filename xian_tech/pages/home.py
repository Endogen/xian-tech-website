import reflex as rx

from ..components.common import feature_card, page_layout, section, terminal_prompt
from ..data import STACK_COMPONENTS
from ..state import State
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


def mission_section() -> rx.Component:
    """Mission overview for the foundation."""
    def bullet(text: str) -> rx.Component:
        return rx.flex(
            rx.text("→", color=ACCENT, size="3"),
            rx.text(text, size="3", color=TEXT_MUTED, line_height="1.6"),
            gap="0.65rem",
            align_items="flex-start",
        )

    return section(
        rx.vstack(
            rx.heading("Our Mission", size="7", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                "The Xian Technology Foundation advances the Xian blockchain stack—pairing CometBFT consensus with a pure Python contracting engine—to keep it simple, powerful, and production-ready.",
                size="4",
                color=TEXT_MUTED,
                max_width="860px",
                line_height="1.7",
            ),
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.heading("Keep it simple & powerful", size="5", color=TEXT_PRIMARY, weight="bold"),
                        bullet("Keep ABCI and the contracting engine clean, deterministic, and auditable."),
                        bullet("Maintain compatibility with new Python interpreters without breaking contracts."),
                        spacing="3",
                        align_items="start",
                    ),
                    padding="2.5rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("Extend functionality", size="5", color=TEXT_PRIMARY, weight="bold"),
                        bullet("Evolve node features and operational insight."),
                        bullet("Ship and maintain high-value system contracts."),
                        bullet("Deliver tools (CLI, SDKs, services) to interface easily with Xian."),
                        spacing="3",
                        align_items="start",
                    ),
                    padding="2.5rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("Make networks easy to run", size="5", color=TEXT_PRIMARY, weight="bold"),
                        bullet("Smooth setup for local nodes and multi-node devnets."),
                        bullet("Documented patterns for distributed production networks."),
                        spacing="3",
                        align_items="start",
                    ),
                    padding="2.5rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("Document everything", size="5", color=TEXT_PRIMARY, weight="bold"),
                        bullet("Explain how the stack works and how to build on it."),
                        bullet("Keep upgrade paths, examples, and reference guides current."),
                        spacing="3",
                        align_items="start",
                    ),
                    padding="2.5rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
                gap="1.5rem",
                width="100%",
            ),
            spacing="6",
            align_items="start",
        ),
        style={"paddingTop": "2rem", "paddingBottom": "3rem"},
    )


def why_another_blockchain() -> rx.Component:
    """Explain why Xian exists."""
    return section(
        rx.grid(
            rx.vstack(
                rx.heading("Why Another Blockchain?", size="7", color=TEXT_PRIMARY, weight="bold"),
                rx.text(
                    "The industry is shifting from specialized, hard-to-extend stacks to general-purpose blockchains that feel familiar, are hackable, and integrate cleanly with existing infrastructure.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                rx.text(
                    "Xian embraces that shift: CometBFT for consensus, pure Python for contracts, and tooling that fits modern workflows—similar to how Google’s GCUL leans on familiar cloud-native primitives and a single API surface.",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                rx.box(
                    rx.vstack(
                        rx.text("“", size="9", color=ACCENT, weight="bold", line_height="0.6"),
                        rx.text(
                            "Google Cloud Universal Ledger (GCUL) is a new platform to create innovative payments services and financial markets products... provided as a service and accessible through a single API.",
                            size="4",
                            color=TEXT_MUTED,
                            line_height="1.8",
                            style={"fontStyle": "italic"},
                        ),
                        rx.hstack(
                            rx.spacer(),
                            rx.text("”", size="9", color=ACCENT, weight="bold", line_height="0.6"),
                            width="100%",
                        ),
                        spacing="1",
                        align_items="start",
                        width="100%",
                    ),
                    rx.link(
                        "Source: Google Cloud Universal Ledger",
                        href="https://cloud.google.com/application/web3/universal-ledger",
                        is_external=True,
                        color=ACCENT,
                        size="2",
                    ),
                    gap="1rem",
                    padding="1.5rem",
                    background=rx.cond(
                        State.theme_mode == "light",
                        "rgba(0, 179, 92, 0.14)",
                        ACCENT_SOFT,
                    ),
                    border_radius="14px",
                    box_shadow=f"0 0 18px {ACCENT_SOFT}",
                ),
                rx.box(
                    rx.heading("Why not just use GCUL?", size="5", color=TEXT_PRIMARY, weight="bold"),
                    rx.text(
                        "GCUL is a proprietary, Google-controlled platform delivered as a service. Xian is public and free software: run it on-prem, private, or public, with full control of your consensus, contracts, governance, fee structure, and data.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    spacing="3",
                    align_items="start",
                ),
                spacing="4",
                align_items="start",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("What this means for Xian", size="5", color=TEXT_PRIMARY, weight="bold"),
                    rx.vstack(
                        rx.flex(rx.text("→", color=ACCENT, size="3"), rx.text("Lower cognitive load: Python everywhere, no transpilers or DSLs.", size="3", color=TEXT_MUTED), gap="0.65rem"),
                        rx.flex(rx.text("→", color=ACCENT, size="3"), rx.text("Integration-first: SDKs and data services that drop into existing stacks.", size="3", color=TEXT_MUTED), gap="0.65rem"),
                        rx.flex(rx.text("→", color=ACCENT, size="3"), rx.text("Operational clarity: deterministic consensus, predictable metering, and documented patterns.", size="3", color=TEXT_MUTED), gap="0.65rem"),
                        rx.flex(rx.text("→", color=ACCENT, size="3"), rx.text("Evolvable: Python ABCI app and contracts that can be maintained and extended cleanly.", size="3", color=TEXT_MUTED), gap="0.65rem"),
                        spacing="3",
                        align_items="start",
                    ),
                    spacing="4",
                    align_items="start",
                ),
                padding="2.5rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
            ),
            template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
            gap="2rem",
        ),
        style={"paddingTop": "2rem", "paddingBottom": "3rem"},
    )


def why_python() -> rx.Component:
    """Explain the Python-first choice."""
    return section(
        rx.grid(
            rx.vstack(
                rx.heading("Why use Python?", size="7", color=TEXT_PRIMARY, weight="bold"),
                rx.text(
                    "Python is one of the most used programming languages worldwide but is barely used in the blockchain world. At Xian, everything user-facing—including smart contracts—is Python-based.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                spacing="4",
                align_items="start",
            ),
            rx.box(
                rx.image(
                    src="/languages.png",
                    alt="Programming languages",
                    width="100%",
                    max_width="520px",
                    border_radius="14px",
                    object_fit="cover",
                    box_shadow=f"0 0 18px {ACCENT_SOFT}",
                ),
                display="flex",
                justify_content="center",
            ),
            template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
            gap="2rem",
        ),
        style={"paddingTop": "2rem", "paddingBottom": "3rem"},
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
        mission_section(),
        why_another_blockchain(),
        why_python(),
        stats_grid(),
        quick_features(),
        cta_section(),
    )


__all__ = ["home_page"]
