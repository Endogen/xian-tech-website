import reflex as rx

from ..components.common import page_layout, section
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_SOFT,
    BORDER_COLOR,
    PRIMARY_BG,
    SURFACE,
    SURFACE_HOVER,
    TEXT_MUTED,
    TEXT_PRIMARY,
)

SEARCH_SECTIONS = [
    {
        "title": "CometBFT Consensus",
        "subtitle": "Byzantine fault-tolerant replication with a language-agnostic ABCI interface.",
        "category": "Technology",
        "badge": "Page",
        "href": "/consensus",
        "keywords": ["CometBFT", "Consensus", "ABCI", "BFT"],
    },
    {
        "title": "Language-agnostic application layer",
        "subtitle": "ABCI lets the application be written in any language while CometBFT handles consensus.",
        "category": "Technology",
        "badge": "Section",
        "href": "/consensus",
        "keywords": ["ABCI", "Application", "Language-agnostic"],
    },
    {
        "title": "ABCI execution flow",
        "subtitle": "CheckTx, FinalizeBlock, and Commit coordinate validation and state changes.",
        "category": "Technology",
        "badge": "Section",
        "href": "/consensus",
        "keywords": ["CheckTx", "FinalizeBlock", "Commit"],
    },
    {
        "title": "Security and extensibility",
        "subtitle": "ABCI++ hooks and evidence handling for advanced consensus workflows.",
        "category": "Technology",
        "badge": "Section",
        "href": "/consensus",
        "keywords": ["ABCI++", "Evidence", "Validators"],
    },
]


def consensus_page() -> rx.Component:
    """CometBFT consensus overview."""
    def info_card(title: str, body: str) -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.heading(title, size="5", color=TEXT_PRIMARY, weight="bold"),
                rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
                spacing="3",
                align_items="start",
            ),
            padding="2.25rem",
            background=SURFACE,
            border=f"1px solid {BORDER_COLOR}",
            border_radius="14px",
            _hover={"backgroundColor": SURFACE_HOVER, "transform": "translateY(-2px)"},
        )

    def choice_card(title: str, body: str, icon: str) -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.flex(
                    rx.icon(tag=icon, size=28, color=ACCENT),
                    rx.heading(title, size="5", weight="bold", color=TEXT_PRIMARY),
                    direction={"base": "row", "lg": "column"},
                    align={"base": "center", "lg": "start"},
                    spacing="3",
                ),
                rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
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
        )

    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("CONSENSUS", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading("CometBFT Consensus", size="8", color=TEXT_PRIMARY, line_height="1.15", weight="bold"),
                rx.text(
                    "CometBFT provides Byzantine fault-tolerant state machine replication and delivers the same ordered "
                    "transaction log to every non-faulty node. It separates consensus from the application state via ABCI, "
                    "so Xian can use its Python contracting engine while relying on a proven consensus core.",
                    size="4",
                    color=TEXT_MUTED,
                    width="100%",
                    line_height="1.7",
                ),
                rx.vstack(
                    rx.heading("Why we chose CometBFT", size="6", color=TEXT_PRIMARY, weight="bold"),
                    rx.grid(
                        choice_card(
                            "BFT replication",
                            "CometBFT keeps every non-faulty node on the same ordered transaction log and tolerates Byzantine failures below one-third of the validator set.",
                            "shield",
                        ),
                        choice_card(
                            "Consensus engine + ABCI",
                            "The consensus engine is decoupled from the application via ABCI, so the state machine can be written in any language.",
                            "link",
                        ),
                        choice_card(
                            "Mempool validation",
                            "CheckTx validates incoming transactions and only relays valid ones to peers before they enter consensus.",
                            "check",
                        ),
                        choice_card(
                            "Multi-connection ABCI",
                            "CometBFT maintains multiple ABCI connections (mempool, consensus, snapshot, and query) to keep responsibilities separated.",
                            "layers",
                        ),
                        columns={
                            "base": "repeat(1, minmax(0, 1fr))",
                            "md": "repeat(2, minmax(0, 1fr))",
                        },
                        spacing="4",
                        width="100%",
                        align="stretch",
                    ),
                    spacing="3",
                    align_items="start",
                ),
                spacing="6",
                align_items="start",
            )
        ),
    )


__all__ = ["consensus_page"]
