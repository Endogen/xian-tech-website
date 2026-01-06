import reflex as rx

from ..components.common import page_layout, section, terminal_prompt
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


def tooling_page() -> rx.Component:
    """Tooling and interfaces overview."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("TOOLING", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading("Tooling to Build and Query", size="8", color=TEXT_PRIMARY, line_height="1.15", weight="bold"),
                rx.text(
                    "SDKs and data services keep builders productive: xian-py for contract lifecycles and BDS for GraphQL access to chain data.",
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
                        rx.heading("xian-py SDK", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Python-native SDK for initializing, deploying, and interacting with contracts. Works with the same language as the runtime.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        rx.vstack(
                            terminal_prompt("pip install xian-py"),
                            terminal_prompt("xian init my-contract"),
                            terminal_prompt("xian deploy"),
                            spacing="2",
                            width="100%",
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
                        rx.heading("Blockchain Data Service (BDS)", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "GraphQL interface to on-chain data for explorers, dashboards, and ops tooling. Optimized for predictable queries over block and contract state.",
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
                        rx.heading("Operational hooks", size="5", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Command palette and search index link directly to docs, GitHub, and community channels for faster collaboration.",
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
            padding_top="0",
        ),
        section(
            rx.vstack(
                rx.heading("Blockchain Data Service (BDS)", size="6", color=TEXT_PRIMARY, weight="bold"),
                rx.text(
                    "BDS is an optional component of the Python ABCI app. When enabled, it records every transaction into PostgreSQL and exposes that data via a GraphQL API powered by ",
                    rx.link("PostGraphile", href="https://www.graphile.org/postgraphile", is_external=True, color=ACCENT),
                    ".",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    width="100%",
                ),
                spacing="4",
                align_items="start",
            )
        ),
        section(
            rx.grid(
                *[
                    rx.box(
                        rx.vstack(
                            rx.flex(
                                rx.icon(tag=item["icon"], size=28, color=ACCENT),
                                rx.heading(item["title"], size="5", weight="bold", color=TEXT_PRIMARY),
                                direction={"base": "row", "lg": "column"},
                                align={"base": "center", "lg": "start"},
                                spacing="3",
                            ),
                            rx.text(item["description"], size="3", color=TEXT_MUTED, line_height="1.7"),
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
                    for item in BDS_COMPONENTS
                ],
                columns={
                    "base": "repeat(1, minmax(0, 1fr))",
                    "md": "repeat(2, minmax(0, 1fr))",
                    "lg": "repeat(3, minmax(0, 1fr))",
                },
                spacing="4",
                width="100%",
                align="stretch",
            ),
            padding_top="0",
        ),
        section(
            rx.vstack(
                rx.text(
                    "When GraphQL is enabled on a node, the GraphiQL UI is available at the node address under `/graphiql`. "
                    "For API access, use `/graphql`.",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    width="100%",
                ),
                rx.box(
                    rx.image(
                        src="/postgraphile.png",
                        alt="GraphiQL interface for BDS",
                        width="100%",
                        border_radius="12px",
                        object_fit="cover",
                        box_shadow=f"0 0 18px {ACCENT_SOFT}",
                    ),
                    width="100%",
                ),
                spacing="3",
                align_items="start",
            )
        ),
    )


__all__ = ["tooling_page"]
