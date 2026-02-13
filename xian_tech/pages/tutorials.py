import reflex as rx

from ..components.common import (
    code_block,
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
    BORDER_COLOR,
    SURFACE,
    SURFACE_HOVER,
    TEXT_MUTED,
    TEXT_PRIMARY,
)

SEARCH_SECTIONS = [
    {
        "title": "Tutorials & First Steps",
        "subtitle": "Step-by-step guides for building on the Xian stack.",
        "category": "Developers",
        "badge": "Page",
        "href": "/tutorials",
        "keywords": ["Tutorials", "Getting Started", "Guides", "Developers"],
    }
]

TOKEN_STEP_1 = """balances = Hash(default_value=0)
allowances = Hash(default_value=0)
metadata = Hash()
operator = Variable()"""

TOKEN_STEP_2 = """@construct
def seed():
    metadata['token_name'] = 'Sample Token'
    metadata['token_symbol'] = 'SMP'
    metadata['token_logo_url'] = ''
    metadata['token_website'] = ''
    metadata['operator'] = ctx.caller
    balances[ctx.caller] = 1_000_000"""

TOKEN_STEP_3 = """@export
def transfer(amount: float, to: str):
    assert balances[ctx.caller] >= amount, 'insufficient funds'
    balances[ctx.caller] -= amount
    balances[to] += amount"""

TOKEN_STEP_4 = """@export
def approve(amount: float, to: str):
    allowances[ctx.caller, to] = amount

@export
def transfer_from(amount: float, to: str, main_account: str):
    assert allowances[main_account, ctx.caller] >= amount, 'not approved'
    assert balances[main_account] >= amount, 'insufficient funds'
    allowances[main_account, ctx.caller] -= amount
    balances[main_account] -= amount
    balances[to] += amount"""

TOKEN_STEP_5 = """@export
def change_metadata(key: str, value):
    assert ctx.caller == metadata['operator'], 'operator only'
    metadata[key] = value"""


def tutorials_page() -> rx.Component:
    """Tutorials page."""
    def concept_card(title: str, body: str, points: list[str], icon: str) -> rx.Component:
        return icon_watermark_hover_card(
            rx.flex(
                hover_icon_chip(icon),
                rx.heading(title, size="5", weight="bold", color=TEXT_PRIMARY),
                direction={"base": "row", "lg": "column"},
                align={"base": "center", "lg": "start"},
                spacing="3",
            ),
            rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
            rx.vstack(
                *[rx.text(f"• {item}", size="3", color=TEXT_MUTED, line_height="1.7") for item in points],
                spacing="1",
                align_items="start",
                width="100%",
            ),
            icon=icon,
            padding="2rem",
        )

    def step_block(step: str, title: str, body: str, snippet: str | None = None) -> rx.Component:
        children = [
            rx.hstack(
                rx.box(
                    rx.text(step, size="2", weight="bold", color=ACCENT),
                    padding="0.25rem 0.6rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="6px",
                ),
                rx.heading(title, size="5", weight="bold", color=TEXT_PRIMARY),
                spacing="3",
                align_items="center",
            ),
            rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
        ]
        if snippet:
            children.append(code_block(snippet))
        return rx.box(
            rx.vstack(
                *children,
                spacing="3",
                align_items="start",
                width="100%",
            ),
            width="100%",
        )

    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("TUTORIALS", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Tutorials & First Steps",
                    size="8",
                    color=TEXT_PRIMARY,
                    weight="bold",
                    line_height="1.2",
                ),
                rx.text(
                    "Learn the core ideas behind Xian contracting and follow a step-by-step walkthrough to build a "
                    "standards-compliant token contract.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    width="100%",
                ),
                spacing="6",
                align_items="start",
            )
        ),
        section(
            section_panel(
                rx.vstack(
                    rx.flex(
                        linked_heading(
                            "Contracting Fundamentals",
                            size="6",
                            color=TEXT_PRIMARY,
                            weight="bold",
                        ),
                        rx.hstack(
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="book_open", size=18),
                                    rx.text("Cheat Sheet", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://docs.xian.org/contracts/cheat-sheet",
                                is_external=True,
                                color=TEXT_MUTED,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="scroll_text", size=18),
                                    rx.text("Functions", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://docs.xian.org/contracts/functions",
                                is_external=True,
                                color=TEXT_MUTED,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="layers", size=18),
                                    rx.text("Context", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://docs.xian.org/contracts/context",
                                is_external=True,
                                color=TEXT_MUTED,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="gauge", size=18),
                                    rx.text("Stamps", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://docs.xian.org/contracts/concepts/stamps",
                                is_external=True,
                                color=TEXT_MUTED,
                                _hover={"color": ACCENT},
                            ),
                            spacing="4",
                            align_items="center",
                            wrap="wrap",
                        ),
                        direction={"base": "column", "lg": "row"},
                        align_items={"base": "start", "lg": "center"},
                        justify="between",
                        gap="0.75rem",
                        width="100%",
                    ),
                    rx.text(
                        "These are the concepts you need before shipping production contracts.",
                        size="3",
                        color=TEXT_MUTED,
                    ),
                    spacing="2",
                    align_items="start",
                    width="100%",
                ),
                rx.grid(
                    concept_card(
                        "Contract structure",
                        "Every contract is a module with a clear public API.",
                        [
                            "Names must start with con_, be lowercase, and match ^con_[a-z][a-z0-9_]*$.",
                            "Use @export for public functions, @construct for one-time initialization.",
                        ],
                        "code",
                    ),
                    concept_card(
                        "State & storage",
                        "Persist contract state with deterministic storage primitives.",
                        [
                            "Variable stores a single value (total = Variable()).",
                            "Hash stores key-value state (balances = Hash(default_value=0)).",
                            "Use .set() / .get() for Variables, and indexing for Hash (total.set(100), balances[ctx.caller] = 10).",
                            "ForeignHash and ForeignVariable read state from other contracts.",
                        ],
                        "database",
                    ),
                    concept_card(
                        "Execution context",
                        "Context tells you who is calling and which contract is running.",
                        [
                            "ctx.caller changes with each contract hop; ctx.signer stays constant.",
                            "ctx.this is the current contract identity; ctx.owner can gate calls.",
                        ],
                        "user",
                    ),
                    concept_card(
                        "Deterministic Python",
                        "Contracts run in a restricted Python subset for safety.",
                        [
                            "Classes are not allowed; use dictionaries for structured data.",
                            "Many built-ins are removed and exceptions are heavily restricted.",
                        ],
                        "shield",
                    ),
                    concept_card(
                        "Stamps & limits",
                        "Execution is metered to keep contracts safe and predictable.",
                        [
                            "Reads are free; writes cost stamps based on bytes written.",
                            "If stamps run out, execution reverts. Limits apply to memory and calls.",
                        ],
                        "gauge",
                    ),
                    columns={"base": "1fr", "lg": "repeat(2, minmax(0, 1fr))"},
                    gap="1.5rem",
                    width="100%",
                ),
            )
        ),
        section(
            section_panel(
                rx.vstack(
                    rx.flex(
                        linked_heading(
                            "Token Contract Walkthrough (XSC0001)",
                            size="6",
                            color=TEXT_PRIMARY,
                            weight="bold",
                        ),
                        rx.hstack(
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="book_open", size=18),
                                    rx.text("Token Standard", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://docs.xian.org/contracts/standards/xsc0001",
                                is_external=True,
                                color=TEXT_MUTED,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="list_checks", size=18),
                                    rx.text("Creating a Token", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://docs.xian.org/tutorials/creating-a-token",
                                is_external=True,
                                color=TEXT_MUTED,
                                _hover={"color": ACCENT},
                            ),
                            spacing="4",
                            align_items="center",
                            wrap="wrap",
                        ),
                        direction={"base": "column", "lg": "row"},
                        align_items={"base": "start", "lg": "center"},
                        justify="between",
                        gap="0.75rem",
                        width="100%",
                    ),
                    rx.text(
                        "Start simple, then layer in the behaviors required by the token standard.",
                        size="3",
                        color=TEXT_MUTED,
                    ),
                    spacing="2",
                    align_items="start",
                    width="100%",
                ),
                rx.vstack(
                    step_block(
                        "Step 1",
                        "Define the core state",
                        "Set up balances, approvals, metadata, and operator storage. Use defaults so reads are safe.",
                        TOKEN_STEP_1,
                    ),
                    step_block(
                        "Step 2",
                        "Seed initial supply and metadata",
                        "The @construct function runs once on submission. Initialize metadata and mint supply to the creator.",
                        TOKEN_STEP_2,
                    ),
                    step_block(
                        "Step 3",
                        "Add transfers",
                        "Implement transfer with basic balance checks. This is the heart of the token flow.",
                        TOKEN_STEP_3,
                    ),
                    step_block(
                        "Step 4",
                        "Implement approvals and transfer_from",
                        "Add allowances so third parties can move funds on behalf of owners.",
                        TOKEN_STEP_4,
                    ),
                    step_block(
                        "Step 5",
                        "Allow metadata updates",
                        "Only the operator should be able to change token metadata.",
                        TOKEN_STEP_5,
                    ),
                    step_block(
                        "Step 6",
                        "Layer on production guardrails",
                        "Add event logging, metadata validation, supply caps, and test coverage to match your launch needs.",
                    ),
                    spacing="6",
                    align_items="start",
                    width="100%",
                ),
            )
        ),
    )


__all__ = ["tutorials_page"]
