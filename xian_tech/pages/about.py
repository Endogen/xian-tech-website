from typing import Any

import reflex as rx

from ..components.common import icon_watermark_hover_card, linked_heading, page_layout, section
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

TEAM_MEMBERS = [
    {
        "name": "David Strohmayer",
        "role": "Core Engineering",
        "bio": "Leads the foundation engineering roadmap across the ABCI layer, contracting runtime, and infrastructure.",
        "image": "/david.png",
        "socials": [
            {"icon": "linkedin", "href": "https://www.linkedin.com/in/david-s-7501b6221", "label": "LinkedIn"},
            {"icon": "github", "href": "https://github.com/Endogen", "label": "GitHub"},
            {"icon": "send", "href": "https://t.me/endogen", "label": "Telegram"},
            {"icon": "x", "href": "https://x.com/Endogen_XIAN", "label": "X"},
        ],
    },
    {
        "name": "Benjamin Gogan",
        "role": "Protocol Research",
        "bio": "Focuses on correctness, deterministic execution, and the long-term integrity of the Xian stack.",
        "image": "/benji.png",
        "socials": [
            {"icon": "linkedin", "href": "https://www.linkedin.com/in/benjamingogan", "label": "LinkedIn"},
            {"icon": "github", "href": "https://github.com/duelingbenjos", "label": "GitHub"},
            {"icon": "send", "href": "http://t.me/duckfever", "label": "Telegram"},
            {"icon": "x", "href": "https://x.com", "label": "X"},
        ],
    },
    {
        "name": "Riley Chen",
        "role": "Ecosystem & Partnerships",
        "bio": "Supports builders, partners, and operators shipping production applications on Xian.",
        "image": "/xian.jpg",
        "socials": [
            {"icon": "linkedin", "href": "https://www.linkedin.com", "label": "LinkedIn"},
            {"icon": "github", "href": "https://github.com", "label": "GitHub"},
            {"icon": "send", "href": "https://t.me/xian_technology", "label": "Telegram"},
            {"icon": "x", "href": "https://x.com", "label": "X"},
        ],
    },
]

HISTORY_EVENTS = [
    {
        "date": "May 1, 2017",
        "title": "Start of Lamden",
        "detail": (
            "Lamden launched in 2017 as a Python-first blockchain project and introduced the original Python "
            "smart-contracting library that later influenced Xian. The project was created by Stuart Farmer "
            "and funded through token rounds; ICO Drops reports $12.65M raised across four rounds, including the ICO."
        ),
        "sources": [
            {"label": "ICO Drops", "href": "https://icodrops.com/lamden"},
            {"label": "Stuart Farmer (LinkedIn)", "href": "https://www.linkedin.com/in/stuartfarmer"},
            {"label": "Lamden Contracting", "href": "https://github.com/lamden/contracting"},
        ],
    },
    {
        "date": "Sep 1, 2023",
        "title": "End of Lamden",
        "detail": (
            "In his farewell, Stuart Farmer described the market shift away from maker culture, early "
            "missteps, and a treasury loan default that eliminated Lamden’s runway. The team chose to "
            "hand stewardship to the community, open the software license for reuse, and place protocol "
            "assets under DAO control, while the original Python node was no longer maintained and the "
            "network went offline."
        ),
        "sources": [
            {"label": "Lamden Farewell", "href": "https://medium.com/lamden/farewell-ad8bb90caad"},
            {"label": "Contracting License", "href": "https://github.com/lamden/contracting/blob/master/LICENSE"},
        ],
    },
    {
        "date": "Dec 19, 2023",
        "title": "Start of the Xian Project",
        "detail": (
            "The Xian project began with the creation of core GitHub repositories like xian-core and "
            "xian-contracting. Community developers Duelingbenjos, Endogen, and Crosschainer kept the Python "
            "contracting library but replaced the Lamden node with CometBFT to secure a reliable consensus layer."
        ),
        "sources": [
            {"label": "xian-core repo", "href": "https://github.com/xian-network/xian-core"},
            {"label": "xian-contracting repo", "href": "https://github.com/xian-network/xian-contracting"},
            {"label": "CometBFT mention", "href": "https://github.com/xian-network/xian-core#xian"},
        ],
    },
    {
        "date": "Nov 8, 2025",
        "title": "Xian Technology Foundation created",
        "detail": (
            "The project formalized into the Xian Technology Foundation, launching the public website and "
            "related properties like the Playground and Contracting Hub. The focus shifted to delivering a polished, "
            "out-of-the-box stack, positioning Xian Technology as an Anaconda-style distribution for Python blockchain development."
        ),
        "sources": [
            {"label": "Xian Technology", "href": "https://www.xian.technology"},
            {"label": "Xian Technology GitHub", "href": "https://github.com/xian-technology"},
            {"label": "Playground", "href": "https://playground.xian.technology"},
        ],
    },
]

SEARCH_SECTIONS = [
    {
        "title": "About Xian",
        "subtitle": "Foundation context, team members, and the Xian stack history.",
        "category": "About",
        "badge": "Page",
        "href": "/about",
        "keywords": ["Foundation", "Team", "History"],
    },
    {
        "title": "Team",
        "subtitle": "Core contributors stewarding Xian Technology.",
        "category": "About",
        "badge": "Section",
        "href": "/about",
        "keywords": ["Team", "Contributors", "Foundation"],
    },
    {
        "title": "History",
        "subtitle": "Timeline from Lamden to the Xian Technology Foundation.",
        "category": "About",
        "badge": "Section",
        "href": "/about",
        "keywords": ["Lamden", "Xian", "Timeline"],
    },
]


def _history_item(event: dict[str, Any]) -> rx.Component:
    """Single timeline entry with expandable detail."""
    hover_shadow = rx.color_mode_cond(
        light="0 12px 28px rgba(80, 177, 101, 0.16)",
        dark="0 12px 28px rgba(0, 255, 136, 0.18)",
    )
    marker_glow = rx.color_mode_cond(
        light="0 0 0 6px rgba(80, 177, 101, 0.12)",
        dark="0 0 0 6px rgba(0, 255, 136, 0.16)",
    )

    sources = event.get("sources", [])
    content_children: list[rx.Component] = [
        rx.text(
            event["detail"],
            size="3",
            color=TEXT_MUTED,
            line_height="1.7",
        )
    ]
    if sources:
        content_children.append(
            rx.flex(
                rx.text("Sources:", size="2", color=TEXT_MUTED),
                rx.flex(
                    *[
                        rx.link(
                            source["label"],
                            href=source["href"],
                            is_external=True,
                            color=TEXT_MUTED,
                            size="2",
                            _hover={"color": ACCENT},
                        )
                        for source in sources
                    ],
                    gap="0.5rem",
                    wrap="wrap",
                ),
                gap="0.5rem",
                align_items="center",
                wrap="wrap",
            )
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
        icon_watermark_hover_card(
            rx.accordion.root(
                rx.accordion.item(
                    rx.accordion.header(
                        rx.accordion.trigger(
                            rx.hstack(
                                rx.hstack(
                                    rx.box(
                                        rx.text(
                                            event["date"],
                                            size="4",
                                            weight="bold",
                                            color=ACCENT,
                                            letter_spacing="0.08em",
                                        ),
                                        min_width=rx.breakpoints(initial="auto", md="150px"),
                                        flex_shrink="0",
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
                            rx.vstack(
                                *content_children,
                                spacing="3",
                                align_items="start",
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
            icon="history",
            padding="0",
            content_spacing="0",
            background=SURFACE,
            border=f"1px solid {BORDER_COLOR}",
            border_radius="14px",
            _hover={
                "borderColor": ACCENT,
                "boxShadow": hover_shadow,
            },
        ),
        position="relative",
        width="100%",
    )


def _team_card(member: dict[str, Any]) -> rx.Component:
    """Profile card for a team member."""
    role = member.get("role", "").lower()
    icon = "cpu" if "engineering" in role else "search" if "research" in role else "users"
    return icon_watermark_hover_card(
        rx.flex(
            rx.box(
                rx.image(
                    src=member["image"],
                    alt=f"{member['name']} portrait",
                    width="100%",
                    height="220px",
                    object_fit="cover",
                    transition="transform 0.35s ease",
                ),
                border_radius="12px",
                border=f"1px solid {BORDER_COLOR}",
                overflow="hidden",
                width="100%",
            ),
            rx.box(
                rx.vstack(
                    rx.text(member["name"], size="4", weight="bold", color=TEXT_PRIMARY),
                    rx.text(member["role"], size="2", color=TEXT_MUTED, text_transform="uppercase", letter_spacing="0.12em"),
                    rx.text(member["bio"], size="3", color=TEXT_MUTED, line_height="1.7"),
                    spacing="2",
                    align_items="start",
                ),
                width="100%",
                flex="1",
            ),
            rx.hstack(
                *[
                    rx.link(
                        rx.icon(tag=social["icon"], size=18),
                        href=social["href"],
                        is_external=True,
                        color=TEXT_MUTED,
                        title=social["label"],
                        _hover={"color": ACCENT},
                    )
                    for social in member["socials"]
                ],
                spacing="3",
                align_items="center",
            ),
            direction="column",
            gap="1rem",
            align_items="start",
            height="100%",
        ),
        icon=icon,
        padding="1.5rem",
        border_radius="16px",
        style={"&:hover img": {"transform": "scale(1.04)"}},
        height="100%",
    )


def team_section() -> rx.Component:
    """Team overview section."""
    return section(
        rx.vstack(
            linked_heading("Team", size="7", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                "The Xian Foundation is led by a small group of researchers and engineers stewarding the Xian stack.",
                size="4",
                color=TEXT_MUTED,
                line_height="1.7",
                max_width="900px",
            ),
            rx.grid(
                *[_team_card(member) for member in TEAM_MEMBERS],
                columns={"base": "1fr", "md": "repeat(3, minmax(0, 1fr))"},
                spacing="4",
                width="100%",
                align="stretch",
            ),
            spacing="6",
            align_items="start",
            width="100%",
        ),
        padding_top="0",
    )


def history_section() -> rx.Component:
    """Timeline of notable foundation milestones."""
    return section(
        rx.vstack(
            linked_heading("History", size="7", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                "Notable milestones that mark the evolution of Xian.",
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


def _network_card(title: str, body: str) -> rx.Component:
    """Card with a hover drawer for network links."""
    card_bg = rx.color_mode_cond(
        light=LIGHT_CARD_BG,
        dark=DARK_CARD_BG,
    )
    def drawer_link(label: str, href: str, icon: str) -> rx.Component:
        return rx.link(
            rx.hstack(
                rx.icon(tag=icon, size=16),
                rx.text(label, size="3"),
                spacing="2",
                align_items="center",
            ),
            href=href,
            is_external=True,
            color=TEXT_MUTED,
            _hover={"color": ACCENT},
        )

    return rx.box(
        rx.box(
            rx.vstack(
                rx.text(title, size="4", weight="bold", color=TEXT_PRIMARY),
                rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
                spacing="3",
                align_items="start",
            ),
            class_name="network-card",
            padding="1.75rem",
            background=card_bg,
            border=f"1px solid {BORDER_COLOR}",
            border_radius="16px",
            box_shadow="0 6px 18px rgba(0,0,0,0.12)",
            transition="all 0.25s ease",
            height="100%",
        ),
        rx.box(
            rx.vstack(
                drawer_link("Homepage", "https://xian.org", "globe"),
                drawer_link("Community", "https://t.me/xian_network", "send"),
                spacing="2",
                align_items="start",
                width="100%",
            ),
            class_name="network-drawer",
            position="absolute",
            top="calc(100% - 1px)",
            left="0",
            right="0",
            width="100%",
            max_height="0px",
            opacity="0",
            transform="translateY(-6px)",
            overflow="hidden",
            padding="0",
            transition="max-height 0.3s ease, opacity 0.3s ease, transform 0.3s ease, padding 0.3s ease",
            background=card_bg,
            border=f"1px solid {BORDER_COLOR}",
            border_top="none",
            border_radius="0 0 16px 16px",
            box_shadow="none",
            pointer_events="none",
            z_index="2",
        ),
        position="relative",
        width="100%",
        overflow="visible",
        style={
            "&:hover .network-card": {
                "borderColor": ACCENT,
                "boxShadow": f"0 14px 32px {ACCENT_SOFT}",
                "borderRadius": "16px 16px 0 0",
                "borderBottom": "none",
            },
            "&:hover .network-drawer": {
                "maxHeight": "140px",
                "opacity": "1",
                "transform": "translateY(0)",
                "padding": "0.85rem 1.75rem 1.25rem",
                "borderColor": ACCENT,
                "boxShadow": f"0 14px 32px {ACCENT_SOFT}",
                "pointerEvents": "auto",
            },
        },
        height="100%",
    )


def about_page() -> rx.Component:
    """Explain key Xian terms and their relationship."""
    foundation = _term_card(
        "Xian Foundation",
        "An independent group advancing the Xian Technology stack, led by the core developers of the Xian Network.",
        highlight=True,
    )
    technology = _term_card(
        "Xian Technology",
        "The software stack combining CometBFT consensus, a custom Python ABCI, the Python contracting engine, and tooling.",
    )
    network = _network_card(
        "Xian Network",
        "A decentralized blockchain, governed by a DAO, that demonstrates the Xian Technology stack in real-world use.",
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
                    "About Xian",
                    size="8",
                    color=TEXT_PRIMARY,
                    weight="bold",
                    line_height="1.2",
                ),
            ),
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
        team_section(),
        history_section(),
    )


__all__ = ["about_page"]
