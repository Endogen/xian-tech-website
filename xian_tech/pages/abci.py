import reflex as rx

from ..components.common import page_layout, section
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
        "title": "Python ABCI for CometBFT",
        "subtitle": "Xian’s ABCI app translates CometBFT calls into the Python contracting runtime.",
        "category": "Technology",
        "badge": "Page",
        "href": "/abci",
        "keywords": ["ABCI", "CometBFT", "Python", "FinalizeBlock", "Commit"],
    },
    {
        "title": "Validation at the edge",
        "subtitle": "CheckTx rejects malformed transactions before they reach consensus.",
        "category": "Technology",
        "badge": "Section",
        "href": "/abci",
        "keywords": ["CheckTx", "Validation", "Signatures"],
    },
    {
        "title": "Deterministic execution pipeline",
        "subtitle": "FinalizeBlock runs ordered transactions through the processor and stages writes for Commit.",
        "category": "Technology",
        "badge": "Section",
        "href": "/abci",
        "keywords": ["FinalizeBlock", "Execution", "Deterministic"],
    },
    {
        "title": "State patching & upkeep",
        "subtitle": "Targeted state patches help networks stay coherent across migrations.",
        "category": "Technology",
        "badge": "Section",
        "href": "/abci",
        "keywords": ["Migrations", "State patches", "Upgrades"],
    },
]


def abci_page() -> rx.Component:
    """Python ABCI overview."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("ABCI", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading("Python ABCI for CometBFT", size="8", color=TEXT_PRIMARY, line_height="1.15", weight="bold"),
                rx.text(
                    "Xian’s ABCI app is written in Python, mediating every CometBFT call—CheckTx, FinalizeBlock, Commit, and proposal hooks—into the contracting runtime.",
                    size="4",
                    color=TEXT_MUTED,
                    max_width="850px",
                    line_height="1.7",
                ),
                spacing="5",
                align_items="start",
            )
        ),
        section(
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.heading("Validation at the edge", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "CheckTx verifies signatures, chain_id, and nonces before gossip; malformed transactions are rejected early.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        spacing="3",
                        align_items="start",
                    ),
                    padding="2.5rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                    _hover={"backgroundColor": SURFACE_HOVER, "transform": "translateY(-2px)"},
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("Deterministic execution pipeline", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "FinalizeBlock routes ordered transactions through the TxProcessor, feeds rewards, and stages writes for Commit to persist.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        spacing="3",
                        align_items="start",
                    ),
                    padding="2.5rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                    _hover={"backgroundColor": SURFACE_HOVER, "transform": "translateY(-2px)"},
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("State patching & upkeep", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "A dedicated state patch manager can apply targeted fixes when migrations are required, keeping long-lived networks coherent.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        spacing="3",
                        align_items="start",
                    ),
                    padding="2.5rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                    _hover={"backgroundColor": SURFACE_HOVER, "transform": "translateY(-2px)"},
                ),
                template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                gap="1.5rem",
            ),
            padding_top="0",
        ),
    )


__all__ = ["abci_page"]
