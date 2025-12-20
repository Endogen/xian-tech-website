import reflex as rx

from ..components.common import feature_card, page_layout, section, terminal_prompt
from ..data import CORE_COMPONENTS
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
                    href="https://github.com/xian-technology",
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
            rx.grid(
                *[
                    rx.link(
                        rx.box(
                            rx.vstack(
                                rx.flex(
                                    rx.text(item["icon"], size="7", line_height="1"),
                                    rx.heading(item["title"], size="5", weight="bold", color=TEXT_PRIMARY),
                                    direction={"base": "row", "lg": "column"},
                                    align={"base": "center", "lg": "start"},
                                    spacing="3",
                                ),
                                rx.text(item["description"], size="3", color=TEXT_MUTED, line_height="1.7"),
                                spacing="3",
                                align_items="start",
                            ),
                            padding="2rem",
                            background=SURFACE,
                            border=f"1px solid {BORDER_COLOR}",
                            border_radius="14px",
                            transition="background-position 0.4s ease, box-shadow 0.3s ease, border-color 0.2s ease",
                            height="100%",
                            width="100%",
                            style={
                                "display": "flex",
                                "flexDirection": "column",
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
                    for item in CORE_COMPONENTS
                ],
                columns={
                    "base": "repeat(1, minmax(0, 1fr))",
                    "md": "repeat(2, minmax(0, 1fr))",
                    "lg": "repeat(4, minmax(0, 1fr))",
                },
                spacing="4",
                width="100%",
                align="stretch",
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
                "The Xian Technology Foundation advances the technology stack behind Xian to keep it simple, powerful, and production-ready.",
                size="4",
                color=TEXT_MUTED,
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
                        bullet("Smooth setup for local nodes and multi-node environments."),
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
                        bullet("Explain how the stack works and how to build on it and interface with it."),
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
                    "Blockchains are shifting away from bespoke, blockchain-only stacks toward ones built on familiar technology—avoiding niche languages and tools you never see outside crypto. The goal is a universal stack that plugs into existing infrastructure and is straightforward to deploy and operate. Our aim is to to deliver a simple yet powerful software stack that companies and communities can run themselves when they want their own decentralized ledger.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                spacing="4",
                align_items="start",
            ),
            template_columns={"base": "1fr", "md": "repeat(1, 1fr)"},
            gap="1.5rem",
        ),
        style={"paddingTop": "2rem", "paddingBottom": "3rem"},
    )


    return section(
        rx.grid(
            rx.vstack(
                rx.heading("Why use Python?", size="7", color=TEXT_PRIMARY, weight="bold"),
                rx.text(
                    "Python is one of the most used programming languages worldwide but is barely used in the blockchain world. At Xian, everything user-facing—including smart contracts—is Python-based, while we also ship JS tooling for web integrations.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                rx.text(
                    rx.fragment(
                        "Explore current programming language trends over at ",
                        rx.link(
                            "Languish",
                            href="https://tjpalmer.github.io/languish",
                            is_external=True,
                            color=ACCENT,
                        ),
                        " for a broader snapshot of the ecosystem.",
                    ),
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                spacing="4",
                align_items="start",
            ),
            rx.box(
                rx.box(
                    rx.image(
                        src="/languages.png",
                        alt="Programming languages",
                        width="100%",
                        border_radius="12px",
                        object_fit="cover",
                        box_shadow=f"0 0 18px {ACCENT_SOFT}",
                    ),
                    rx.link(
                        rx.badge(
                            "Source",
                            variant="soft",
                            color_scheme="green",
                            radius="medium",
                            size="2",
                        ),
                        href="https://github.blog/news-insights/octoverse/octoverse-2024",
                        is_external=True,
                        position="absolute",
                        bottom="0.33rem",
                        right="0.33rem",
                        _hover={"textDecoration": "none"},
                    ),
                    position="relative",
                    width="100%",
                ),
                display="flex",
                justify_content="center",
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
                    "Python is one of the most used programming languages worldwide but is barely used in the blockchain world. At Xian, everything user-facing—including smart contracts—is Python-based, while we also ship JS tooling for web integrations.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                rx.text(
                    rx.fragment(
                        "Explore current programming language trends over at ",
                        rx.link(
                            "Languish",
                            href="https://tjpalmer.github.io/languish",
                            is_external=True,
                            color=ACCENT,
                        ),
                        " for a broader snapshot of the ecosystem.",
                    ),
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                spacing="4",
                align_items="start",
            ),
            rx.box(
                rx.box(
                    rx.image(
                        src="/languages.png",
                        alt="Programming languages",
                        width="100%",
                        border_radius="12px",
                        object_fit="cover",
                        box_shadow=f"0 0 18px {ACCENT_SOFT}",
                    ),
                    rx.link(
                        rx.badge(
                            "Source",
                            variant="soft",
                            color_scheme="green",
                            radius="medium",
                            size="2",
                        ),
                        href="https://github.blog/news-insights/octoverse/octoverse-2024",
                        is_external=True,
                        position="absolute",
                        bottom="0.33rem",
                        right="0.33rem",
                        _hover={"textDecoration": "none"},
                    ),
                    position="relative",
                    width="100%",
                ),
                display="flex",
                justify_content="center",
            ),
            template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
            gap="2rem",
        ),
        style={"paddingTop": "2rem", "paddingBottom": "3rem"},
    )


def noteworthy_quotes() -> rx.Component:
    """Showcase notable quotes about Python and technology."""
    quotes = [
        {
            "quote": (
                "Mastery of technology must infuse everything we do. Not just in our labs, but in the field, in our tradecraft, "
                "and even more importantly, in the mindset of every officer. We must be as comfortable with lines of code as we are "
                "with human sources, as fluent in Python as we are in multiple languages."
            ),
            "author": "Blaise Metreweli — Head of MI6",
            "source": "https://www.theguardian.com/uk-news/2025/dec/15/new-mi6-head-blaise-metreweli-speech-russia-threat",
        },
        {
            "quote": (
                "Python is now the most used language on GitHub as global open source activity continues to extend beyond traditional "
                "software development. We saw Python emerge for the first time as the most used language on GitHub (more on that later). "
                "Python is used heavily across machine learning, data science, scientific computing, hobbyist, and home automation fields among others."
            ),
            "author": "GitHub Staff — Octoverse 2024",
            "source": "https://github.blog/news-insights/octoverse/octoverse-2024/",
        },
        {
            "quote": (
                "Python is approachable because it's designed for developers who are learning, tinkering, and exploring. Python's future remains bright "
                "because its values align with how developers actually learn and build: readability, approachability, stability, and a touch of irreverence."
            ),
            "author": "Guido van Rossum — Python Creator",
            "source": "https://github.blog/developer-skills/programming-languages-and-frameworks/why-developers-still-flock-to-python-guido-van-rossum-on-readability-ai-and-the-future-of-programming",
        },
    ]

    def quote_card(item: dict[str, str]) -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.text("“", size="9", color=ACCENT, weight="bold", line_height="0.6"),
                rx.text(item["quote"], size="4", color=TEXT_MUTED, line_height="1.8", style={"fontStyle": "italic"}),
                rx.hstack(
                    rx.spacer(),
                    rx.text("”", size="9", color=ACCENT, weight="bold", line_height="0.6"),
                    width="100%",
                ),
                rx.hstack(
                    rx.box(width="6px", height="6px", border_radius="50%", background=ACCENT),
                    rx.text(item["author"], size="2", color=TEXT_MUTED, weight="medium"),
                    rx.link(
                        "Source",
                        href=item["source"],
                        is_external=True,
                        color=ACCENT,
                        size="2",
                        _hover={"textDecoration": "none"},
                    ),
                    gap="0.6rem",
                    align_items="center",
                    wrap="wrap",
                ),
                spacing="1",
                align_items="start",
                width="100%",
            ),
            padding="1.25rem",
            background=rx.cond(
                State.theme_mode == "light",
                "rgba(0, 179, 92, 0.14)",
                ACCENT_SOFT,
            ),
            border_radius="14px",
            box_shadow=f"0 0 18px {ACCENT_SOFT}",
            width="100%",
        )

    return section(
        rx.vstack(
            rx.heading("Noteworthy quotes", size="6", color=TEXT_PRIMARY, weight="bold"),
            rx.grid(
                *[quote_card(item) for item in quotes],
                template_columns={"initial": "1fr"},
                gap="1.5rem",
                width="100%",
            ),
            spacing="4",
            align_items="start",
        ),
        style={"paddingTop": "0rem", "paddingBottom": "3rem"},
    )


def home_page() -> rx.Component:
    """Landing page entry point."""
    return page_layout(
        hero_section(),
        stack_overview(),
        mission_section(),
        why_another_blockchain(),
        why_python(),
        noteworthy_quotes(),
    )


__all__ = ["home_page"]
