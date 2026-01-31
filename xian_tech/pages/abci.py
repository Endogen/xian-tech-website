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
        "title": "ABCI (Application Blockchain Interface)",
        "subtitle": "The interface between CometBFT consensus and the Xian application layer.",
        "category": "Technology",
        "badge": "Page",
        "href": "/abci",
        "keywords": ["ABCI", "CometBFT", "Application", "FinalizeBlock", "Commit"],
    },
    {
        "title": "Language-agnostic interface",
        "subtitle": "ABCI lets the application be written in any language while CometBFT handles consensus.",
        "category": "Technology",
        "badge": "Section",
        "href": "/abci",
        "keywords": ["ABCI", "Language-agnostic", "Interface"],
    },
    {
        "title": "Execution pipeline",
        "subtitle": "CheckTx, FinalizeBlock, and Commit define the core ABCI flow.",
        "category": "Technology",
        "badge": "Section",
        "href": "/abci",
        "keywords": ["CheckTx", "FinalizeBlock", "Commit"],
    },
    {
        "title": "ABCI++ hooks",
        "subtitle": "PrepareProposal, ProcessProposal, ExtendVote, and VerifyVoteExtension add richer consensus hooks.",
        "category": "Technology",
        "badge": "Section",
        "href": "/abci",
        "keywords": ["ABCI++", "PrepareProposal", "ProcessProposal", "ExtendVote"],
    },
]


def abci_page() -> rx.Component:
    """Python ABCI overview."""
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
                    rx.text("ABCI", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading("ABCI: the Application Blockchain Interface", size="8", color=TEXT_PRIMARY, line_height="1.15", weight="bold"),
                rx.text(
                    "ABCI is the interface between CometBFT (the state-machine replication engine) and the application state "
                    "machine. CometBFT initiates ABCI methods and the application responds, allowing the app to be written in "
                    "any language while CometBFT provides consensus and networking.",
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
            rx.vstack(
                rx.heading("Why it matters for Xian", size="6", color=TEXT_PRIMARY, weight="bold"),
                rx.vstack(
                    bullet("ABCI keeps the application language-agnostic, so the Python contracting engine stays intact."),
                    bullet("CometBFT handles consensus and P2P; the Xian application focuses on validation and state."),
                    bullet("Xian Core is implemented as an ABCI application for CometBFT 0.38.x."),
                    spacing="2",
                    align_items="start",
                ),
                spacing="3",
                align_items="start",
            ),
            padding_top="0",
        ),
        section(
            rx.grid(
                info_card(
                    "Mempool validation (CheckTx)",
                    "CometBFT validates incoming transactions with CheckTx and only relays valid ones to peers before consensus.",
                ),
                info_card(
                    "FinalizeBlock execution",
                    "FinalizeBlock executes the decided block and returns transaction results in a single method.",
                ),
                info_card(
                    "Commit + state commitment",
                    "Commit persists the state and returns a cryptographic commitment that is placed into the next block header.",
                ),
                template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                gap="1.5rem",
            ),
            padding_top="0",
        ),
        section(
            rx.grid(
                info_card(
                    "ABCI 2.0 (ABCI++) hooks",
                    "PrepareProposal and ProcessProposal let the application shape and validate proposals; ExtendVote and VerifyVoteExtension attach and verify application data on votes.",
                ),
                info_card(
                    "FinalizeBlock unifies execution",
                    "ABCI 2.0 coalesces BeginBlock, DeliverTx, and EndBlock into FinalizeBlock to simplify the execution pipeline.",
                ),
                info_card(
                    "Multiple ABCI connections",
                    "CometBFT opens separate ABCI connections for mempool validation, consensus execution, snapshots, and queries.",
                ),
                template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                gap="1.5rem",
            ),
            padding_top="0",
        ),
        section(
            rx.box(
                rx.vstack(
                    rx.heading("Xian Core implementation", size="6", color=TEXT_PRIMARY, weight="bold"),
                    rx.text(
                        "The Xian node is implemented as a dedicated ABCI application for CometBFT. "
                        "Explore the Xian Core repository for the Python implementation and protocol glue.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                        max_width="900px",
                    ),
                    rx.link(
                        rx.hstack(
                            rx.icon(tag="github", size=18),
                            rx.text("xian-core on GitHub", size="3"),
                            spacing="2",
                            align_items="center",
                        ),
                        href="https://github.com/xian-network/xian-core",
                        is_external=True,
                        color=ACCENT,
                        _hover={"color": TEXT_PRIMARY},
                    ),
                    spacing="3",
                    align_items="start",
                ),
                padding="2.5rem",
                background=PRIMARY_BG,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="16px",
            ),
            padding_top="0",
        ),
    )


__all__ = ["abci_page"]
