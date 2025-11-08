import reflex as rx

from ..data import NAV_LINKS
from ..state import State
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_HOVER,
    ACCENT_SOFT,
    BORDER_BRIGHT,
    BORDER_COLOR,
    CODE_BG,
    MAX_CONTENT_WIDTH,
    PRIMARY_BG,
    SURFACE,
    SURFACE_BRIGHT,
    SURFACE_HOVER,
    TEXT_MUTED,
    TEXT_PRIMARY,
    TOP_GRADIENT,
)


def section(*children: rx.Component, **kwargs) -> rx.Component:
    """Wrap content in a centered section with generous spacing."""
    identifier = kwargs.pop("id", None)
    style = {
        "width": "100%",
        "maxWidth": MAX_CONTENT_WIDTH,
        "margin": "0 auto",
        "paddingLeft": "2rem",
        "paddingRight": "2rem",
        "paddingTop": "5rem",
        "paddingBottom": "5rem",
    }
    style.update(kwargs.pop("style", {}))
    return rx.box(*children, id=identifier, style=style, **kwargs)


def theme_toggle() -> rx.Component:
    """Theme toggle button with minimalist icons."""
    return rx.button(
        rx.cond(
            State.theme_mode == "dark",
            rx.text("◐", size="6", line_height="1"),
            rx.text("◑", size="6", line_height="1"),
        ),
        on_click=State.toggle_theme,
        variant="ghost",
        cursor="pointer",
        padding="0.5rem",
        background_color="transparent",
        color=TEXT_MUTED,
        _hover={
            "color": ACCENT,
            "transform": "rotate(180deg)",
        },
        style={
            "transition": "all 0.3s ease",
            "border": "none",
        },
    )


def nav_link(link: dict[str, str]) -> rx.Component:
    """Navigation link with consistent spacing."""
    return rx.link(
        rx.text(
            link["label"],
            size="3",
            weight="medium",
            color=TEXT_MUTED,
        ),
        href=link["href"],
        style={
            "padding": "0.75rem 1.25rem",
            "borderRadius": "8px",
            "transition": "all 0.2s ease",
        },
        _hover={
            "textDecoration": "none",
            "color": ACCENT,
            "backgroundColor": ACCENT_SOFT,
        },
    )


def nav_bar() -> rx.Component:
    """Professional navigation bar."""
    border_color = rx.cond(
        State.theme_mode == "light",
        "1px solid rgba(15, 23, 42, 0.08)",
        "1px solid rgba(255, 255, 255, 0.12)",
    )
    box_shadow = rx.cond(
        State.theme_mode == "light",
        "0 1px 20px rgba(15, 23, 42, 0.08)",
        "0 1px 20px rgba(0, 0, 0, 0.35)",
    )
    return rx.box(
        rx.box(
            rx.flex(
                rx.link(
                    rx.flex(
                        rx.image(
                            src="/xian.jpg",
                            alt="Xian Technology Logo",
                            width="3rem",
                            height="3rem",
                            border_radius="8px",
                            object_fit="cover",
                        ),
                        rx.vstack(
                            rx.text("Xian Technology", weight="bold", size="4", color=TEXT_PRIMARY),
                            rx.text("Python-native contracting", size="2", color=TEXT_MUTED),
                            align_items="start",
                            spacing="0",
                        ),
                        gap="1rem",
                        align_items="center",
                    ),
                    href="/",
                    _hover={"textDecoration": "none"},
                ),
                rx.flex(
                    rx.flex(
                        *[nav_link(link) for link in NAV_LINKS],
                        gap="0.5rem",
                        display={"base": "none", "md": "flex"},
                    ),
                    theme_toggle(),
                    gap="1rem",
                    align_items="center",
                ),
                align_items="center",
                justify="between",
                width="100%",
            ),
            max_width=MAX_CONTENT_WIDTH,
            margin="0 auto",
            padding="0 2rem",
        ),
        position="sticky",
        top="0",
        z_index="100",
        background_color="transparent",
        backdrop_filter="blur(20px)",
        border_bottom=border_color,
        box_shadow=box_shadow,
        padding="0.85rem 0",
        width="100%",
        style={"transition": "background-color 0.3s ease"},
    )


def code_block(code: str) -> rx.Component:
    """Syntax-highlight friendly code block."""
    return rx.box(
        rx.text(
            code,
            font_family="'SF Mono', 'Monaco', 'Menlo', 'Courier New', monospace",
            size="2",
            color=rx.cond(State.theme_mode == "light", "#1f2937", "#c9d1d9"),
            white_space="pre",
            line_height="1.6",
        ),
        background=CODE_BG,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="10px",
        padding="1.5rem",
        overflow_x="auto",
        width="100%",
        style={"transition": "all 0.3s ease"},
    )


def feature_card(title: str, description: str, icon: str) -> rx.Component:
    """Feature card with hover affordances."""
    return rx.box(
        rx.vstack(
            rx.text(icon, size="9", line_height="1"),
            rx.heading(title, size="5", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                description,
                size="3",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            spacing="5",
            align_items="start",
        ),
        padding="2.5rem",
        background=SURFACE,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="14px",
        transition="all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
        _hover={
            "borderColor": ACCENT,
            "backgroundColor": SURFACE_HOVER,
            "transform": "translateY(-8px)",
            "boxShadow": f"0 20px 40px {ACCENT_SOFT}",
        },
        height="100%",
    )


def terminal_prompt(command: str) -> rx.Component:
    """Terminal-style command prompt."""
    return rx.flex(
        rx.text("$", color=ACCENT, weight="bold", size="3"),
        rx.text(
            command,
            color=TEXT_PRIMARY,
            size="3",
            font_family="'SF Mono', 'Monaco', monospace",
        ),
        gap="1rem",
        padding="1rem 1.5rem",
        background=CODE_BG,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="8px",
        align_items="center",
        width="100%",
    )


def footer() -> rx.Component:
    """Professional footer with proper spacing."""
    return rx.box(
        rx.box(
            rx.vstack(
                rx.flex(
                    rx.vstack(
                        rx.text("Xian Technology Foundation", size="4", weight="bold", color=TEXT_PRIMARY),
                        rx.text("Python-native blockchain infrastructure", size="3", color=TEXT_MUTED, line_height="1.6"),
                        spacing="2",
                        align_items="start",
                    ),
                    rx.vstack(
                        rx.text("Resources", size="3", weight="bold", color=TEXT_PRIMARY),
                        rx.vstack(
                            rx.link("Documentation", href="https://xian.org", is_external=True, color=TEXT_MUTED, size="3"),
                            rx.link("GitHub", href="https://github.com/xian-network", is_external=True, color=TEXT_MUTED, size="3"),
                            rx.link("Community", href="/community", color=TEXT_MUTED, size="3"),
                            spacing="3",
                            align_items="start",
                        ),
                        spacing="3",
                        align_items="start",
                    ),
                    rx.vstack(
                        rx.text("Contact", size="3", weight="bold", color=TEXT_PRIMARY),
                        rx.link("foundation@xian.technology", href="mailto:foundation@xian.technology", color=TEXT_MUTED, size="3"),
                        spacing="3",
                        align_items="start",
                    ),
                    justify="between",
                    width="100%",
                    direction={"base": "column", "md": "row"},
                    gap="4rem",
                    align_items={"base": "start", "md": "start"},
                ),
                rx.box(
                    rx.text(
                        "© 2025 Xian Technology Foundation. Built for the Xian Network community.",
                        size="2",
                        color=TEXT_MUTED,
                        text_align="center",
                    ),
                    padding_top="3rem",
                    border_top=f"1px solid {BORDER_COLOR}",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
            max_width=MAX_CONTENT_WIDTH,
            margin="0 auto",
            padding="4rem 2rem",
        ),
        background_color=CODE_BG,
        width="100%",
        style={"transition": "background-color 0.3s ease"},
    )


def page_layout(*children: rx.Component) -> rx.Component:
    """Base layout wrapper for all pages."""
    gradient_overlay = rx.box(
        background=TOP_GRADIENT,
        position="absolute",
        top="0",
        left="0",
        right="0",
        height="520px",
        pointer_events="none",
        z_index="0",
    )
    return rx.box(
        gradient_overlay,
        rx.box(
            nav_bar(),
            rx.box(
                *children,
                min_height="calc(100vh - 200px)",
            ),
            footer(),
            position="relative",
            z_index="1",
        ),
        position="relative",
        background=PRIMARY_BG,
        color=TEXT_PRIMARY,
        min_height="100vh",
        style={"transition": "background-color 0.3s ease, color 0.3s ease"},
    )


__all__ = [
    "code_block",
    "feature_card",
    "nav_bar",
    "nav_link",
    "page_layout",
    "section",
    "terminal_prompt",
    "theme_toggle",
]
