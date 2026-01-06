import reflex as rx

from ..components.common import feature_card, page_layout, section, terminal_prompt
from ..data import CORE_COMPONENTS, NOTEWORTHY_QUOTES
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

QUOTE_GAP = "1.5rem"
QUOTE_GAP_HALF = "0.75rem"

QUOTE_MARQUEE_STYLE = """
@keyframes quote-marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(calc(-50% - var(--quote-gap-half))); }
}

@media (prefers-reduced-motion: reduce) {
  .quote-track {
    animation-play-state: paused !important;
  }
}
"""


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
                            rx.text("View on GitHub", size="3", weight="medium"),
                            rx.text("→", weight="bold", size="4"),
                            gap="0.75rem",
                            align_items="center",
                        ),
                        size="4",
                        background_color=ACCENT,
                        color=PRIMARY_BG,
                        border_radius="10px",
                        padding="1.25rem 2rem",
                        cursor="pointer",
                        _hover={
                            "backgroundColor": ACCENT_HOVER,
                            "boxShadow": f"0 12px 30px {ACCENT_SOFT}",
                        },
                        transition="all 0.2s ease",
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
        padding_top="8rem",
        padding_bottom="8rem",
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
                                    rx.icon(tag=item["icon"], size=28, color=ACCENT),
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
                            display="flex",
                            flex_direction="column",
                            background_image="linear-gradient(135deg, rgba(0, 179, 92, 0.08), rgba(0, 179, 92, 0))",
                            background_size="200% 200%",
                            background_position="left center",
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
        padding_top="3rem",
        padding_bottom="3rem",
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

    card_props = {
        "display": "flex",
        "flex_direction": "column",
        "align_self": "stretch",
    }

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
                    height="100%",
                    width="100%",
                    **card_props,
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
                    height="100%",
                    width="100%",
                    **card_props,
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
                    height="100%",
                    width="100%",
                    **card_props,
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
                    height="100%",
                    width="100%",
                    **card_props,
                ),
                columns={
                    "base": "repeat(1, minmax(0, 1fr))",
                    "md": "repeat(2, minmax(0, 1fr))",
                },
                rows="2",
                flow="row",
                gap="1.5rem",
                width="100%",
                align="stretch",
            ),
            spacing="6",
            align_items="start",
        ),
        padding_top="2rem",
        padding_bottom="3rem",
    )


def why_another_blockchain() -> rx.Component:
    """Explain why Xian exists."""
    return section(
        rx.grid(
            rx.vstack(
                rx.heading("Another Blockchain?", size="7", color=TEXT_PRIMARY, weight="bold"),
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
            width="100%",
        ),
        rx.box(
            rx.text(
                rx.fragment(
                    "A practical example of this shift is ",
                    rx.link(
                        "Google’s Universal Ledger (GCUL)",
                        href="https://cloud.google.com/application/web3/universal-ledger",
                        is_external=True,
                        color=ACCENT,
                    ),
                    ": a managed, programmable ledger on familiar cloud primitives. It uses Python as its programmable layer, underscoring the move toward mainstream tooling over blockchain-only stacks.",
                ),
                size="3",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            margin_top="1rem",
        ),
        rx.box(
            rx.text(
                "The Xian software stack aims to be a free, open alternative to offerings like GCUL—built on familiar technology, ready to run on-prem or in the cloud, and suited for your next distributed or decentralized project.",
                size="3",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            margin_top="0.5rem",
        ),
        padding_top="2rem",
        padding_bottom="3rem",
    )


    return section(
        rx.grid(
            rx.vstack(
                rx.heading("Why Python?", size="7", color=TEXT_PRIMARY, weight="bold"),
                rx.text(
                    "Python is one of the most used programming languages worldwide but is barely used in the blockchain world. At Xian, everything user-facing—including smart contracts—is Python-based, while we also ship JS tooling for web integrations. Python is slower than specialized smart-contract languages, but Xian still delivers strong performance, and the trade-off buys us the clarity, safety, and adoption of Python.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                rx.text(
                    "Take a look at current programming language trends and see how Python dominates.",
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
                        src="/github.png",
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
        padding_top="2rem",
        padding_bottom="3rem",
    )


def why_python() -> rx.Component:
    """Explain the Python-first choice."""
    def trend_image(src: str, alt: str, source: str, description: str) -> rx.Component:
        overlay_bg = rx.color_mode_cond(
            light="linear-gradient(180deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.82) 45%, rgba(255, 255, 255, 0.95) 100%)",
            dark="linear-gradient(180deg, rgba(10, 14, 20, 0) 0%, rgba(10, 14, 20, 0.78) 45%, rgba(10, 14, 20, 0.95) 100%)",
        )
        return rx.box(
            rx.image(
                src=src,
                alt=alt,
                width="100%",
                height=rx.breakpoints(initial="200px", md="220px", lg="240px"),
                object_fit="cover",
            ),
            rx.box(
                rx.text(
                    description,
                    size="2",
                    color=TEXT_PRIMARY,
                    line_height="1.6",
                ),
                class_name="trend-overlay",
                position="absolute",
                bottom="0",
                left="0",
                right="0",
                height="75%",
                padding="1rem",
                background=overlay_bg,
                transform="translateY(100%)",
                opacity="0",
                transition="transform 0.35s ease, opacity 0.35s ease",
                pointer_events="none",
                z_index="1",
                align_items="end",
                display="flex",
            ),
            rx.link(
                rx.badge(
                    "Source",
                    variant="soft",
                    color_scheme="green",
                    radius="medium",
                    size="2",
                ),
                href=source,
                is_external=True,
                position="absolute",
                bottom="0.33rem",
                right="0.33rem",
                on_click=rx.stop_propagation,
                z_index="2",
                _hover={"textDecoration": "none"},
            ),
            position="relative",
            width="100%",
            cursor="zoom-in",
            on_click=State.open_image_lightbox(src, alt),
            border_radius="12px",
            border=f"2px solid {BORDER_COLOR}",
            box_shadow=f"0 0 18px {ACCENT_SOFT}",
            overflow="hidden",
            style={
                "&:hover .trend-overlay": {
                    "transform": "translateY(0)",
                    "opacity": "1",
                }
            },
            class_name="trend-image",
        )

    return section(
        rx.grid(
            rx.vstack(
                rx.heading("Why Python?", size="7", color=TEXT_PRIMARY, weight="bold"),
                rx.text(
                    "Python is one of the most used programming languages worldwide but is barely used in the blockchain world. At Xian, everything user-facing—including smart contracts—is Python-based, while we also ship JS tooling for web integrations. Python is slower than specialized smart-contract languages, but Xian still delivers strong performance, and the trade-off buys us the clarity, safety, and adoption of Python.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                rx.text(
                    "Take a look at current programming language trends and see how Python dominates.",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                spacing="4",
                align_items="start",
            ),
            rx.box(
                rx.grid(
                    trend_image(
                        "/github.png",
                        "Programming languages on GitHub",
                        "https://github.blog/news-insights/octoverse/octoverse-2024",
                        "Top programming languages on GitHub, ranked by the number of distinct contributors per language.",
                    ),
                    trend_image(
                        "/languish.png",
                        "Programming language trends from Languish",
                        "https://tjpalmer.github.io/languish",
                        "Language trends based on the mean of GitHub stars and Stack Overflow question counts.",
                    ),
                    trend_image(
                        "/tiobe.png",
                        "TIOBE index ranking snapshot",
                        "https://www.tiobe.com/tiobe-index",
                        "The TIOBE index tracks language popularity using signals like global engineer counts, courses, and vendors.",
                    ),
                    columns={"base": "1fr", "md": "repeat(3, minmax(0, 1fr))"},
                    spacing="4",
                    width="100%",
                    align="stretch",
                ),
                display="flex",
                justify_content="center",
            ),
            template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
            gap="2rem",
        ),
        rx.button(
            on_click=State.close_image_lightbox,
            id="image-lightbox-close",
            display="none",
        ),
        rx.cond(
            State.image_lightbox_open,
            rx.center(
                rx.box(
                    rx.button(
                        rx.icon(tag="x", size=20),
                        on_click=State.close_image_lightbox,
                        size="2",
                        variant="ghost",
                        color=TEXT_MUTED,
                        position="absolute",
                        top="0.75rem",
                        right="0.75rem",
                        cursor="pointer",
                        _hover={"color": ACCENT},
                    ),
                    rx.image(
                        src=State.image_lightbox_src,
                        alt=State.image_lightbox_alt,
                        width="auto",
                        height="auto",
                        max_width="min(92vw, 1200px)",
                        max_height="82vh",
                        object_fit="contain",
                        border_radius="14px",
                        box_shadow=rx.color_mode_cond(
                            light="0 30px 120px rgba(15, 23, 42, 0.25)",
                            dark="0 30px 120px rgba(0, 0, 0, 0.8)",
                        ),
                    ),
                    on_click=rx.stop_propagation,
                    width="fit-content",
                    max_width="min(92vw, 1200px)",
                    display="inline-flex",
                    position="relative",
                ),
                position="fixed",
                top="0",
                left="0",
                width="100%",
                height="100vh",
                z_index="1002",
                background="rgba(6, 11, 17, 0.65)",
                backdrop_filter="blur(12px)",
                on_click=State.close_image_lightbox,
                id="image-lightbox-container",
            ),
            rx.box(),
        ),
        padding_top="2rem",
        padding_bottom="3rem",
    )


def noteworthy_quotes() -> rx.Component:
    """Showcase notable quotes about Python and technology."""
    quotes = NOTEWORTHY_QUOTES
    items = quotes if len(quotes) == 1 else quotes * 4
    card_width = rx.breakpoints(initial="260px", sm="300px", md="340px")
    animation_style = "quote-marquee 55s linear infinite" if len(quotes) > 1 else "none"
    fade_left = rx.color_mode_cond(
        light="linear-gradient(90deg, #ffffff 0%, rgba(255, 255, 255, 0) 100%)",
        dark="linear-gradient(90deg, #0a0e14 0%, rgba(10, 14, 20, 0) 100%)",
    )
    fade_right = rx.color_mode_cond(
        light="linear-gradient(270deg, #ffffff 0%, rgba(255, 255, 255, 0) 100%)",
        dark="linear-gradient(270deg, #0a0e14 0%, rgba(10, 14, 20, 0) 100%)",
    )

    def quote_card(item: dict[str, str]) -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.text("“", size="7", color=ACCENT, weight="bold", line_height="0.6"),
                rx.text(item["quote"], size="2", color=TEXT_MUTED, line_height="1.6", font_style="italic"),
                rx.hstack(
                    rx.spacer(),
                    rx.text("”", size="7", color=ACCENT, weight="bold", line_height="0.6"),
                    width="100%",
                ),
                rx.hstack(
                    rx.box(width="5px", height="5px", border_radius="50%", background=ACCENT),
                    rx.text(item["author"], size="1", color=TEXT_MUTED, weight="medium"),
                    rx.link(
                        "Source",
                        href=item["source"],
                        is_external=True,
                        color=ACCENT,
                        size="1",
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
            padding="1rem",
            background=rx.color_mode_cond(
                light="rgba(0, 179, 92, 0.14)",
                dark=ACCENT_SOFT,
            ),
            border_radius="12px",
            box_shadow=f"0 0 18px {ACCENT_SOFT}",
            width=card_width,
            min_width=card_width,
            flex="0 0 auto",
        )

    return section(
        rx.vstack(
            rx.heading("Quotes on Python", size="6", color=TEXT_PRIMARY, weight="bold"),
            rx.el.style(QUOTE_MARQUEE_STYLE),
            rx.box(
                rx.flex(
                    *[quote_card(item) for item in items],
                    class_name="quote-track",
                    direction="row",
                    gap=QUOTE_GAP,
                    align_items="stretch",
                    style={
                        "width": "max-content",
                        "animation": animation_style,
                        "animationPlayState": "running",
                        "--quote-gap": QUOTE_GAP,
                        "--quote-gap-half": QUOTE_GAP_HALF,
                    },
                    _hover={
                        "animationPlayState": "paused",
                    },
                ),
                rx.box(
                    position="absolute",
                    top="0",
                    bottom="0",
                    left="0",
                    width="2rem",
                    background=fade_left,
                    pointer_events="none",
                    z_index="1",
                ),
                rx.box(
                    position="absolute",
                    top="0",
                    bottom="0",
                    right="0",
                    width="2rem",
                    background=fade_right,
                    pointer_events="none",
                    z_index="1",
                ),
                width="100%",
                overflow="hidden",
                position="relative",
            ),
            spacing="4",
            align_items="start",
        ),
        padding_top="0rem",
        padding_bottom="3rem",
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
