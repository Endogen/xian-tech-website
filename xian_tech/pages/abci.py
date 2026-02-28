import reflex as rx

from ..components.common import (
    hover_icon_chip,
    icon_watermark_hover_card,
    linked_heading,
    page_layout,
    section,
    section_panel,
    subsection,
)
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_SOFT,
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
    def info_card(title: str, body: str, icon: str = "circle_help") -> rx.Component:
        return icon_watermark_hover_card(
            rx.heading(title, size="5", color=TEXT_PRIMARY, weight="bold"),
            rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
            icon=icon,
            padding="2.25rem",
        )

    def choice_card(title: str, body: str, icon: str) -> rx.Component:
        return icon_watermark_hover_card(
            rx.flex(
                hover_icon_chip(icon),
                rx.heading(title, size="5", weight="bold", color=TEXT_PRIMARY),
                direction={"base": "row", "lg": "column"},
                align={"base": "center", "lg": "start"},
                spacing="3",
            ),
            rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
            icon=icon,
            padding="2rem",
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
                    "ABCI is the precise interface between the CometBFT consensus engine and the application logic "
                    "of an app-specific blockchain. It keeps consensus language-agnostic, so teams can build a full "
                    "custom chain in the programming language that fits their project—Xian uses Python for its execution "
                    "layer, validation, and contract logic.",
                    size="4",
                    color=TEXT_MUTED,
                    width="100%",
                    line_height="1.7",
                ),
                spacing="5",
                align_items="start",
            ),
        ),
        section(
            section_panel(
                rx.vstack(
                        rx.flex(
                            linked_heading("ABCI", size="6", color=TEXT_PRIMARY, weight="bold"),
                            rx.hstack(
                                rx.link(
                                    rx.hstack(
                                        rx.icon(tag="github", size=18),
                                        rx.text("Repo", size="3", display=rx.breakpoints(initial="none", md="inline")),
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
                                        rx.icon(tag="brain", size=18),
                                        rx.text("DeepWiki", size="3", display=rx.breakpoints(initial="none", md="inline")),
                                        spacing="2",
                                        align_items="center",
                                    ),
                                    href="https://deepwiki.com/xian-technology/xian-abci",
                                    is_external=True,
                                    color=TEXT_MUTED,
                                    _hover={"color": ACCENT},
                                ),
                                rx.link(
                                    rx.hstack(
                                        rx.icon(tag="book_open", size=18),
                                        rx.text("Docs", size="3", display=rx.breakpoints(initial="none", md="inline")),
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
                            "That ABCI app is the chain’s logic program, and in Xian it bridges consensus hooks to Python "
                            "contract execution and state transitions.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                            width="100%",
                        ),
                        spacing="3",
                        align_items="start",
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
                    rx.text(
                        "CometBFT proposes and finalizes blocks, then calls into the ABCI app so the application can "
                        "validate transactions, execute state transitions, and return results. ABCI keeps consensus and "
                        "application logic cleanly separated, while allowing the application to be written in any language—"
                        "including Xian’s Python execution layer.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                        width="100%",
                    ),
                    rx.image(
                        src="/abci.png",
                        alt="ABCI flow diagram",
                        width="100%",
                        max_width="960px",
                        border_radius="12px",
                        align_self="center",
                    ),
                ),
            ),
        ),
    )


__all__ = ["abci_page"]
