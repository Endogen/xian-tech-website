import re
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

MD_MEDIA = "@media (min-width: 1024px)"
NAV_DROPDOWN_LABELS = [link["label"] for link in NAV_LINKS if link.get("children")]


def _nav_has_dropdown(label_var: rx.Var) -> rx.Var:
    """Return True if the hovered label has dropdown children."""
    active: rx.Var | bool = False
    for label in NAV_DROPDOWN_LABELS:
        active = rx.cond(label_var == label, True, active)
    return active


def section(*children: rx.Component, **kwargs) -> rx.Component:
    """Wrap content in a centered section with generous spacing."""
    identifier = kwargs.pop("id", None)
    kwargs.setdefault("width", "100%")
    kwargs.setdefault("max_width", MAX_CONTENT_WIDTH)
    kwargs.setdefault("margin", "0 auto")
    kwargs.setdefault("padding_left", "2rem")
    kwargs.setdefault("padding_right", "2rem")
    kwargs.setdefault("padding_top", "5rem")
    kwargs.setdefault("padding_bottom", "5rem")
    return rx.box(*children, id=identifier, **kwargs)


def _anchor_id(value: str) -> str:
    """Create a URL-safe anchor id from a heading."""
    slug = value.lower().replace("&", "and")
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = slug.replace("_", "-")
    slug = re.sub(r"\s+", "-", slug).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug


def linked_heading(
    title: str,
    *,
    href: Optional[str] = None,
    anchor_id: Optional[str] = None,
    size: str = "6",
    icon_size: int = 18,
    scroll_margin_top: str = "1.5rem",
    **heading_kwargs: Any,
) -> rx.Component:
    """Heading with a hover-revealed anchor link icon."""
    anchor = anchor_id or _anchor_id(title)
    link_href = href or f"#{anchor}"
    return rx.link(
        rx.heading(title, size=size, **heading_kwargs),
        rx.icon(tag="link", size=icon_size, class_name="anchor-icon"),
        href=link_href,
        id=anchor,
        aria_label=f"Link to {title}",
        display="inline-flex",
        align_items="center",
        gap="0.5rem",
        text_decoration="none",
        color="inherit",
        style={
            "scrollMarginTop": scroll_margin_top,
            "& .anchor-icon": {
                "opacity": "0",
                "transform": "translateY(1px)",
                "transition": "opacity 0.2s ease, transform 0.2s ease, color 0.2s ease",
                "color": TEXT_MUTED,
            },
            "&:hover .anchor-icon": {
                "opacity": "1",
                "transform": "translateY(0)",
                "color": ACCENT,
            },
            "&:focus-visible .anchor-icon": {
                "opacity": "1",
                "transform": "translateY(0)",
                "color": ACCENT,
            },
        },
    )


def subsection(title: str, *children: rx.Component, **kwargs) -> rx.Component:
    """Section block with consistent spacing and a title."""
    spacing = kwargs.pop("spacing", "3")
    margin_top = kwargs.pop("margin_top", "1.5rem")
    heading_size = kwargs.pop("heading_size", "5")
    heading_id = kwargs.pop("id", None)
    heading_href = kwargs.pop("href", None)
    return rx.vstack(
        linked_heading(
            title,
            size=heading_size,
            color=TEXT_PRIMARY,
            weight="bold",
            href=heading_href,
            anchor_id=heading_id,
            scroll_margin_top="0.75rem",
        ),
        *children,
        spacing=spacing,
        align_items="start",
        width="100%",
        min_width="0",
        margin_top=margin_top,
        **kwargs,
    )


def section_panel(header: rx.Component, *children: rx.Component, **kwargs) -> rx.Component:
    """Highlight a page section with a header band and consistent spacing."""
    header_padding = kwargs.pop("header_padding", "2.5rem 2.5rem 1.75rem 2.5rem")
    body_padding = kwargs.pop("body_padding", "2rem 2.5rem 2.5rem 2.5rem")
    body_spacing = kwargs.pop("body_spacing", "4")
    header_background = rx.color_mode_cond(
        light="linear-gradient(180deg, rgba(80, 177, 101, 0.18) 0%, rgba(248, 249, 250, 0) 100%)",
        dark="linear-gradient(180deg, rgba(80, 177, 101, 0.22) 0%, rgba(15, 20, 28, 0) 100%)",
    )
    return rx.box(
        rx.box(
            header,
            padding=header_padding,
            background=header_background,
            width="100%",
            box_sizing="border-box",
        ),
        rx.box(
            rx.vstack(*children, spacing=body_spacing, align_items="start", width="100%"),
            padding=body_padding,
            width="100%",
            box_sizing="border-box",
        ),
        background=SURFACE,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="0 0 16px 16px",
        overflow="hidden",
        width="100%",
        **kwargs,
    )


def theme_toggle() -> rx.Component:
    """Theme toggle button with minimalist icons."""
    return rx.button(
        rx.color_mode_cond(
            light=rx.text("◑", size="6", line_height="1"),
            dark=rx.text("◐", size="6", line_height="1"),
        ),
        on_click=rx.toggle_color_mode,
        variant="ghost",
        cursor="pointer",
        padding="0.5rem",
        background_color="transparent",
        color=TEXT_MUTED,
        border="none",
        transition="all 0.3s ease",
        _hover={
            "color": ACCENT,
            "transform": "rotate(180deg)",
        },
    )


def nav_link(link: dict[str, str], extra: Optional[rx.Component] = None) -> rx.Component:
    """Navigation link with consistent spacing."""
    return rx.link(
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.text(
                        link["label"],
                        size="3",
                        weight="medium",
                        color=TEXT_MUTED,
                    ),
                    extra if extra is not None else rx.box(),
                    align_items="center",
                    gap="0.35rem",
                ),
                rx.box(
                    bg=ACCENT,
                    height="2px",
                    width=rx.cond(
                        State.nav_hover_label == link["label"],
                        "100%",
                        "0%",
                    ),
                    transition="width 0.2s ease",
                    border_radius="999px",
                ),
                spacing="1",
                align_items="start",
            ),
            padding="0.35rem 0",
        ),
        href=link["href"],
        padding="0.35rem 0.1rem",
        transition="all 0.2s ease",
        display="inline-flex",
        align_items="center",
        gap="0.35rem",
        _hover={
            "textDecoration": "none",
            "color": ACCENT,
        },
    )


def nav_label(link: dict[str, str], extra: Optional[rx.Component] = None) -> rx.Component:
    """Navigation label for dropdown triggers (non-clickable)."""
    return rx.box(
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.text(
                        link["label"],
                        size="3",
                        weight="medium",
                        color=TEXT_MUTED,
                    ),
                    extra if extra is not None else rx.box(),
                    align_items="center",
                    gap="0.35rem",
                ),
                rx.box(
                    bg=ACCENT,
                    height="2px",
                    width=rx.cond(
                        State.nav_hover_label == link["label"],
                        "100%",
                        "0%",
                    ),
                    transition="width 0.2s ease",
                    border_radius="999px",
                ),
                spacing="1",
                align_items="start",
            ),
            padding="0.35rem 0",
        ),
        padding="0.35rem 0.1rem",
        transition="all 0.2s ease",
        display="inline-flex",
        align_items="center",
        gap="0.35rem",
        cursor="pointer",
        role="button",
        tab_index=0,
        _hover={
            "textDecoration": "none",
            "color": ACCENT,
        },
    )


def nav_item(link: dict[str, Any]) -> rx.Component:
    """Navigation item with hover tracking for mega menu."""
    return rx.box(
        nav_label(link) if link.get("children") else nav_link(link),
        on_mouse_enter=State.set_nav_hover(link["label"]),
        on_focus=State.set_nav_hover(link["label"]),
        display="inline-flex",
    )


def _submenu_item(child: dict) -> rx.Component:
    """Render a single submenu item, optionally highlighted with accent gradient."""
    highlighted = child.get("highlighted", False)

    # Normal state: green-to-green gradient (light green → darker green)
    light_normal_gradient = "linear-gradient(to right, rgba(0, 179, 92, 0.12) 0%, rgba(0, 179, 92, 0.25) 100%)"
    dark_normal_gradient = "linear-gradient(to right, rgba(0, 255, 136, 0.10) 0%, rgba(0, 255, 136, 0.20) 100%)"

    # Hover state: surface color → green gradient
    light_hover_gradient = "linear-gradient(to right, rgba(255, 255, 255, 0.95) 40%, rgba(0, 179, 92, 0.15) 100%)"
    dark_hover_gradient = "linear-gradient(to right, rgba(25, 35, 48, 0.95) 40%, rgba(0, 255, 136, 0.12) 100%)"

    base_props = {
        "transition": "transform 0.2s ease, background 0.2s ease, box-shadow 0.2s ease, color 0.2s ease",
        "display": "block",
    }
    if highlighted:
        base_props["background_image"] = rx.color_mode_cond(
            light=light_normal_gradient,
            dark=dark_normal_gradient,
        )

    # Hover styles
    if highlighted:
        hover_style = {
            "textDecoration": "none",
            "color": ACCENT,
            "backgroundImage": rx.color_mode_cond(
                light=light_hover_gradient,
                dark=dark_hover_gradient,
            ),
            "boxShadow": "0 12px 32px rgba(0,0,0,0.16)",
        }
    else:
        hover_style = {
            "textDecoration": "none",
            "color": ACCENT,
            "background": SURFACE_BRIGHT,
            "boxShadow": "0 12px 32px rgba(0,0,0,0.16)",
        }

    return rx.link(
        rx.box(
            rx.text(child["label"], size="1", weight="bold", color=TEXT_PRIMARY),
            rx.text(child["description"], size="2", color=TEXT_MUTED, line_height="1.5"),
            spacing="1",
            align_items="start",
        ),
        href=child["href"],
        _hover=hover_style,
        padding="0.85rem 0.95rem",
        border_radius="10px",
        width="100%",
        **base_props,
    )


def submenu_children(label: str) -> rx.Component:
    """Render submenu content for a hovered label."""
    groups: list[rx.Component] = []
    for link in NAV_LINKS:
        children = link.get("children")
        if not children:
            continue
        if link["label"] == "Developers":
            highlighted = [child for child in children if child.get("highlighted")]
            regular = [child for child in children if not child.get("highlighted")]
            content = rx.vstack(
                rx.grid(
                    rx.vstack(
                        rx.text("Highlighted", size="2", weight="bold", color=TEXT_MUTED, letter_spacing="0.08em"),
                        rx.vstack(
                            *[_submenu_item(child) for child in highlighted],
                            spacing="3",
                            align_items="start",
                            width="100%",
                        ),
                        spacing="3",
                        align_items="start",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text("Developers", size="2", weight="bold", color=TEXT_MUTED, letter_spacing="0.08em"),
                        rx.grid(
                            *[_submenu_item(child) for child in regular],
                            columns={
                                "initial": "repeat(1, minmax(0, 1fr))",
                                "md": "repeat(2, minmax(0, 1fr))",
                            },
                            spacing="3",
                            width="100%",
                        ),
                        spacing="3",
                        align_items="start",
                        width="100%",
                    ),
                    columns={
                        "initial": "repeat(1, minmax(0, 1fr))",
                        "md": "minmax(0, 1fr) minmax(0, 2fr)",
                    },
                    spacing="4",
                    width="100%",
                ),
                spacing="3",
                align_items="start",
                width="100%",
            )
        else:
            content = rx.vstack(
                rx.text(link["label"], size="2", weight="bold", color=TEXT_MUTED, letter_spacing="0.08em"),
                rx.grid(
                    *[_submenu_item(child) for child in children],
                    columns={
                        "initial": "repeat(1, minmax(0, 1fr))",
                        "md": "repeat(3, minmax(0, 1fr))",
                    },
                    spacing="3",
                    width="100%",
                ),
                spacing="3",
                align_items="start",
            )
        groups.append(
            rx.cond(
                State.nav_hover_label == link["label"],
                content,
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
        background_color=rx.color_mode_cond(
            light="rgba(255, 255, 255, 0.65)",
            dark="rgba(12, 18, 26, 0.6)",
        ),
        backdrop_filter="blur(16px)",
        color=TEXT_PRIMARY,
        transition="all 0.2s ease",
        _hover={
            "borderColor": ACCENT,
            "color": ACCENT,
        },
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
                            rx.text(child["label"], size="1", weight="bold", color=TEXT_PRIMARY),
                            rx.text(child["description"], size="2", color=TEXT_MUTED, line_height="1.5"),
                            spacing="1",
                            align_items="start",
                        ),
                        href=child["href"],
                        _hover={
                            "textDecoration": "none",
                            "color": ACCENT,
                            "background": SURFACE_BRIGHT,
                            "boxShadow": "0 12px 32px rgba(0,0,0,0.16)",
                        },
                        padding="0.8rem 0.9rem",
                        border_radius="10px",
                        width="100%",
                        transition="transform 0.2s ease, background 0.2s ease, box-shadow 0.2s ease, color 0.2s ease",
                        display="block",
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
            background=SURFACE,
            position="absolute",
            top="100%",
            left="0",
            right="0",
            z_index="90",
            border_bottom="none",
            padding="1rem 1.5rem 1.5rem",
            box_shadow="none",
            max_height="70vh",
            overflow_y="auto",
            display=rx.breakpoints(initial="block", lg="none"),
        ),
        rx.box(),
    )


def nav_bar() -> rx.Component:
    """Professional navigation bar."""
    border_color = rx.color_mode_cond(
        light="1px solid rgba(15, 23, 42, 0.08)",
        dark="1px solid rgba(255, 255, 255, 0.12)",
    )
    base_shadow = rx.color_mode_cond(
        light="0 1px 20px rgba(15, 23, 42, 0.08)",
        dark="0 1px 20px rgba(0, 0, 0, 0.35)",
    )
    dropdown_active = _nav_has_dropdown(State.nav_hover_label)
    box_shadow = rx.cond(dropdown_active, "none", base_shadow)
    filter_shadow = "none"
    return rx.box(
        # Background layer for the nav surface (kept separate to avoid stacking context issues)
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background_color=SURFACE,
            z_index="-1",
            transition="background-color 0.3s ease",
        ),
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
                        display=rx.breakpoints(initial="none", lg="flex"),
                    ),
                    rx.flex(
                        command_palette_button(),
                        theme_toggle(),
                        rx.button(
                            rx.icon(tag="menu", size=24),
                            variant="ghost",
                            cursor="pointer",
                            padding="0.4rem 0.55rem",
                            border_radius="12px",
                            border="none",
                            background_color="transparent",
                            on_click=State.toggle_mobile_nav,
                            _hover={"color": ACCENT},
                            _active={"transform": "scale(0.92)"},
                            display=rx.breakpoints(initial="flex", lg="none"),
                            align_items="center",
                            justify_content="center",
                            height="2.6rem",
                            transition="color 0.2s ease, transform 0.15s ease",
                        ),
                        gap="1.25rem",
                        align_items="center",
                    ),
                    align_items="center",
                    width="100%",
                    gap="1.25rem",
                    justify="between",
                ),
                max_width=MAX_CONTENT_WIDTH,
                margin="0 auto",
                padding="0 2rem",
            ),
        ),
        rx.box(
            rx.box(
                rx.box(
                    submenu_children(State.nav_hover_label),
                    padding="1.5rem 2rem",
                    max_width=MAX_CONTENT_WIDTH,
                    width="100%",
                    margin="0 auto",
                ),
                position="relative",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_top="none",
                border_radius="0px",
                box_shadow="none",
                width="100%",
                overflow="hidden",
                opacity=rx.cond(dropdown_active, "1", "0"),
                transform=rx.cond(dropdown_active, "translateY(0)", "translateY(6px)"),
                visibility=rx.cond(dropdown_active, "visible", "hidden"),
                transition="opacity 0.18s cubic-bezier(0.22, 0.61, 0.36, 1), transform 0.18s cubic-bezier(0.22, 0.61, 0.36, 1), visibility 0s",
                pointer_events=rx.cond(dropdown_active, "auto", "none"),
            ),
            position="absolute",
            top="100%",
            left="0",
            right="0",
            padding_top="0px",
            padding_left="0",
            padding_right="0",
            z_index="99",
            display=rx.breakpoints(initial="none", lg="block"),
        ),
        mobile_nav_panel(),
        position="sticky",
        top="0",
        z_index="100",
        border_bottom=rx.cond(
            dropdown_active,
            "1px solid transparent",
            rx.cond(State.mobile_nav_open, "1px solid transparent", border_color),
        ),
        padding="0.85rem 0",
        width="100%",
        on_mouse_leave=State.clear_nav_hover,
        filter=rx.breakpoints(initial="none", lg=filter_shadow),
        box_shadow=rx.breakpoints(initial="none", lg=box_shadow),
        transition="filter 0.18s ease, box-shadow 0.18s ease",
    )


def code_block(code: str) -> rx.Component:
    """Syntax-highlight friendly code block."""
    return rx.box(
        rx.text(
            code,
            font_family="'SF Mono', 'Monaco', 'Menlo', 'Courier New', monospace",
            size="2",
            color=rx.color_mode_cond(light="#1f2937", dark="#c9d1d9"),
            white_space="pre",
            line_height="1.6",
        ),
        background=CODE_BG,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="10px",
        padding="1.5rem",
        overflow_x="auto",
        width="100%",
        transition="all 0.3s ease",
    )


def feature_card(title: str, description: str, icon: str) -> rx.Component:
    """Feature card with hover affordances."""
    return rx.box(
        rx.vstack(
            rx.icon(tag=icon, size=28, color=ACCENT),
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
  const moveUp = () => document.getElementById("command-palette-up")?.click();
  const moveDown = () => document.getElementById("command-palette-down")?.click();
  const selectActive = () => document.getElementById("command-palette-select")?.click();
  const closeLightbox = () => document.getElementById("image-lightbox-close")?.click();
  const isLightboxOpen = () => document.getElementById("image-lightbox-container");
  const scrollToActive = () => {
    setTimeout(() => {
      const active = document.getElementById("palette-active-item");
      if (active) {
        active.scrollIntoView({ block: "nearest", behavior: "smooth" });
      }
    }, 50);
  };
  window.addEventListener("keydown", (event) => {
    const key = event.key?.toLowerCase();
    if ((event.metaKey || event.ctrlKey) && key === "k") {
      event.preventDefault();
      trigger();
    }
    if (key === "escape") {
      if (isLightboxOpen()) {
        closeLightbox();
      } else {
        close();
      }
    }
    if (key === "arrowup") {
      event.preventDefault();
      moveUp();
      scrollToActive();
    }
    if (key === "arrowdown") {
      event.preventDefault();
      moveDown();
      scrollToActive();
    }
    if (key === "enter") {
      const active = document.activeElement;
      const isInput = active?.tagName === "INPUT";
      if (isInput) {
        event.preventDefault();
        selectActive();
      }
    }
  });
})();
"""


def command_palette() -> rx.Component:
    """Global command palette with CMD/CTRL + K shortcut."""

    def action_row(action: dict[str, Any]) -> rx.Component:
        arrow = rx.cond(
            action["external"],
            rx.icon(tag="arrow_up_right", size=18, color=TEXT_MUTED),
            rx.icon(tag="corner_down_left", size=18, color=TEXT_MUTED),
        )
        arrow_slot = rx.center(
            arrow,
            width="22px",
            height="22px",
            flex_shrink="0",
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
                    border_radius="6px",
                ),
                rx.vstack(
                    rx.text(action["title"], size="3", weight="medium", color=TEXT_PRIMARY),
                    rx.text(action["subtitle"], size="2", color=TEXT_MUTED),
                    spacing="1",
                    align_items="start",
                ),
                rx.spacer(),
                arrow_slot,
                align_items="center",
                width="100%",
            ),
            id=rx.cond(is_active, "palette-active-item", ""),
            href=action["href"],
            is_external=action["external"],
            on_click=State.close_command_palette,
            on_mouse_enter=State.set_command_palette_selection(action["id"]),
            padding="0.85rem 1rem",
            border_radius="12px",
            border=f"1px solid {BORDER_COLOR}",
            transition="all 0.2s ease",
            background=rx.cond(is_active, ACCENT_SOFT, "transparent"),
            border_color=rx.cond(is_active, ACCENT, BORDER_COLOR),
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
        rx.button(on_click=State.command_palette_move_up, id="command-palette-up", display="none"),
        rx.button(on_click=State.command_palette_move_down, id="command-palette-down", display="none"),
        rx.button(on_click=State.command_palette_select_active, id="command-palette-select", display="none"),
        rx.script(COMMAND_SCRIPT),
        rx.cond(
            State.command_palette_open,
            rx.fragment(
                rx.center(
                    rx.box(
                        rx.vstack(
                            rx.text_field(
                                rx.text_field.slot(
                                    rx.button(
                                        "ESC",
                                        on_click=State.close_command_palette,
                                        size="1",
                                        variant="outline",
                                        color=TEXT_MUTED,
                                        border_color=BORDER_COLOR,
                                        background_color=rx.color_mode_cond(
                                            light="rgba(255, 255, 255, 0.7)",
                                            dark="rgba(12, 18, 26, 0.6)",
                                        ),
                                        padding="0.1rem 0.6rem",
                                        font_size="0.75rem",
                                        cursor="pointer",
                                        title="Close",
                                        _hover={
                                            "color": ACCENT,
                                            "borderColor": ACCENT,
                                        },
                                    ),
                                    side="right",
                                ),
                                value=State.command_query,
                                on_change=State.set_command_query,
                                placeholder='Try "deterministic python", "research guild", or "foundation contact"',
                                auto_focus=True,
                                width="100%",
                                size="3",
                                radius="medium",
                                variant="surface",
                                border=f"1.5px solid {BORDER_COLOR}",
                                background=rx.color_mode_cond(
                                    light="rgba(248, 249, 250, 0.95)",
                                    dark="rgba(15, 20, 28, 0.9)",
                                ),
                                color=TEXT_PRIMARY,
                                font_size="1.1rem",
                                line_height="1.5",
                                style={
                                    "& input::placeholder": {
                                        "color": rx.color_mode_cond(light="#4b5563", dark="#9ca3af"),
                                        "opacity": "1",
                                    },
                                },
                                _focus={
                                    "borderColor": ACCENT,
                                    "outline": "none",
                                },
                                _focus_within={
                                    "borderColor": ACCENT,
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
                                        padding_right="0.5rem",
                                        padding_bottom="0.5rem",
                                    ),
                                ),
                                width="100%",
                                max_height="360px",
                                overflow_y="auto",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                        width="min(960px, 92vw)",
                        max_width="960px",
                        background=PRIMARY_BG,
                        border_radius="20px",
                        border=f"1px solid {BORDER_COLOR}",
                        box_shadow=rx.color_mode_cond(
                            light="0 30px 120px rgba(15, 23, 42, 0.25)",
                            dark="0 30px 120px rgba(0, 0, 0, 0.8)",
                        ),
                        padding="2rem",
                        z_index="1001",
                        on_click=rx.stop_propagation,
                    ),
                    position="fixed",
                    top="0",
                    left="0",
                    width="100%",
                    height="100vh",
                    z_index="1001",
                    background="rgba(6, 11, 17, 0.65)",
                    backdrop_filter="blur(12px)",
                    on_click=State.close_command_palette,
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
    nav_sections = [link for link in NAV_LINKS if link.get("children")]

    def footer_link(child: dict[str, str]) -> rx.Component:
        href = child["href"]
        return rx.link(
            child["label"],
            href=href,
            is_external=href.startswith("http"),
            color=TEXT_MUTED,
            size="3",
            _hover={"color": ACCENT},
        )

    def footer_nav_section(section: dict[str, str]) -> rx.Component:
        return rx.vstack(
            rx.text(section["label"], size="3", weight="bold", color=TEXT_PRIMARY),
            rx.vstack(
                *[footer_link(child) for child in section["children"]],
                spacing="3",
                align_items="start",
            ),
            spacing="3",
            align_items="start",
        )

    return rx.box(
        rx.box(
            rx.vstack(
                rx.grid(
                    rx.vstack(
                        rx.text("Xian Technology", size="4", weight="bold", color=TEXT_PRIMARY),
                        rx.text("Python-native contracting", size="3", color=TEXT_MUTED, line_height="1.6"),
                        spacing="2",
                        align_items="start",
                    ),
                    *[footer_nav_section(section) for section in nav_sections],
                    rx.vstack(
                        rx.text("Contact", size="3", weight="bold", color=TEXT_PRIMARY),
                        rx.hstack(
                            rx.link(
                                rx.icon(tag="mail", size=20),
                                href="mailto:foundation@xian.technology",
                                color=TEXT_PRIMARY,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.icon(tag="message_square_text", size=20),
                                href="/contact",
                                color=TEXT_PRIMARY,
                                _hover={"color": ACCENT},
                            ),
                            spacing="3",
                            align_items="center",
                        ),
                        rx.text("Follow", size="3", weight="bold", color=TEXT_PRIMARY),
                        rx.hstack(
                            rx.link(
                                rx.icon(tag="github", size=20),
                                href="https://github.com/xian-technology",
                                is_external=True,
                                color=TEXT_PRIMARY,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.icon(tag="send", size=20),
                                href="https://t.me/xian_technology",
                                is_external=True,
                                color=TEXT_PRIMARY,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.icon(tag="twitter", size=20),
                                href="https://x.com/xian_technology",
                                is_external=True,
                                color=TEXT_PRIMARY,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.icon(tag="youtube", size=20),
                                href="https://www.youtube.com/xian-technology",
                                is_external=True,
                                color=TEXT_PRIMARY,
                                _hover={"color": ACCENT},
                            ),
                            spacing="3",
                            align_items="center",
                        ),
                        spacing="3",
                        align_items="start",
                    ),
                    columns={
                        "initial": "1fr",
                        "md": "repeat(2, minmax(0, 1fr))",
                        "lg": "repeat(5, minmax(0, 1fr))",
                    },
                    gap="3rem",
                    width="100%",
                    align_items="start",
                ),
                rx.box(
                    rx.flex(
                        rx.text("© 2025 Xian Technology. Built with 💚 and 🐍", size="2", color=TEXT_MUTED),
                        gap="0.35rem",
                        align_items="center",
                        justify="center",
                        wrap="wrap",
                        width="100%",
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
        transition="background-color 0.3s ease",
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
        transition="background-color 0.3s ease, color 0.3s ease",
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
    "section_panel",
    "subsection",
    "terminal_prompt",
    "theme_toggle",
]
