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
            rx.vstack(
                rx.text(column["name"], size="4", weight="bold", color=TEXT_PRIMARY),
                rx.hstack(
                    rx.text(column.get("count", 0), size="2", color=TEXT_MUTED),
                    rx.text("cards", size="2", color=TEXT_MUTED),
                    spacing="1",
                    align_items="center",
                ),
                rx.vstack(
                    rx.foreach(column["cards"], roadmap_card),
                    spacing="2",
                    align_items="stretch",
                    width="100%",
                ),
                spacing="2",
                align_items="start",
                width="100%",
            ),
            padding="1.5rem",
            background=SURFACE,
            border=f"1px solid {BORDER_COLOR}",
            border_radius="10px",
            min_width="260px",
            max_width="320px",
            width="100%",
            height="100%",
        )

    board_view = rx.hstack(
        rx.foreach(State.roadmap_columns, roadmap_column),
        spacing="3",
        align_items="stretch",
        width="100%",
        min_width="0",
        padding_bottom="1rem",
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
                        "Live roadmap board powered by Fizzy—showing what’s in progress, what’s next, and what’s ready to ship.",
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
                        rx.box(
                            board_view,
                            overflow_x="auto",
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
