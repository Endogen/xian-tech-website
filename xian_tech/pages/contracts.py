import reflex as rx

from ..components.common import code_block, page_layout, section, terminal_prompt
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
                style={"paddingBottom": "0.5rem"},
            ),
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.heading("Contract on Algorand", size="5", color=TEXT_PRIMARY, weight="bold"),
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
                    padding="2.5rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("Contract on Xian", size="5", color=TEXT_PRIMARY, weight="bold"),
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
                    padding="2.5rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
                gap="1.5rem",
            ),
            style={"paddingTop": "0"},
        ),
        section(
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.heading("Deterministic runtime", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Sandboxed Executor enforces stamp budgets, restricted imports, and owner checks for predictable execution.",
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
                        rx.heading("Simple developer flow", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Write @export functions in Python, submit via the submission contract, and interact with stateful variables and hashes directly.",
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
                        rx.heading("Stamped economics", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Stamp consumption is debited per call; rewards route to validators, the foundation, and contract developers.",
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
            style={"paddingTop": "0"},
        ),
        section(
            rx.vstack(
                rx.heading("Tiny contract sketch", size="6", color=TEXT_PRIMARY, weight="bold"),
                code_block(
                    "@export\n"
                    "def transfer(to: str, amount: int):\n"
                    "    assert amount > 0\n"
                    "    balances[to] += amount\n"
                ),
                rx.vstack(
                    terminal_prompt("pip install xian-py"),
                    terminal_prompt("xian init my-contract"),
                    terminal_prompt("xian deploy"),
                    spacing="3",
                    width="100%",
                ),
                spacing="5",
                align_items="start",
            )
        ),
    )


__all__ = ["contracts_page"]
