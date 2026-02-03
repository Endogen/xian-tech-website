import reflex as rx

from ..components.common import page_layout, section
from ..state import RoadmapCard, RoadmapColumn, State
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_SOFT,
    BORDER_COLOR,
    SURFACE,
    SURFACE_HOVER,
    TEXT_MUTED,
    TEXT_PRIMARY,
)

SEARCH_SECTIONS = [
    {
        "title": "Roadmap",
        "subtitle": "Upcoming milestones for the Xian Technology stack and ecosystem.",
        "category": "Technology",
        "badge": "Page",
        "href": "/roadmap",
        "keywords": ["Roadmap", "Milestones", "Stack"],
    }
]


def roadmap_page() -> rx.Component:
    """Roadmap page."""
    column_header_background = rx.color_mode_cond(
        light="linear-gradient(180deg, rgba(80, 177, 101, 0.18) 0%, rgba(248, 249, 250, 0) 100%)",
        dark="linear-gradient(180deg, rgba(80, 177, 101, 0.22) 0%, rgba(15, 20, 28, 0) 100%)",
    )

    def roadmap_card(card: RoadmapCard) -> rx.Component:
        card_body = rx.box(
            rx.vstack(
                rx.text(card["title"], size="2", weight="bold", color=TEXT_PRIMARY),
                rx.cond(
                    card["tags_text"] != "",
                    rx.text(card["tags_text"], size="1", color=TEXT_MUTED),
                    rx.box(),
                ),
                spacing="1",
                align_items="start",
            ),
            padding="0.65rem 0.75rem",
            background=ACCENT_SOFT,
            border=f"1px solid {BORDER_COLOR}",
            border_radius="6px",
            transition="all 0.2s ease",
            _hover={"backgroundColor": SURFACE_HOVER, "borderColor": ACCENT},
            width="100%",
        )
        return rx.cond(
            card["url"] != "",
            rx.link(card_body, href=card["url"], is_external=True, _hover={"textDecoration": "none"}),
            card_body,
        )

    def roadmap_column(column: RoadmapColumn) -> rx.Component:
        return rx.box(
            rx.box(
                rx.vstack(
                    rx.text(column["name"], size="4", weight="bold", color=TEXT_PRIMARY),
                    rx.hstack(
                        rx.text(column.get("count", 0), size="2", color=TEXT_MUTED),
                        rx.text("cards", size="2", color=TEXT_MUTED),
                        spacing="1",
                        align_items="center",
                    ),
                    spacing="1",
                    align_items="start",
                    width="100%",
                ),
                padding="1.25rem 1.5rem 1rem 1.5rem",
                background=column_header_background,
                width="100%",
                box_sizing="border-box",
            ),
            rx.box(
                rx.vstack(
                    rx.foreach(column["cards"], roadmap_card),
                    spacing="2",
                    align_items="stretch",
                    width="100%",
                ),
                padding="1rem 1.5rem 1.5rem 1.5rem",
                width="100%",
                box_sizing="border-box",
            ),
            background=SURFACE,
            border=f"1px solid {BORDER_COLOR}",
            border_radius="0 0 16px 16px",
            overflow="hidden",
            width="100%",
        )

    board_view = rx.grid(
        rx.foreach(State.roadmap_columns, roadmap_column),
        columns={"base": "1", "md": "2", "lg": "4"},
        spacing="4",
        align="start",
        width="100%",
    )

    done_section = rx.vstack(
        rx.hstack(
            rx.text("Done", size="4", weight="bold", color=TEXT_PRIMARY),
            rx.text(State.roadmap_done_count, size="2", color=TEXT_MUTED),
            spacing="2",
            align_items="center",
        ),
        rx.grid(
            rx.foreach(State.roadmap_done_cards, roadmap_card),
            columns={"base": "1", "sm": "2", "md": "3", "lg": "4"},
            spacing="4",
            width="100%",
        ),
        spacing="3",
        align_items="start",
        width="100%",
        padding_top="1.5rem",
    )

    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("ROADMAP", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                    rx.heading(
                        "Roadmap",
                        size="8",
                        color=TEXT_PRIMARY,
                        weight="bold",
                        line_height="1.2",
                    ),
                    rx.text(
                        "Live roadmap board powered by ",
                        rx.link(
                            "Fizzy",
                            href="https://github.com/basecamp/fizzy",
                            is_external=True,
                            color=ACCENT,
                            _hover={"text_decoration": "underline"},
                        ),
                        "—showing what’s in progress, what’s next, and what’s ready to ship.",
                        size="4",
                        color=TEXT_MUTED,
                        line_height="1.7",
                        max_width="900px",
                    ),
                spacing="6",
                align_items="start",
            )
        ),
        section(
            rx.box(
                rx.cond(
                    State.roadmap_loading,
                    rx.hstack(
                        rx.spinner(color=ACCENT),
                        rx.text("Loading roadmap…", size="3", color=TEXT_MUTED),
                        spacing="2",
                        align_items="center",
                    ),
                    rx.cond(
                        State.roadmap_error != "",
                        rx.box(
                            rx.text(
                                "Roadmap data is not available right now. "
                                "Set FIZZY_TOKEN, FIZZY_ACCOUNT_SLUG, and FIZZY_BOARD_ID to enable it.",
                                size="3",
                                color=TEXT_MUTED,
                                line_height="1.7",
                            ),
                            padding="1.5rem",
                            background=SURFACE,
                            border=f"1px solid {BORDER_COLOR}",
                            border_radius="12px",
                        ),
                        rx.vstack(
                            board_view,
                            rx.cond(State.roadmap_done_count > 0, done_section, rx.box()),
                            spacing="4",
                            align_items="start",
                            width="100%",
                        ),
                    ),
                ),
                on_mount=State.load_roadmap,
            ),
            padding_top="0",
        ),
    )


__all__ = ["roadmap_page"]
