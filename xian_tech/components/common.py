from typing import Any, Optional

import reflex as rx

from ..data import NAV_LINKS
from ..state import State
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
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
    chevron = link.get("children")
    return rx.link(
        rx.hstack(
            rx.text(
                link["label"],
                size="3",
                weight="medium",
                color=TEXT_MUTED,
            ),
            rx.cond(
                chevron,
                rx.text("▾", size="2", color=TEXT_MUTED, weight="bold"),
                rx.box(),
            ),
            align_items="center",
            gap="0.35rem",
        ),
        href=link["href"],
        style={
            "padding": "0.65rem 1rem",
            "borderRadius": "10px",
            "transition": "all 0.2s ease",
            "display": "inline-flex",
            "alignItems": "center",
            "gap": "0.35rem",
        },
        _hover={
            "textDecoration": "none",
            "color": ACCENT,
            "backgroundColor": ACCENT_SOFT,
        },
    )


def nav_item(link: dict[str, Any]) -> rx.Component:
    """Navigation item with hover tracking for mega menu."""
    has_children = bool(link.get("children"))
    return rx.box(
        nav_link(link),
        on_mouse_enter=State.set_nav_hover(link["label"]) if has_children else State.clear_nav_hover,
        on_focus=State.set_nav_hover(link["label"]) if has_children else State.clear_nav_hover,
        display="inline-flex",
    )


def submenu_children(label: str) -> rx.Component:
    """Render submenu content for a hovered label."""
    groups: list[rx.Component] = []
    for link in NAV_LINKS:
        children = link.get("children")
        if not children:
            continue
        groups.append(
            rx.cond(
                State.nav_hover_label == link["label"],
                rx.vstack(
                    rx.heading(link["label"], size="4", weight="bold", color=TEXT_PRIMARY),
                    rx.grid(
                        *[
                            rx.link(
                                rx.box(
                                    rx.text(child["label"], size="3", weight="bold", color=TEXT_PRIMARY),
                                    rx.text(child["description"], size="2", color=TEXT_MUTED, line_height="1.5"),
                                    spacing="1",
                                    align_items="start",
                                ),
                                href=child["href"],
                                _hover={"textDecoration": "none", "color": ACCENT},
                            )
                            for child in children
                        ],
                        columns={
                            "base": "repeat(1, minmax(0, 1fr))",
                            "md": "repeat(3, minmax(0, 1fr))",
                        },
                        spacing="3",
                        width="100%",
                    ),
                    spacing="3",
                    align_items="start",
                ),
                rx.box(),
            )
        )
    return rx.fragment(*groups)


def command_palette_button() -> rx.Component:
    """Compact trigger for the global command palette."""
    return rx.button(
        rx.hstack(
            rx.text("Search the site", size="2", color=TEXT_MUTED),
            rx.box(
                "⌘K",
                font_size="0.75rem",
                color=TEXT_MUTED,
                padding="0.1rem 0.4rem",
                border=f"1px solid {BORDER_COLOR}",
                border_radius="0.4rem",
            ),
            align_items="center",
            gap="0.5rem",
        ),
        on_click=State.open_command_palette,
        variant="ghost",
        cursor="pointer",
        padding="0.4rem 0.85rem",
        border_radius="12px",
        border=f"1px solid {BORDER_COLOR}",
        background_color=rx.cond(
            State.theme_mode == "light",
            "rgba(255, 255, 255, 0.65)",
            "rgba(12, 18, 26, 0.6)",
        ),
        backdrop_filter="blur(16px)",
        color=TEXT_PRIMARY,
        _hover={
            "borderColor": ACCENT,
            "color": ACCENT,
        },
        style={"transition": "all 0.2s ease"},
    )


def nav_dropdown(link: dict[str, Any]) -> rx.Component:
    """Hoverable dropdown for links with children."""
    items = link.get("children", [])
    if not items:
        return nav_link(link)

    return rx.hover_card.root(
        rx.hover_card.trigger(nav_link(link)),
        rx.hover_card.content(
            rx.vstack(
                *[
                    rx.link(
                        rx.vstack(
                            rx.text(child["label"], size="3", weight="bold", color=TEXT_PRIMARY),
                            rx.text(child["description"], size="2", color=TEXT_MUTED, line_height="1.5"),
                            spacing="1",
                            align_items="start",
                        ),
                        href=child["href"],
                        _hover={
                            "textDecoration": "none",
                            "color": ACCENT,
                        },
                        width="100%",
                    )
                    for child in items
                ],
                spacing="3",
                align_items="start",
            ),
            side="bottom",
            side_offset=10,
            align="start",
            padding="1rem",
            background=SURFACE_BRIGHT,
            border=f"1px solid {BORDER_BRIGHT}",
            border_radius="12px",
            box_shadow="0 20px 36px rgba(0,0,0,0.35)",
            min_width="260px",
            style={"backdropFilter": "blur(12px)"},
        ),
        open_delay=80,
        close_delay=120,
    )


def mobile_nav_panel() -> rx.Component:
    """Slide-down mobile navigation with nested links."""
    return rx.cond(
        State.mobile_nav_open,
        rx.box(
            rx.vstack(
                *[
                    rx.box(
                        rx.link(
                            rx.hstack(
                                rx.text(link["label"], size="4", weight="bold", color=TEXT_PRIMARY),
                                rx.cond(
                                    link.get("children"),
                                    rx.text("▾", size="3", color=TEXT_MUTED),
                                    rx.box(),
                                ),
                                align_items="center",
                                gap="0.5rem",
                            ),
                            href=link["href"],
                            _hover={"textDecoration": "none", "color": ACCENT},
                            on_click=State.close_mobile_nav,
                        ),
                        rx.cond(
                            link.get("children"),
                            rx.vstack(
                                *[
                                    rx.link(
                                        rx.text(
                                            f"• {child['label']}",
                                            size="3",
                                            color=TEXT_MUTED,
                                        ),
                                        href=child["href"],
                                        padding_left="1.5rem",
                                        _hover={"textDecoration": "none", "color": ACCENT},
                                        on_click=State.close_mobile_nav,
                                    )
                                    for child in link.get("children", [])
                                ],
                                spacing="2",
                                align_items="start",
                                margin_top="0.5rem",
                            ),
                            rx.box(),
                        ),
                        padding="0.5rem 0",
                        border_bottom=f"1px solid {BORDER_COLOR}",
                    )
                    for link in NAV_LINKS
                ],
                spacing="2",
                align_items="start",
            ),
            background=PRIMARY_BG,
            position="absolute",
            top="100%",
            left="0",
            right="0",
            z_index="90",
            border_bottom=f"1px solid {BORDER_COLOR}",
            padding="1rem 1.5rem 1.5rem",
            box_shadow="0 10px 30px rgba(0,0,0,0.18)",
            display={"base": "block", "md": "none"},
        ),
        rx.box(),
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
                        *[nav_item(link) for link in NAV_LINKS],
                        gap="0.75rem",
                        justify="center",
                        align_items="center",
                        flex="1",
                        display={"base": "none", "md": "flex"},
                    ),
                    rx.flex(
                        command_palette_button(),
                        theme_toggle(),
                        rx.button(
                            rx.text("☰", size="6"),
                            variant="ghost",
                            cursor="pointer",
                            padding="0.35rem 0.6rem",
                            border_radius="10px",
                            border=f"1px solid {BORDER_COLOR}",
                            background_color=rx.cond(
                                State.theme_mode == "light",
                                "rgba(255, 255, 255, 0.8)",
                                "rgba(12, 18, 26, 0.7)",
                            ),
                            on_click=State.toggle_mobile_nav,
                            display={"base": "flex", "md": "none"},
                            _hover={"borderColor": ACCENT, "color": ACCENT},
                        ),
                        gap="1rem",
                        align_items="center",
                    ),
                    align_items="center",
                    width="100%",
                    gap="1rem",
                ),
                max_width=MAX_CONTENT_WIDTH,
                margin="0 auto",
                padding="0 2rem",
            ),
            rx.box(
                submenu_children(State.nav_hover_label),
                max_width=MAX_CONTENT_WIDTH,
                margin="0 auto",
                padding=rx.cond(State.nav_hover_label != "", "1.25rem 2rem", "0 2rem"),
                opacity=rx.cond(State.nav_hover_label != "", "1", "0"),
                max_height=rx.cond(State.nav_hover_label != "", "400px", "0px"),
                overflow="hidden",
                transition="max-height 0.25s ease, opacity 0.2s ease, padding 0.2s ease",
                display={"base": "none", "md": "block"},
            ),
        ),
        mobile_nav_panel(),
        position="sticky",
        top="0",
        z_index="100",
        background_color=SURFACE,
        backdrop_filter="blur(20px)",
        border_bottom=border_color,
        box_shadow=box_shadow,
        padding="0.85rem 0",
        width="100%",
        style={"transition": "background-color 0.3s ease"},
        on_mouse_leave=State.clear_nav_hover,
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


COMMAND_SCRIPT = """
(() => {
  if (window.__xianCommandHotkeys) return;
  window.__xianCommandHotkeys = true;
  const trigger = () => document.getElementById("command-palette-trigger")?.click();
  const close = () => document.getElementById("command-palette-close")?.click();
  window.addEventListener("keydown", (event) => {
    const key = event.key?.toLowerCase();
    if ((event.metaKey || event.ctrlKey) && key === "k") {
      event.preventDefault();
      trigger();
    }
    if (key === "escape") {
      close();
    }
  });
})();
"""


def command_palette() -> rx.Component:
    """Global command palette with CMD/CTRL + K shortcut."""

    def action_row(action: dict[str, Any]) -> rx.Component:
        arrow = rx.cond(
            action["external"],
            rx.text("↗", size="3", color=TEXT_MUTED),
            rx.text("↩", size="3", color=TEXT_MUTED),
        )
        is_active = action["id"] == State.command_palette_active_id

        return rx.link(
            rx.hstack(
                rx.box(
                    action["badge"],
                    font_size="0.75rem",
                    color=ACCENT,
                    background=ACCENT_SOFT,
                    padding="0.15rem 0.5rem",
                    border_radius="999px",
                ),
                rx.vstack(
                    rx.text(action["title"], size="3", weight="medium", color=TEXT_PRIMARY),
                    rx.text(action["subtitle"], size="2", color=TEXT_MUTED),
                    spacing="1",
                    align_items="start",
                ),
                rx.spacer(),
                arrow,
                align_items="center",
                width="100%",
            ),
            href=action["href"],
            is_external=action["external"],
            on_click=State.close_command_palette,
            on_mouse_enter=State.set_command_palette_selection(action["id"]),
            style={
                "padding": "0.85rem 1rem",
                "borderRadius": "12px",
                "border": f"1px solid {BORDER_COLOR}",
                "transition": "all 0.2s ease",
                "background": rx.cond(is_active, ACCENT_SOFT, "transparent"),
                "borderColor": rx.cond(is_active, ACCENT, BORDER_COLOR),
            },
            _hover={
                "borderColor": ACCENT,
                "backgroundColor": ACCENT_SOFT,
                "textDecoration": "none",
            },
            width="100%",
        )

    def palette_list_entry(entry: dict[str, Any]) -> rx.Component:
        header = rx.box(
            rx.text(
                entry["category"],
                size="2",
                color=TEXT_MUTED,
                text_transform="uppercase",
                letter_spacing="0.2em",
            ),
            padding_top="0.5rem",
        )

        return rx.cond(
            entry["type"] == "header",
            header,
            action_row(entry),
        )

    return rx.fragment(
        rx.button(on_click=State.open_command_palette, id="command-palette-trigger", display="none"),
        rx.button(on_click=State.close_command_palette, id="command-palette-close", display="none"),
        rx.script(COMMAND_SCRIPT),
        rx.cond(
            State.command_palette_open,
            rx.fragment(
                rx.box(
                    position="fixed",
                    top="0",
                    left="0",
                    width="100%",
                    height="100vh",
                    background="rgba(6, 11, 17, 0.65)",
                    backdrop_filter="blur(12px)",
                    z_index="1000",
                    on_click=State.close_command_palette,
                ),
                rx.center(
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.vstack(
                                    rx.text("Search Xian Technology", size="4", weight="bold", color=TEXT_PRIMARY),
                                    spacing="1",
                                    align_items="start",
                                ),
                                rx.spacer(),
                                rx.text("ESC to close", size="2", color=TEXT_MUTED),
                                align_items="center",
                                width="100%",
                            ),
                            rx.input(
                                value=State.command_query,
                                on_change=State.set_command_query,
                                placeholder="Try “deterministic python”, “research guild”, or “foundation contact”",
                                auto_focus=True,
                                width="100%",
                                padding="1.1rem 1rem",
                                border=f"1.5px solid {BORDER_COLOR}",
                                border_radius="8px",
                                background=rx.cond(
                                    State.theme_mode == "light",
                                    "rgba(248, 249, 250, 0.95)",
                                    "rgba(15, 20, 28, 0.9)",
                                ),
                                color=TEXT_PRIMARY,
                                font_size="1.1rem",
                                style={"boxShadow": "none", "lineHeight": "1.5", "height": "64px"},
                                _focus={
                                    "borderColor": ACCENT,
                                    "outline": "none",
                                },
                            ),
                            rx.box(
                                rx.cond(
                                    State.command_palette_empty,
                                    rx.flex(
                                        rx.text("No matches found.", size="2", color=TEXT_MUTED),
                                        align="center",
                                        justify="center",
                                        height="100%",
                                        width="100%",
                                    ),
                                    rx.vstack(
                                        rx.foreach(
                                            State.command_palette_sections,
                                            lambda entry: palette_list_entry(entry),
                                        ),
                                        spacing="2",
                                        width="100%",
                                    ),
                                ),
                                width="100%",
                                max_height="360px",
                                overflow_y="auto",
                                border=f"1px solid {BORDER_COLOR}",
                                border_radius="12px",
                                padding="0.75rem",
                                background=rx.cond(
                                    State.theme_mode == "light",
                                    "rgba(248, 249, 250, 0.7)",
                                    "rgba(13, 17, 23, 0.8)",
                                ),
                            ),
                            spacing="4",
                            width="100%",
                        ),
                        width="min(960px, 92vw)",
                        max_width="960px",
                        background=PRIMARY_BG,
                        border_radius="20px",
                        border=f"1px solid {BORDER_COLOR}",
                        box_shadow=rx.cond(
                            State.theme_mode == "light",
                            "0 30px 120px rgba(15, 23, 42, 0.25)",
                            "0 30px 120px rgba(0, 0, 0, 0.8)",
                        ),
                        padding="2rem",
                        z_index="1001",
                    ),
                    position="fixed",
                    top="0",
                    left="0",
                    width="100%",
                    height="100vh",
                    z_index="1001",
                ),
            ),
        ),
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
                        rx.text("Follow", size="3", weight="bold", color=TEXT_PRIMARY),
                        rx.hstack(
                            rx.link(
                                rx.icon(tag="github", size=20, color=TEXT_PRIMARY),
                                href="https://github.com/xian-technology",
                                is_external=True,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.icon(tag="send", size=20, color=TEXT_PRIMARY),
                                href="https://t.me/xian_technology",
                                is_external=True,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.icon(tag="mail", size=20, color=TEXT_PRIMARY),
                                href="mailto:foundation@xian.technology",
                                _hover={"color": ACCENT},
                            ),
                            spacing="3",
                            align_items="center",
                        ),
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
                        "© 2025 Xian Technology Foundation. Built with ❤️ and 🐍.",
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
        command_palette(),
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
    "command_palette",
    "command_palette_button",
    "code_block",
    "feature_card",
    "nav_bar",
    "nav_link",
    "page_layout",
    "section",
    "terminal_prompt",
    "theme_toggle",
]
