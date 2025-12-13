import reflex as rx

from ..components.common import code_block, page_layout, section
from ..data import BDS_COMPONENTS
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
            rx.flex(
                *[
                    rx.box(
                        rx.vstack(
                            rx.text(item["icon"], size="8", line_height="1"),
                            rx.heading(item["title"], size="5", weight="bold", color=TEXT_PRIMARY),
                            rx.text(item["description"], size="3", color=TEXT_MUTED, line_height="1.7"),
                            spacing="3",
                            align_items="start",
                        ),
                        padding="2.5rem",
                        background=SURFACE,
                        border=f"1px solid {BORDER_COLOR}",
                        border_radius="14px",
                        transition="background-position 0.4s ease, box-shadow 0.3s ease, border-color 0.2s ease",
                        height="100%",
                        width="100%",
                        min_width="0",
                        style={
                            "backgroundImage": "linear-gradient(135deg, rgba(0, 179, 92, 0.08), rgba(0, 179, 92, 0))",
                            "backgroundSize": "200% 200%",
                            "backgroundPosition": "left center",
                        },
                        _hover={
                            "borderColor": ACCENT,
                            "backgroundColor": SURFACE_HOVER,
                            "boxShadow": f"0 18px 32px {ACCENT_SOFT}",
                            "backgroundPosition": "right center",
                        },
                    )
                    for item in BDS_COMPONENTS
                ],
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
