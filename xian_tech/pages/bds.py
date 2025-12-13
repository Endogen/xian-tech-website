import reflex as rx

from ..components.common import code_block, page_layout, section
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_SOFT,
    BORDER_COLOR,
    PRIMARY_BG,
    SURFACE,
    TEXT_MUTED,
    TEXT_PRIMARY,
)


GRAPHQL_SAMPLE = """query RecentTransactions {
  transactions(orderBy: BLOCK_HEIGHT_DESC, first: 5) {
    edges {
      node {
        hash
        status
        blockHeight
        contract
        function
        stampsUsed
      }
    }
  }
}"""


def bds_page() -> rx.Component:
    """Blockchain Data Service overview."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("BDS", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading("Blockchain Data Service (BDS)", size="8", color=TEXT_PRIMARY, line_height="1.2", weight="bold"),
                rx.text(
                    "BDS is an optional component of the Python ABCI app. When enabled, it records every transaction—successful or failed—into PostgreSQL and exposes that data via a GraphQL API powered by PostGraphile.",
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
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.heading("Opt-in at install", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Enable BDS when provisioning the node. It runs inside the ABCI app—no extra daemon to manage.",
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
                    min_width="280px",
                    max_width="320px",
                    height="100%",
                    transition="all 0.3s ease",
                    _hover={
                        "borderColor": BORDER_COLOR,
                        "backgroundColor": SURFACE,
                    },
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("Complete transaction history", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Capture every transaction—successes and failures—with status, stamps, contract/function, and block metadata for auditing.",
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
                    min_width="280px",
                    max_width="320px",
                    height="100%",
                    transition="all 0.3s ease",
                    _hover={
                        "borderColor": BORDER_COLOR,
                        "backgroundColor": SURFACE,
                    },
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("PostgreSQL + GraphQL", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Data lands in PostgreSQL and is served through PostGraphile, so you can query with GraphQL or tap Postgres directly.",
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
                    min_width="280px",
                    max_width="320px",
                    height="100%",
                    transition="all 0.3s ease",
                    _hover={
                        "borderColor": BORDER_COLOR,
                        "backgroundColor": SURFACE,
                    },
                ),
                spacing="4",
                width="100%",
                wrap="nowrap",
                overflow_x="auto",
            ),
            style={"paddingTop": "0"},
        ),
        section(
            rx.vstack(
                rx.heading("Sample GraphQL query", size="6", color=TEXT_PRIMARY, weight="bold"),
                code_block(GRAPHQL_SAMPLE),
                rx.text(
                    "Query recent transactions with status, stamps, and contract metadata. Extend the schema as needed via PostGraphile or consume the underlying PostgreSQL tables for analytics.",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                ),
                spacing="4",
                align_items="start",
            )
        ),
    )


__all__ = ["bds_page"]
