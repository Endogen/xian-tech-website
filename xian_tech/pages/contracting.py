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
ALG_CONTRACT = """import beaker as bk
import pyteal as pt

class MyState:
    result = bk.GlobalStateValue(pt.TealType.uint64)

app = bk.Application("Calculator", state=MyState())

@app.external
def add(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    add_result = a.get() + b.get()
    return pt.Seq(
        app.state.result.set(add_result),
        output.set(add_result)
    )

@app.external(read_only=True)
def read_result(*, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(app.state.result)

if __name__ == "__main__":
    spec = app.build()
    spec.export("artifacts")
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
pragma solidity ^0.8.20;

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

VYPER_CONTRACT = """# @version ^0.3.10
result: public(uint256)

@external
def add(a: uint256, b: uint256):
    self.result = a + b

@external
@view
def read_result() -> uint256:
    return self.result
"""

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
        "subtitle": "Side-by-side examples across Xian, Algorand, Solidity, and Vyper.",
        "category": "Technology",
        "badge": "Comparison",
        "href": "/contracting",
        "keywords": ["Comparison", "Xian", "Algorand", "Solidity", "Vyper"],
    },
]


def contracting_page() -> rx.Component:
    """Python smart contract engine overview."""
    def choice_card(title: str, body: str, detail: str, icon: str) -> rx.Component:
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
                rx.text(detail, size="2", color=TEXT_MUTED, line_height="1.6"),
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
                    rx.tabs.trigger("Xian", value="xian", color_scheme="green"),
                    rx.tabs.trigger("Algorand", value="algorand", color_scheme="green"),
                    rx.tabs.trigger("Solidity", value="solidity", color_scheme="green"),
                    rx.tabs.trigger("Vyper", value="vyper", color_scheme="green"),
                    gap="0.75rem",
                    wrap="wrap",
                ),
                rx.tabs.content(
                    rx.vstack(
                        rx.code_block(
                            XIAN_CONTRACT,
                            language="python",
                            show_line_numbers=True,
                            wrap_long_lines=False,
                            custom_style={"overflowX": "auto"},
                            width="100%",
                        ),
                        rx.text(
                            "Deploy flow: send the Python contract itself; the submission contract deploys it, and execution stays Python-native throughout.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.6",
                        ),
                        spacing="3",
                        align_items="start",
                        width="100%",
                    ),
                    value="xian",
                    width="100%",
                ),
                rx.tabs.content(
                    rx.vstack(
                        rx.code_block(
                            ALG_CONTRACT,
                            language="python",
                            show_line_numbers=True,
                            wrap_long_lines=False,
                            custom_style={"overflowX": "auto"},
                            width="100%",
                        ),
                        rx.text(
                            "Deploy flow: run Python to generate TEAL + artifacts, pick the compiled output, and deploy via a UI that recompiles to AVM bytecode.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.6",
                        ),
                        spacing="3",
                        align_items="start",
                        width="100%",
                    ),
                    value="algorand",
                    width="100%",
                ),
                rx.tabs.content(
                    rx.vstack(
                        rx.code_block(
                            SOLIDITY_CONTRACT,
                            language="solidity",
                            show_line_numbers=True,
                            wrap_long_lines=False,
                            custom_style={"overflowX": "auto"},
                            width="100%",
                        ),
                        rx.text(
                            "Deploy flow: compile to EVM bytecode, deploy the contract, and call the public read function to return the stored result.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.6",
                        ),
                        spacing="3",
                        align_items="start",
                        width="100%",
                    ),
                    value="solidity",
                    width="100%",
                ),
                rx.tabs.content(
                    rx.vstack(
                        rx.code_block(
                            VYPER_CONTRACT,
                            language="python",
                            show_line_numbers=True,
                            wrap_long_lines=False,
                            custom_style={"overflowX": "auto"},
                            width="100%",
                        ),
                        rx.text(
                            "Deploy flow: compile with the Vyper compiler, deploy to an EVM chain, and call the public getter to read the result.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.6",
                        ),
                        spacing="3",
                        align_items="start",
                        width="100%",
                    ),
                    value="vyper",
                    width="100%",
                ),
                default_value="xian",
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
