import reflex as rx

from ..components.common import code_block, page_layout, section, terminal_prompt
from ..data import TECHNOLOGY_TRACKS
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_HOVER,
    ACCENT_SOFT,
    BORDER_BRIGHT,
    BORDER_COLOR,
    PRIMARY_BG,
    SURFACE,
    SURFACE_BRIGHT,
    SURFACE_HOVER,
    TEXT_MUTED,
    TEXT_PRIMARY,
)


def architecture_card(title: str, description: str, badge: str) -> rx.Component:
    """Reusable architecture card."""
    return rx.box(
        rx.vstack(
            rx.badge(badge, color_scheme="green", variant="soft", size="2"),
            rx.heading(title, size="5", color=TEXT_PRIMARY, weight="bold"),
            rx.text(description, size="3", color=TEXT_MUTED, line_height="1.7"),
            spacing="3",
            align_items="start",
        ),
        padding="2rem",
        background=SURFACE,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="14px",
        height="100%",
    )


def architecture_overview() -> rx.Component:
    """Stack architecture overview."""
    return section(
        rx.vstack(
            rx.heading("How the stack fits together", size="7", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                "Consensus in Go, execution in Python: CometBFT handles node-to-node state replication, a Python ABCI bridges into the contracting engine, BDS streams indexed data into PostgreSQL, and HDF5 captures on-disk state snapshots. Tooling (xian-py) talks to both contracts and data services.",
                size="4",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            rx.grid(
                rx.vstack(
                    architecture_card(
                        "CometBFT Node",
                        "Go-based consensus engine that gossips transactions, finalizes blocks, and replicates state across peers.",
                        "Go • Consensus",
                    ),
                    rx.center(rx.text("↓", size="6", color=ACCENT, weight="bold")),
                    architecture_card(
                        "Custom ABCI (Python)",
                        "Python ABCI app connects CometBFT to the execution layer: CheckTx, FinalizeBlock, Commit, and proposal hooks.",
                        "Python • ABCI",
                    ),
                    rx.center(rx.text("↓", size="6", color=ACCENT, weight="bold")),
                    architecture_card(
                        "Contracting Engine",
                        "Pure Python smart contract runtime embedded in the ABCI app for deterministic execution, metering, and state writes.",
                        "Python • Runtime",
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.vstack(
                    architecture_card(
                        "Blockchain Data Service (BDS)",
                        "Python service integrated with the ABCI app to stream chain state into PostgreSQL and expose it via GraphQL.",
                        "Python • Data",
                    ),
                    architecture_card(
                        "PostgreSQL",
                        "Durable database backing BDS for fast queries across blocks, contracts, and derived views.",
                        "Storage",
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.vstack(
                    architecture_card(
                        "HDF5 State Snapshots",
                        "On-disk state persistence via HDF5 for fast local reads, backups, and operational recovery alongside live ABCI state.",
                        "Storage",
                    ),
                    architecture_card(
                        "xian-py SDK & Tooling",
                        "Python SDK for deploying and interacting with contracts and querying data services; fits directly into Python apps and CLIs.",
                        "Tools",
                    ),
                    spacing="3",
                    width="100%",
                ),
                template_columns={"base": "1fr", "md": "repeat(2, 1fr)", "lg": "repeat(3, 1fr)"},
                gap="2rem",
                width="100%",
            ),
            spacing="5",
            align_items="start",
        ),
        style={"paddingBottom": "3rem"},
    )


def architecture_diagram() -> rx.Component:
    """Visual architecture diagram."""
    return section(
        rx.vstack(
            rx.heading("Architecture diagram", size="6", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                "High-level flow from consensus to execution, data services, and SDKs.",
                size="3",
                color=TEXT_MUTED,
                line_height="1.6",
            ),
            rx.box(
                rx.image(
                    src="/architecture.svg",
                    alt="Xian architecture diagram",
                    width="100%",
                    border_radius="14px",
                ),
                width="100%",
                padding_top="1.5rem",
            ),
            spacing="3",
            align_items="start",
        )
    )


def roadmap_section() -> rx.Component:
    """Roadmap section with cards."""
    return section(
        rx.link(
            rx.box(
                rx.vstack(
                    rx.heading("Xian Technology Roadmap", size="7", color=TEXT_PRIMARY, weight="bold"),
                    rx.text(
                        "Transparent milestones for the contracting library, node, and ecosystem tooling.",
                        size="4",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    rx.grid(
                        rx.box(
                            rx.vstack(
                                rx.text("🧱", size="7", line_height="1"),
                                rx.text("In Progress", size="4", weight="bold", color=TEXT_PRIMARY),
                                rx.text("Active engineering sprints", size="2", color=TEXT_MUTED, text_align="center"),
                                spacing="3",
                                align_items="center",
                            ),
                            padding="2rem",
                            background=SURFACE_BRIGHT,
                            border=f"1px solid {BORDER_BRIGHT}",
                            border_radius="10px",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text("🧪", size="7", line_height="1"),
                                rx.text("Testing", size="4", weight="bold", color=TEXT_PRIMARY),
                                rx.text("Formal verification & audits", size="2", color=TEXT_MUTED, text_align="center"),
                                spacing="3",
                                align_items="center",
                            ),
                            padding="2rem",
                            background=SURFACE_BRIGHT,
                            border=f"1px solid {BORDER_BRIGHT}",
                            border_radius="10px",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text("✅", size="7", line_height="1"),
                                rx.text("Completed", size="4", weight="bold", color=TEXT_PRIMARY),
                                rx.text("Shipped improvements", size="2", color=TEXT_MUTED, text_align="center"),
                                spacing="3",
                                align_items="center",
                            ),
                            padding="2rem",
                            background=SURFACE_BRIGHT,
                            border=f"1px solid {BORDER_BRIGHT}",
                            border_radius="10px",
                        ),
                        template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                        gap="1.5rem",
                        width="100%",
                    ),
                    rx.flex(
                        rx.flex(
                            rx.text("View Full Roadmap on GitHub", size="4", weight="medium", color=ACCENT),
                            rx.text("→", size="5", weight="bold", color=ACCENT),
                            gap="1rem",
                            align_items="center",
                        ),
                        justify="center",
                        width="100%",
                    ),
                    spacing="7",
                    align_items="start",
                    width="100%",
                ),
                padding="3.5rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
                width="100%",
                transition="all 0.3s ease",
                cursor="pointer",
                _hover={
                    "borderColor": ACCENT,
                    "backgroundColor": SURFACE_HOVER,
                    "transform": "translateY(-4px)",
                    "boxShadow": f"0 20px 40px {ACCENT_SOFT}",
                },
            ),
            href="https://github.com/orgs/xian-technology/projects/1",
            is_external=True,
            _hover={"textDecoration": "none"},
            width="100%",
        )
    )


def technology_page() -> rx.Component:
    """Technology route."""
    return page_layout(
        architecture_diagram(),
    )


__all__ = ["technology_page"]
