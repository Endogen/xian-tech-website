import reflex as rx

from ..components.common import linked_heading, page_layout, section, section_panel, subsection
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
            transition="all 0.25s ease",
            _hover={
                "backgroundColor": SURFACE_HOVER,
                "transform": "translateY(-2px)",
                "boxShadow": f"0 12px 28px {ACCENT_SOFT}",
            },
            height="100%",
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
                rx.heading(
                    "ABCI - Application Blockchain Interface",
                    size="8",
                    color=TEXT_PRIMARY,
                    line_height="1.15",
                    weight="bold",
                ),
                rx.text(
                    "ABCI is the interface between CometBFT consensus and the application state machine. "
                    "It keeps the consensus layer language-agnostic while Xian’s Python execution layer focuses "
                    "on validation, contract execution, and state transitions.",
                    size="4",
                    color=TEXT_MUTED,
                    width="100%",
                    line_height="1.7",
                ),
                spacing="5",
                align_items="start",
            )
        ),
        section(
            section_panel(
                rx.flex(
                    linked_heading("ABCI", size="6", color=TEXT_PRIMARY, weight="bold"),
                    rx.hstack(
                        rx.link(
                            rx.hstack(
                                rx.icon(tag="github", size=18),
                                rx.text("Repo", size="3"),
                                spacing="2",
                                align_items="center",
                            ),
                            href="https://github.com/xian-technology/xian-abci",
                            is_external=True,
                            color=TEXT_MUTED,
                            _hover={"color": ACCENT},
                        ),
                        rx.link(
                            rx.hstack(
                                rx.icon(tag="book_open", size=18),
                                rx.text("Docs", size="3"),
                                spacing="2",
                                align_items="center",
                            ),
                            href="https://docs.xian.technology/",
                            is_external=True,
                            color=TEXT_MUTED,
                            _hover={"color": ACCENT},
                        ),
                        spacing="4",
                        align_items="center",
                    ),
                    direction={"base": "column", "md": "row"},
                    align_items={"base": "start", "md": "center"},
                    justify="between",
                    gap="0.75rem",
                    width="100%",
                ),
                rx.text(
                    "CometBFT calls into the ABCI app to validate transactions, execute blocks, and persist state. "
                    "The Xian ABCI implementation bridges those consensus hooks to Python contract execution.",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    width="100%",
                ),
                rx.grid(
                    choice_card(
                        "Mempool validation (CheckTx)",
                        "CometBFT validates incoming transactions with CheckTx and only relays valid ones to peers before consensus.",
                        "check",
                    ),
                    choice_card(
                        "FinalizeBlock execution",
                        "FinalizeBlock executes the decided block and returns transaction results in a single method.",
                        "bolt",
                    ),
                    choice_card(
                        "Commit + state commitment",
                        "Commit persists the state and returns a cryptographic commitment that is placed into the next block header.",
                        "shield",
                    ),
                    choice_card(
                        "ABCI 2.0 (ABCI++) hooks",
                        "PrepareProposal and ProcessProposal let the application shape and validate proposals; ExtendVote and VerifyVoteExtension attach and verify application data on votes.",
                        "code",
                    ),
                    choice_card(
                        "FinalizeBlock unifies execution",
                        "ABCI 2.0 coalesces BeginBlock, DeliverTx, and EndBlock into FinalizeBlock to simplify the execution pipeline.",
                        "layers",
                    ),
                    choice_card(
                        "Multiple ABCI connections",
                        "CometBFT opens separate ABCI connections for mempool validation, consensus execution, snapshots, and queries.",
                        "link",
                    ),
                    columns={
                        "base": "repeat(1, minmax(0, 1fr))",
                        "md": "repeat(2, minmax(0, 1fr))",
                        "lg": "repeat(3, minmax(0, 1fr))",
                    },
                    spacing="4",
                    width="100%",
                    align="stretch",
                ),
                subsection(
                    "How it works",
                    rx.vstack(
                        bullet("CometBFT calls CheckTx to validate transactions before they enter consensus."),
                        bullet("FinalizeBlock executes the block and returns transaction results in one pass."),
                        bullet("Commit writes state and returns the app hash that anchors the next block."),
                        bullet("ABCI++ adds proposal shaping and vote extension hooks for richer app logic."),
                        spacing="2",
                        align_items="start",
                    ),
                ),
            )
        ),
    )


__all__ = ["abci_page"]
