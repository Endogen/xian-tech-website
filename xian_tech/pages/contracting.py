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
    BORDER_COLOR,
    SURFACE,
    SURFACE_HOVER,
    TEXT_MUTED,
    TEXT_PRIMARY,
)
ALGORAND_CONTRACT = """import algopy
from algopy import arc4

class Calculator(algopy.ARC4Contract):
    def __init__(self) -> None:
        self.result = algopy.UInt64(0)

    @arc4.abimethod
    def add(self, a: arc4.UInt64, b: arc4.UInt64) -> arc4.UInt64:
        self.result = a.native + b.native
        return arc4.UInt64(self.result)

    @arc4.abimethod
    def read_result(self) -> arc4.UInt64:
        return arc4.UInt64(self.result)
"""

XIAN_CONTRACT = """result = Variable()

@export
def add(a: int, b: int):
    result.set(a + b)

@export
def read_result():
    return result.get()
"""

SOLIDITY_CONTRACT = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.34;

contract Calculator {
    uint256 public result;

    function add(uint256 a, uint256 b) external {
        result = a + b;
    }

    function readResult() external view returns (uint256) {
        return result;
    }
}
"""

VYPER_CONTRACT = """#pragma version ~=0.4.0
result: public(uint256)

@external
def add(a: uint256, b: uint256):
    self.result = a + b

@external
@view
def read_result() -> uint256:
    return self.result
"""

MOVE_CONTRACT = """module 0x42::calculator {
    use std::signer;

    struct Result has key {
        value: u64,
    }

    public entry fun init(account: &signer) {
        move_to(account, Result { value: 0 });
    }

    public entry fun add(account: &signer, a: u64, b: u64) acquires Result {
        let addr = signer::address_of(account);
        let result = borrow_global_mut<Result>(addr);
        result.value = a + b;
    }

    public fun read_result(account: address): u64 acquires Result {
        borrow_global<Result>(account).value
    }
}
"""

TACT_CONTRACT = """message Add {
    a: Int as uint64;
    b: Int as uint64;
}

contract Calculator {
    result: Int as uint64 = 0;

    receive(msg: Add) {
        self.result = msg.a + msg.b;
    }

    get fun readResult(): Int {
        return self.result;
    }
}
"""

ANCHOR_CONTRACT = """use anchor_lang::prelude::*;

declare_id!("11111111111111111111111111111111");

#[program]
pub mod calculator {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        ctx.accounts.calculator.result = 0;
        Ok(())
    }

    pub fn add(ctx: Context<Update>, a: u64, b: u64) -> Result<()> {
        ctx.accounts.calculator.result = a.saturating_add(b);
        Ok(())
    }
}

#[account]
pub struct CalculatorAccount {
    pub result: u64,
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = signer, space = 8 + 8)]
    pub calculator: Account<'info, CalculatorAccount>,
    #[account(mut)]
    pub signer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub calculator: Account<'info, CalculatorAccount>,
}
"""

CLARITY_CONTRACT = """(define-data-var result uint u0)

(define-public (add (a uint) (b uint))
  (begin
    (var-set result (+ a b))
    (ok (var-get result))))

(define-read-only (read-result)
  (var-get result))
"""

CONTRACT_EXAMPLES = [
    {
        "label": "Xian",
        "value": "xian",
        "language": "python",
        "code": XIAN_CONTRACT,
        "deploy_flow": (
            "Deploy flow: submit the Python contract directly; execution stays Python-native "
            "throughout deployment and runtime."
        ),
    },
    {
        "label": "Algorand Python",
        "value": "algorand_python",
        "language": "python",
        "code": ALGORAND_CONTRACT,
        "deploy_flow": (
            "Deploy flow: compile ARC-4 Python to AVM artifacts with AlgoKit, deploy the application, "
            "then call ABI methods."
        ),
    },
    {
        "label": "Solidity",
        "value": "solidity",
        "language": "solidity",
        "code": SOLIDITY_CONTRACT,
        "deploy_flow": (
            "Deploy flow: compile to EVM bytecode, deploy the contract, and call the public read function "
            "to return the stored result."
        ),
    },
    {
        "label": "Vyper",
        "value": "vyper",
        "language": "python",
        "code": VYPER_CONTRACT,
        "deploy_flow": (
            "Deploy flow: compile with the Vyper compiler, deploy to an EVM chain, and call the public "
            "getter to read the result."
        ),
    },
    {
        "label": "Move",
        "value": "move",
        "language": "rust",
        "code": MOVE_CONTRACT,
        "deploy_flow": (
            "Deploy flow: publish the Move package, call entry functions to mutate state, and call "
            "a read function for the stored value."
        ),
    },
    {
        "label": "TON (Tact)",
        "value": "ton_tact",
        "language": "solidity",
        "code": TACT_CONTRACT,
        "deploy_flow": (
            "Deploy flow: compile Tact to TON VM artifacts, deploy the contract, send typed messages, "
            "and query the getter method."
        ),
    },
    {
        "label": "Rust (Anchor)",
        "value": "rust_anchor",
        "language": "rust",
        "code": ANCHOR_CONTRACT,
        "deploy_flow": (
            "Deploy flow: build and deploy the Anchor program, send instructions to update the account, "
            "and read the stored result from account state."
        ),
    },
    {
        "label": "Clarity",
        "value": "clarity",
        "language": "lisp",
        "code": CLARITY_CONTRACT,
        "deploy_flow": (
            "Deploy flow: publish the Clarity contract on Stacks, call the public function for state "
            "updates, and call the read-only function to fetch the result."
        ),
    },
]

HIGHLIGHTS = [
    {
        "title": "Python-first by design",
        "icon": "code",
        "body": (
            "No custom DSLs or transpilers. Contracts are idiomatic Python, making audits and upgrades straightforward "
            "and letting teams use the language they already know."
        ),
        "detail": (
            "Execution stays on the standard Python VM end to end, so there is no translation layer where semantics can drift "
            "or opaque behavior can creep in."
        ),
    },
    {
        "title": "Native value semantics",
        "icon": "scale",
        "body": (
            "We avoid bespoke integer abstractions for balances. The engine stays Python-native rather than inventing "
            "a special-purpose blockchain language."
        ),
        "detail": (
            "Decimal-friendly value types keep amounts natural to read and reason about. Solidity-style integer scaling forces "
            "manual conversions and can still introduce precision pitfalls."
        ),
    },
    {
        "title": "Deterministic fees",
        "icon": "calculator",
        "body": (
            "Fees are deterministic and compute-based, so outcomes and costs can be simulated before a transaction is sent."
        ),
        "detail": (
            "Stamps map directly to the computation required for contract execution. A dry run yields both the expected result "
            "and the exact fee, so you can verify the outcome or opt out before spending."
        ),
    },
    {
        "title": "Standalone & portable",
        "icon": "plug",
        "body": (
            "The contracting library can run independently and could integrate with other node systems—not just CometBFT—"
            "or power entirely different use cases."
        ),
        "detail": (
            "You can embed the engine inside a local app, test harness, or other runtime. Blockchain integration is a choice, "
            "not a requirement."
        ),
    },
    {
        "title": "Upgradable patterns",
        "icon": "puzzle",
        "body": (
            "With the right design patterns, you can ship upgradable contracts when you need them—without forcing "
            "complexity on contracts that don't."
        ),
        "detail": (
            "Contracts can call other contracts, and routing through a registry lets you swap implementations. Bind that switch "
            "to a multisig so upgrades only happen with explicit consensus."
        ),
    },
    {
        "title": "Event-driven observability",
        "icon": "activity",
        "body": (
            "Contracts emit structured, typed events so external systems can track state changes without polling."
        ),
        "detail": (
            "Index by sender, receiver, or any custom field to power real-time dashboards, analytics, or reactive workflows "
            "that respond to contract activity."
        ),
    },
]

SEARCH_SECTIONS = [
    {
        "title": "Pure Python Smart Contracts",
        "subtitle": "Deterministic, stamp-metered execution with native Python contracts.",
        "category": "Technology",
        "badge": "Page",
        "href": "/contracting",
        "keywords": ["Python", "Contracts", "Deterministic", "Smart contracts"],
    },
    *[
        {
            "title": item["title"],
            "subtitle": item["body"],
            "category": "Technology",
            "badge": "Highlight",
            "href": "/contracting",
            "keywords": [item["title"]],
        }
        for item in HIGHLIGHTS
    ],
    {
        "title": "Compare Contracting Platforms",
        "subtitle": (
            "Side-by-side examples across Xian, Algorand Python, Solidity, Vyper, "
            "Move, TON (Tact), Rust (Anchor), and Clarity."
        ),
        "category": "Technology",
        "badge": "Comparison",
        "href": "/contracting",
        "keywords": [
            "Comparison",
            "Xian",
            "Algorand Python",
            "Solidity",
            "Vyper",
            "Move",
            "TON",
            "Tact",
            "Rust",
            "Anchor",
            "Clarity",
        ],
    },
]


def contracting_page() -> rx.Component:
    """Python smart contract engine overview."""
    def choice_card(title: str, body: str, detail: str, icon: str) -> rx.Component:
        return icon_watermark_hover_card(
            rx.flex(
                hover_icon_chip(icon),
                rx.heading(title, size="5", weight="bold", color=TEXT_PRIMARY),
                direction={"base": "row", "lg": "column"},
                align={"base": "center", "lg": "start"},
                spacing="3",
            ),
            rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
            rx.text(detail, size="2", color=TEXT_MUTED, line_height="1.6"),
            icon=icon,
            padding="2rem",
        )

    def timeline_item(year: str, text: str) -> rx.Component:
        return rx.hstack(
            rx.box(
                rx.text(year, size="2", weight="bold", color=ACCENT),
                padding="0.2rem 0.6rem",
                background=ACCENT_SOFT,
                border=f"1px solid {ACCENT_GLOW}",
                border_radius="6px",
            ),
            rx.text(text, size="3", color=TEXT_MUTED, line_height="1.7"),
            spacing="3",
            align_items="center",
            width="100%",
        )

    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("CONTRACTING", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Pure Python Smart Contracts",
                    size="8",
                    color=TEXT_PRIMARY,
                    line_height="1.15",
                    weight="bold",
                ),
                rx.text(
                    "The heart of Xian is a native Python contracting engine—no transpilers, no second-class runtimes. Deterministic, stamp-metered execution keeps performance predictable while making audits and upgrades straightforward.",
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
                    linked_heading("Contracting Engine", size="6", color=TEXT_PRIMARY, weight="bold"),
                    rx.hstack(
                        rx.link(
                            rx.hstack(
                                rx.icon(tag="github", size=18),
                                rx.text("Repo", size="3"),
                                spacing="2",
                                align_items="center",
                            ),
                            href="https://github.com/xian-technology/xian-contracting",
                            is_external=True,
                            color=TEXT_MUTED,
                            _hover={"color": ACCENT},
                        ),
                        rx.link(
                            rx.hstack(
                                rx.icon(tag="book_open", size=18),
                                rx.text("DeepWiki", size="3"),
                                spacing="2",
                                align_items="center",
                            ),
                            href="https://deepwiki.com/xian-technology/xian-contracting",
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
                            href="https://docs.xian.technology",
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
                    "The contracting engine executes pure Python contracts with deterministic rules and a stamp-metered "
                    "budget. It keeps developer ergonomics high without compromising on predictable execution.",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    width="100%",
                ),
                rx.grid(
                    *[
                        choice_card(item["title"], item["body"], item["detail"], item["icon"])
                        for item in HIGHLIGHTS
                    ],
                    columns={"base": "repeat(1, minmax(0, 1fr))", "lg": "repeat(3, minmax(0, 1fr))"},
                    spacing="4",
                    width="100%",
                    align="stretch",
                ),
            ),
            padding_top="0",
        ),
        section(
            rx.vstack(
                linked_heading("Compare Contracting Platforms", size="6", color=TEXT_PRIMARY, weight="bold"),
                rx.text(
                    "Let’s compare a simple add-and-read contract across stacks:",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                spacing="2",
                align_items="start",
                width="100%",
            ),
            rx.tabs.root(
                rx.tabs.list(
                    *[
                        rx.tabs.trigger(
                            example["label"],
                            value=example["value"],
                            color_scheme="green",
                        )
                        for example in CONTRACT_EXAMPLES
                    ],
                    gap="0.75rem",
                    wrap="wrap",
                ),
                *[
                    rx.tabs.content(
                        rx.vstack(
                            rx.code_block(
                                example["code"],
                                language=example["language"],
                                show_line_numbers=True,
                                wrap_long_lines=False,
                                custom_style={"overflowX": "auto"},
                                width="100%",
                            ),
                            rx.text(
                                example["deploy_flow"],
                                size="3",
                                color=TEXT_MUTED,
                                line_height="1.6",
                            ),
                            spacing="3",
                            align_items="start",
                            width="100%",
                        ),
                        value=example["value"],
                        width="100%",
                    )
                    for example in CONTRACT_EXAMPLES
                ],
                default_value=CONTRACT_EXAMPLES[0]["value"],
                width="100%",
                min_width="0",
            ),
            rx.vstack(
                linked_heading("Python Adoption", size="5", color=TEXT_PRIMARY, weight="bold"),
                rx.text(
                    "Both Ethereum and Algorand introduced Python-like workflows after developers struggled with the "
                    "native contract languages. Algorand’s path shows a clear, incremental shift toward Python:",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                rx.vstack(
                    timeline_item("2019", "Algorand launched with TEAL only, an assembly-like language."),
                    timeline_item("2020", "PyTeal arrived as a Python wrapper/compiler to make TEAL development easier."),
                    timeline_item("2025", "Algorand Python shipped as a next-generation, native Python experience."),
                    spacing="2",
                    align_items="start",
                    width="100%",
                ),
                rx.text(
                    "Python support arrived about a year after launch, starting as a high-level abstraction over TEAL and "
                    "evolving into a native experience over time.",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                rx.text(
                    "A side effect of pure Python contracts is that AI assistants can draft nearly correct smart contracts "
                    "on the first try when guided by the ",
                    rx.link(
                        "AI Contracting Guide",
                        href="/tooling#ai-guides",
                        color=ACCENT,
                        _hover={"color": ACCENT},
                    ),
                    ", which accelerates adoption and shortens development cycles.",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                spacing="4",
                align_items="start",
                width="100%",
                margin_top="3rem",
            ),
            padding_top="0",
        ),
    )


__all__ = ["contracting_page"]
