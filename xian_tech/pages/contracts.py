import reflex as rx

from ..components.common import page_layout, section, terminal_prompt
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_SOFT,
    BORDER_BRIGHT,
    BORDER_COLOR,
    PRIMARY_BG,
    SURFACE,
    SURFACE_HOVER,
    TEXT_MUTED,
    TEXT_PRIMARY,
)
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_SOFT,
    BORDER_BRIGHT,
    BORDER_COLOR,
    PRIMARY_BG,
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
    },
    {
        "title": "Native value semantics",
        "icon": "scale",
        "body": (
            "We avoid bespoke integer abstractions for balances. The engine stays Python-native rather than inventing "
            "a special-purpose blockchain language."
        ),
    },
    {
        "title": "Standalone & portable",
        "icon": "plug",
        "body": (
            "The contracting library can run independently and could integrate with other node systems—not just CometBFT—"
            "or power entirely different use cases."
        ),
    },
    {
        "title": "Upgradable patterns",
        "icon": "puzzle",
        "body": (
            "With the right design patterns, you can ship upgradable contracts when you need them—without forcing "
            "complexity on contracts that don't."
        ),
    },
]


def contracts_page() -> rx.Component:
    """Python smart contract engine overview."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("CONTRACTS", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading("Pure Python Smart Contracts", size="8", color=TEXT_PRIMARY, line_height="1.15", weight="bold"),
                rx.text(
                    "The heart of Xian is a native Python contracting engine—no transpilers, no second-class runtimes. Deterministic, stamp-metered execution keeps performance predictable while making audits and upgrades straightforward.",
                    size="4",
                    color=TEXT_MUTED,
                    max_width="900px",
                    line_height="1.7",
                ),
                spacing="5",
                align_items="start",
            )
        ),
        section(
            rx.text(
                "Let’s compare a simple add-and-read contract across stacks:",
                size="3",
                color=TEXT_MUTED,
                line_height="1.7",
                padding_bottom="0.5rem",
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
            ),
            padding_top="0",
        ),
        section(
            rx.vstack(
                rx.heading("Why the Xian contracting model?", size="6", color=TEXT_PRIMARY, weight="bold"),
                rx.grid(
                    *[
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(tag=item["icon"], size=28, color=ACCENT),
                                    rx.heading(item["title"], size="5", color=TEXT_PRIMARY, weight="bold"),
                                    align_items="center",
                                    gap="0.75rem",
                                ),
                                rx.text(item["body"], size="3", color=TEXT_MUTED, line_height="1.7"),
                                spacing="3",
                                align_items="start",
                            ),
                            padding="2.25rem",
                            background=SURFACE,
                            border=f"1px solid {BORDER_COLOR}",
                            border_radius="14px",
                            border_left=f"4px solid {ACCENT}",
                            transition="all 0.3s ease",
                            _hover={
                                "borderColor": BORDER_BRIGHT,
                                "backgroundColor": SURFACE_HOVER,
                            },
                            height="100%",
                        )
                        for item in HIGHLIGHTS
                    ],
                    template_columns={"base": "1fr", "md": "repeat(2, 1fr)", "lg": "repeat(4, 1fr)"},
                    gap="1.25rem",
                ),
                spacing="5",
                align_items="start",
            ),
            padding_top="0",
        ),
    )


__all__ = ["contracts_page"]
