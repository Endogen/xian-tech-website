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


def consensus_page() -> rx.Component:
    """CometBFT consensus overview."""
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
                rx.heading("CometBFT Deterministic Consensus", size="8", color=TEXT_PRIMARY, line_height="1.15", weight="bold"),
                rx.text(
                    "Xian leverages CometBFT for distributed, Byzantine fault-tolerant state machine replication. "
                    "Blocks finalize deterministically, feeding the Python contracting layer with a reliable ordering of transactions.",
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
                        rx.heading("Deterministic finality", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "CometBFT’s BFT consensus delivers fast, deterministic finality—no probabilistic forks or reorgs.",
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
                        rx.heading("ABCI-driven state", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "The CometBFT block pipeline invokes Xian’s Python ABCI app for CheckTx, FinalizeBlock, and Commit to keep state and consensus in lockstep.",
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
                        rx.heading("Validator economics", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Masternode rewards are calculated per transaction, driven by stamp usage and allocated to validators and developers each block.",
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


__all__ = ["consensus_page"]
