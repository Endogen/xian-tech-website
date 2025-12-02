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
                    "Xian’s contracting engine runs native Python—no transpilers or alternate DSLs—making audits and upgrades faster. "
                    "Deterministic execution, metered by stamps, keeps runtime predictable.",
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
