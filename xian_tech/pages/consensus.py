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

    def bullet(text: str) -> rx.Component:
        return rx.hstack(
            rx.icon(tag="check", size=18, color=ACCENT),
            rx.text(text, size="3", color=TEXT_MUTED, line_height="1.7"),
            spacing="3",
            align_items="start",
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
                    "so Xian can keep its Python contracting engine while relying on a proven consensus core.",
                    size="4",
                    color=TEXT_MUTED,
                    max_width="900px",
                    line_height="1.7",
                ),
                rx.vstack(
                    rx.heading("Why we chose CometBFT", size="6", color=TEXT_PRIMARY, weight="bold"),
                    rx.vstack(
                        bullet("ABCI keeps the application language-agnostic, so the Python contracting layer stays intact."),
                        bullet("The mempool validates transactions with CheckTx and only relays valid ones to peers."),
                        bullet("ABCI’s execution flow (CheckTx → FinalizeBlock → Commit) gives clear checkpoints for validation and state commits."),
                        bullet("ABCI++ adds PrepareProposal, ProcessProposal, ExtendVote, and VerifyVoteExtension hooks for richer consensus logic."),
                        spacing="2",
                        align_items="start",
                    ),
                    spacing="3",
                    align_items="start",
                ),
                spacing="6",
                align_items="start",
            )
        ),
        section(
            rx.grid(
                info_card(
                    "BFT replication",
                    "CometBFT keeps every non-faulty node on the same ordered transaction log and tolerates Byzantine failures below one-third of the validator set.",
                ),
                info_card(
                    "Consensus engine + ABCI",
                    "The consensus engine is decoupled from the application via ABCI, so the state machine can be written in any language.",
                ),
                info_card(
                    "Mempool validation",
                    "CheckTx validates incoming transactions and only relays valid ones to peers before they enter consensus.",
                ),
                info_card(
                    "Multi-connection ABCI",
                    "CometBFT maintains multiple ABCI connections (mempool, consensus, snapshot, and query) to keep responsibilities separated.",
                ),
                template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
                gap="1.5rem",
            ),
            padding_top="0",
        ),
        section(
            rx.vstack(
                rx.heading("ABCI execution flow", size="6", color=TEXT_PRIMARY, weight="bold"),
                rx.grid(
                    info_card(
                        "1. CheckTx",
                        "Transactions are validated before entering the mempool; only valid transactions are gossiped to peers.",
                    ),
                    info_card(
                        "2. FinalizeBlock",
                        "When consensus decides a block, FinalizeBlock executes transactions and prepares the state update.",
                    ),
                    info_card(
                        "3. Commit",
                        "Commit persists state and returns a cryptographic commitment that is embedded in the next block header.",
                    ),
                    template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                    gap="1.5rem",
                ),
                spacing="4",
                align_items="start",
            )
        ),
        section(
            rx.grid(
                info_card(
                    "ABCI++ hooks",
                    "ABCI 2.0 introduces PrepareProposal, ProcessProposal, ExtendVote, and VerifyVoteExtensions for application-aware proposal and vote workflows.",
                ),
                info_card(
                    "Evidence pipeline",
                    "CometBFT gossips evidence of Byzantine behavior and commits it on-chain; applications decide how to punish faults (e.g., slashing).",
                ),
                info_card(
                    "Light client support",
                    "CometBFT specifies a light client protocol for verifying the latest state without running a full node.",
                ),
                template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                gap="1.5rem",
            ),
            padding_top="0",
        ),
    )


__all__ = ["consensus_page"]
