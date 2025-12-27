import reflex as rx

from ..components.common import code_block, page_layout, section, terminal_prompt
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
    return result
"""

HIGHLIGHTS = [
    {
        "title": "Python-first by design",
        "icon": "🐍",
        "body": (
            "No custom DSLs or transpilers. Contracts are idiomatic Python, making audits and upgrades straightforward "
            "and letting teams use the language they already know."
        ),
    },
    {
        "title": "Native value semantics",
        "icon": "⚖️",
        "body": (
            "We avoid bespoke integer abstractions for balances. The engine stays Python-native rather than inventing "
            "a special-purpose blockchain language."
        ),
    },
    {
        "title": "Standalone & portable",
        "icon": "🔌",
        "body": (
            "The contracting library can run independently and could integrate with other node systems—not just CometBFT—"
            "or power entirely different use cases."
        ),
    },
    {
        "title": "Upgradable patterns",
        "icon": "🧩",
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
                "Let’s compare a simple add-and-read contract on Algorand versus Xian:",
                size="3",
                color=TEXT_MUTED,
                line_height="1.7",
            padding_bottom="0.5rem",
        ),
            rx.grid(
                rx.vstack(
                    rx.heading("Algorand Contract", size="5", color=TEXT_PRIMARY, weight="bold"),
                    code_block(ALG_CONTRACT),
                    rx.text(
                        "Deploy flow: run Python to generate TEAL + artifacts, pick the compiled output, and deploy via a UI that recompiles to AVM bytecode.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.6",
                    ),
                    spacing="3",
                    align_items="start",
                ),
                rx.vstack(
                    rx.heading("Xian Contract", size="5", color=TEXT_PRIMARY, weight="bold"),
                    code_block(XIAN_CONTRACT),
                    rx.text(
                        "Deploy flow: send the Python contract itself; the submission contract deploys it, and execution stays Python-native throughout.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.6",
                    ),
                    spacing="3",
                    align_items="start",
                ),
                template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
                gap="1.5rem",
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
                                    rx.text(item["icon"], size="7", line_height="1"),
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
