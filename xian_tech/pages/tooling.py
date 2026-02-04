import reflex as rx

from ..components.common import linked_heading, page_layout, section, section_panel, subsection
from ..data import BDS_COMPONENTS
from ..state import State
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_SOFT,
    BORDER_COLOR,
    CODE_BG,
    SURFACE,
    SURFACE_HOVER,
    TEXT_MUTED,
    TEXT_PRIMARY,
)

SDK_INSTALL_COMMAND = "pip install xian-py"
SDK_WALLET_EXAMPLE = """from xian_py import Wallet

wallet = Wallet()

print(f"Address: {wallet.public_key}")
print(f"Private key: {wallet.private_key}")"""
SDK_BALANCE_EXAMPLE = """from xian_py import Xian, Wallet

wallet = Wallet()
xian = Xian("http://node-ip:26657", wallet=wallet)

balance = xian.get_balance(wallet.public_key)
print(f"Balance: {balance}")"""
SDK_SEND_EXAMPLE = """from xian_py import Xian, Wallet

wallet = Wallet()
xian = Xian("http://node-ip:26657", wallet=wallet)

result = xian.send(amount=10, to_address="recipient_address")
print(f"Transaction successful: {result['success']}")"""
SDK_CONTRACT_EXAMPLE = """from xian_py import Xian, Wallet

wallet = Wallet()
xian = Xian("http://node-ip:26657", wallet=wallet)

result = xian.send_tx(
    contract="currency",
    function="transfer",
    kwargs={"to": "recipient_address", "amount": 100},
)
print(f"Success: {result['success']}")"""
SDK_BDS_STATE_QUERY = """query QueryState {
  allStates(condition: {key: "currency.balances:some_address"}) {
    edges {
      node {
        key
        value
      }
    }
  }
}"""
SDK_BDS_EVENTS_QUERY = """query TransferEventQuery {
  allEvents(
    filter: {dataIndexed: {contains: {to: "some_address"}}}
    condition: {event: "Transfer"}
  ) {
    edges {
      node {
        id
        dataIndexed
        data
        contract
        event
        txHash
      }
    }
  }
}"""
MCP_QUICKSTART = """git clone https://github.com/xian-technology/xian-mcp-server.git
cd xian-mcp-server
docker build -t xian-mcp-server ."""
MCP_CONFIG_SNIPPET = """{
  "mcpServers": {
    "xian": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "xian-mcp-server"]
    }
  }
}"""

SEARCH_SECTIONS = [
    {
        "title": "Tooling to Build and Query",
        "subtitle": "SDKs and data services for contract lifecycles and chain data access.",
        "category": "Technology",
        "badge": "Page",
        "href": "/tooling",
        "keywords": ["Tooling", "SDK", "GraphQL", "BDS"],
    },
    {
        "title": "Python SDK",
        "subtitle": "xian-py for wallets, transactions, and contract workflows.",
        "category": "Technology",
        "badge": "Section",
        "href": "/tooling",
        "keywords": ["xian-py", "SDK", "Wallets", "Transactions"],
    },
    {
        "title": "Blockchain Data Service (BDS)",
        "subtitle": "PostgreSQL + GraphQL access to transaction and state history.",
        "category": "Technology",
        "badge": "Section",
        "href": "/tooling",
        "keywords": ["BDS", "GraphQL", "PostgreSQL", "PostGraphile"],
    },
    {
        "title": "MCP Server",
        "subtitle": "Local MCP server for AI assistants to interact with Xian wallets, contracts, and the DEX.",
        "category": "Technology",
        "badge": "Section",
        "href": "/tooling",
        "keywords": ["MCP", "AI assistants", "Wallets", "DEX"],
    },
    {
        "title": "AI Guides",
        "subtitle": "AI-ready guides for building and reviewing Xian contracts.",
        "category": "Technology",
        "badge": "Section",
        "href": "/tooling",
        "keywords": ["AI guides", "Contracting guide", "Smart contracts"],
    },
]


def _sdk_install_card() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("Install", size="3", weight="bold", color=TEXT_PRIMARY),
            rx.flex(
                rx.text("$", color=ACCENT, weight="bold", size="3"),
                rx.text(
                    SDK_INSTALL_COMMAND,
                    color=TEXT_PRIMARY,
                    size="3",
                    font_family="'SF Mono', 'Monaco', monospace",
                ),
                rx.spacer(),
                rx.button(
                    rx.box(
                        rx.icon(
                            tag="clipboard_copy",
                            size=18,
                            color="currentColor",
                            opacity=rx.cond(State.sdk_install_copied, "0", "1"),
                            transform=rx.cond(State.sdk_install_copied, "scale(0.85)", "scale(1)"),
                            transition="opacity 0.2s ease, transform 0.2s ease",
                            position="absolute",
                            top="0",
                            left="0",
                        ),
                        rx.icon(
                            tag="check",
                            size=18,
                            color="currentColor",
                            opacity=rx.cond(State.sdk_install_copied, "1", "0"),
                            transform=rx.cond(State.sdk_install_copied, "scale(1)", "scale(0.85)"),
                            transition="opacity 0.2s ease, transform 0.2s ease",
                            position="absolute",
                            top="0",
                            left="0",
                        ),
                        width="18px",
                        height="18px",
                        position="relative",
                        display="inline-block",
                    ),
                    on_click=State.copy_sdk_install_command,
                    variant="ghost",
                    cursor="pointer",
                    padding="0.35rem",
                    background_color="transparent",
                    color=rx.cond(State.sdk_install_copied, ACCENT, TEXT_MUTED),
                    border="none",
                    _hover={"color": ACCENT, "background_color": "transparent"},
                    aria_label="Copy install command",
                ),
                gap="0.75rem",
                padding="1rem 1.5rem",
                background=CODE_BG,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="8px",
                align_items="center",
                width="100%",
            ),
            spacing="3",
            align_items="start",
            width="100%",
        ),
        padding="1.75rem",
        background=SURFACE,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="14px",
        width="100%",
    )


def _feature_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon(tag="check", size=16, color=ACCENT),
        rx.text(text, size="3", color=TEXT_MUTED),
        spacing="2",
        align_items="center",
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
                rx.heading(
                    "Tooling to Build and Query",
                    size="8",
                    color=TEXT_PRIMARY,
                    line_height="1.15",
                    weight="bold",
                ),
                rx.text(
                    "SDKs and data services keep builders productive: xian-py for contract lifecycles and BDS for GraphQL access to chain data.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    width="100%",
                ),
                spacing="5",
                align_items="start",
            )
        ),
        section(
            section_panel(
                rx.vstack(
                    rx.flex(
                        linked_heading(
                            "Blockchain Data Service (BDS)",
                            size="6",
                            color=TEXT_PRIMARY,
                            weight="bold",
                        ),
                        rx.hstack(
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="github", size=18),
                                    rx.text("Repo", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://github.com/xian-technology/xian-py",
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
                        "BDS is an optional component of the Python ABCI app. When enabled, it records every transaction into PostgreSQL and exposes that data via a GraphQL API powered by ",
                        rx.link("PostGraphile", href="https://www.graphile.org/postgraphile", is_external=True, color=ACCENT),
                        ".",
                        size="4",
                        color=TEXT_MUTED,
                        line_height="1.7",
                        width="100%",
                    ),
                    spacing="3",
                    align_items="start",
                    width="100%",
                ),
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
                    subsection(
                        "Examples",
                        rx.tabs.root(
                            rx.tabs.list(
                                rx.tabs.trigger("Querying state", value="state", color_scheme="green"),
                                rx.tabs.trigger("Querying events", value="events", color_scheme="green"),
                                gap="0.75rem",
                                wrap="wrap",
                            ),
                            rx.tabs.content(
                                rx.code_block(
                                    SDK_BDS_STATE_QUERY,
                                    language="graphql",
                                    show_line_numbers=True,
                                    wrap_long_lines=False,
                                    custom_style={"overflowX": "auto"},
                                    width="100%",
                                ),
                                value="state",
                                width="100%",
                            ),
                            rx.tabs.content(
                                rx.vstack(
                                    rx.code_block(
                                        SDK_BDS_EVENTS_QUERY,
                                        language="graphql",
                                        show_line_numbers=True,
                                        wrap_long_lines=False,
                                        custom_style={"overflowX": "auto"},
                                        width="100%",
                                    ),
                                    rx.text(
                                        "The filter is optional if you want all Transfer events.",
                                        size="3",
                                        color=TEXT_MUTED,
                                        line_height="1.6",
                                    ),
                                    spacing="3",
                                    align_items="start",
                                    width="100%",
                                ),
                                value="events",
                                width="100%",
                            ),
                            default_value="state",
                            width="100%",
                            min_width="0",
                        ),
                        id="bds-examples",
                    ),
                    spacing="3",
                    align_items="start",
                    width="100%",
                    min_width="0",
                ),
            )
        ),
        section(
            section_panel(
                rx.vstack(
                    rx.flex(
                        linked_heading("Python SDK", size="6", color=TEXT_PRIMARY, weight="bold"),
                        rx.hstack(
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="github", size=18),
                                    rx.text("Repo", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://github.com/xian-technology/xian-py",
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
                        "xian-py is the Python SDK for interacting with Xian nodes, managing accounts, and deploying or "
                        "calling contracts from scripts and services.",
                        size="4",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    spacing="3",
                    align_items="start",
                    width="100%",
                ),
                rx.grid(
                    _sdk_install_card(),
                    rx.box(
                        rx.vstack(
                            rx.text("Features", size="3", weight="bold", color=TEXT_PRIMARY),
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(tag="check", size=16, color=ACCENT),
                                    rx.text("Create wallets, manage keys, and sign transactions.", size="3", color=TEXT_MUTED),
                                    spacing="2",
                                    align_items="center",
                                ),
                                rx.hstack(
                                    rx.icon(tag="check", size=16, color=ACCENT),
                                    rx.text("Deploy, call, and inspect Python smart contracts.", size="3", color=TEXT_MUTED),
                                    spacing="2",
                                    align_items="center",
                                ),
                                rx.hstack(
                                    rx.icon(tag="check", size=16, color=ACCENT),
                                    rx.text("Build and submit transactions with predictable outcomes.", size="3", color=TEXT_MUTED),
                                    spacing="2",
                                    align_items="center",
                                ),
                                rx.hstack(
                                    rx.icon(tag="check", size=16, color=ACCENT),
                                    rx.text("Query node data, balances, and contract state.", size="3", color=TEXT_MUTED),
                                    spacing="2",
                                    align_items="center",
                                ),
                                spacing="2",
                                align_items="start",
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                        padding="1.75rem",
                        background=SURFACE,
                        border=f"1px solid {BORDER_COLOR}",
                        border_radius="14px",
                        width="100%",
                    ),
                    columns={"base": "1", "lg": "2"},
                    spacing="4",
                    width="100%",
                    align="stretch",
                ),
                subsection(
                    "Examples",
                    rx.tabs.root(
                        rx.tabs.list(
                            rx.tabs.trigger("Create wallet", value="wallet", color_scheme="green"),
                            rx.tabs.trigger("Get balance", value="balance", color_scheme="green"),
                            rx.tabs.trigger("Send tokens", value="send", color_scheme="green"),
                            rx.tabs.trigger("Call contract", value="contract", color_scheme="green"),
                            gap="0.75rem",
                            wrap="wrap",
                        ),
                        rx.tabs.content(
                            rx.code_block(
                                SDK_WALLET_EXAMPLE,
                                language="python",
                                show_line_numbers=True,
                                wrap_long_lines=False,
                                custom_style={"overflowX": "auto"},
                                width="100%",
                            ),
                            value="wallet",
                            width="100%",
                        ),
                        rx.tabs.content(
                            rx.code_block(
                                SDK_BALANCE_EXAMPLE,
                                language="python",
                                show_line_numbers=True,
                                wrap_long_lines=False,
                                custom_style={"overflowX": "auto"},
                                width="100%",
                            ),
                            value="balance",
                            width="100%",
                        ),
                        rx.tabs.content(
                            rx.code_block(
                                SDK_SEND_EXAMPLE,
                                language="python",
                                show_line_numbers=True,
                                wrap_long_lines=False,
                                custom_style={"overflowX": "auto"},
                                width="100%",
                            ),
                            value="send",
                            width="100%",
                        ),
                        rx.tabs.content(
                            rx.code_block(
                                SDK_CONTRACT_EXAMPLE,
                                language="python",
                                show_line_numbers=True,
                                wrap_long_lines=False,
                                custom_style={"overflowX": "auto"},
                                width="100%",
                            ),
                            value="contract",
                            width="100%",
                        ),
                        default_value="wallet",
                        width="100%",
                        min_width="0",
                    ),
                    id="sdk-examples",
                ),
            )
        ),
        section(
            section_panel(
                rx.vstack(
                    rx.flex(
                        linked_heading("MCP Server", size="6", color=TEXT_PRIMARY, weight="bold"),
                        rx.hstack(
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="github", size=18),
                                    rx.text("Repo", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://github.com/xian-technology/xian-mcp-server",
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
                                href="https://modelcontextprotocol.io",
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
                        "A local Model Context Protocol (MCP) server that lets AI assistants create wallets, send transactions, "
                        "query smart contracts, and trade on the Xian DEX through standard MCP tools.",
                        size="4",
                        color=TEXT_MUTED,
                        line_height="1.7",
                        width="100%",
                    ),
                    spacing="3",
                    align_items="start",
                    width="100%",
                ),
                rx.box(
                    rx.text(
                        "Security note: the MCP server handles private keys and should only be run locally for development.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.6",
                    ),
                    padding="1rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="10px",
                    width="100%",
                ),
                rx.grid(
                    rx.box(
                        rx.vstack(
                            rx.text("Features", size="3", weight="bold", color=TEXT_PRIMARY),
                            rx.vstack(
                                _feature_item("Create or import standard and HD wallets."),
                                _feature_item("Check balances, send tokens, and simulate transactions."),
                                _feature_item("Query contract state, source, and token metadata."),
                                _feature_item("DEX helpers for buy/sell plus real-time pricing."),
                                _feature_item("Crypto utilities for signing and encryption."),
                                spacing="2",
                                align_items="start",
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                        padding="1.75rem",
                        background=SURFACE,
                        border=f"1px solid {BORDER_COLOR}",
                        border_radius="14px",
                        width="100%",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("Install & use", size="3", weight="bold", color=TEXT_PRIMARY),
                            rx.text(
                                "Clone the repo and build the Docker image locally:",
                                size="3",
                                color=TEXT_MUTED,
                                line_height="1.6",
                            ),
                            rx.code_block(
                                MCP_QUICKSTART,
                                language="bash",
                                show_line_numbers=False,
                                wrap_long_lines=False,
                                custom_style={"overflowX": "auto"},
                                width="100%",
                            ),
                            rx.text(
                                "Then register the server in your MCP config (Claude Desktop or LM Studio):",
                                size="3",
                                color=TEXT_MUTED,
                                line_height="1.6",
                            ),
                            rx.code_block(
                                MCP_CONFIG_SNIPPET,
                                language="json",
                                show_line_numbers=False,
                                wrap_long_lines=False,
                                custom_style={"overflowX": "auto"},
                                width="100%",
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                        padding="1.75rem",
                        background=SURFACE,
                        border=f"1px solid {BORDER_COLOR}",
                        border_radius="14px",
                        width="100%",
                    ),
                    columns={"base": "1", "lg": "2"},
                    spacing="4",
                    width="100%",
                    align="stretch",
                ),
            )
        ),
        section(
            section_panel(
                rx.vstack(
                    rx.flex(
                        linked_heading("AI Guides", size="6", color=TEXT_PRIMARY, weight="bold"),
                        rx.hstack(
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="github", size=18),
                                    rx.text("Repo", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://github.com/xian-technology/xian-ai-guides",
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
                                href="https://github.com/xian-technology/xian-ai-guides/blob/main/contracting-guide.txt",
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
                        "A collection of AI-ready guides that define the rules for writing and reviewing Xian smart contracts. "
                        "The contracting guide is the authoritative spec for Python contract structure, allowed features, and safety limits.",
                        size="4",
                        color=TEXT_MUTED,
                        line_height="1.7",
                        width="100%",
                    ),
                    spacing="3",
                    align_items="start",
                    width="100%",
                ),
                rx.grid(
                    rx.box(
                        rx.vstack(
                            rx.text("Guide highlights", size="3", weight="bold", color=TEXT_PRIMARY),
                            rx.vstack(
                                _feature_item("Python 3.11 only with strict builtins and no standard imports."),
                                _feature_item("Only @construct and @export; no return type annotations."),
                                _feature_item("Use Variable/Hash for state; no tuple unpacking or Hash membership checks."),
                                _feature_item("importlib for cross-contract calls; no nested imports."),
                                _feature_item("Events, limits, and stamp costs spelled out for safe design."),
                                spacing="2",
                                align_items="start",
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                        padding="1.75rem",
                        background=SURFACE,
                        border=f"1px solid {BORDER_COLOR}",
                        border_radius="14px",
                        width="100%",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("How to use", size="3", weight="bold", color=TEXT_PRIMARY),
                            rx.vstack(
                                _feature_item("Start from the contract template and keep state at top level."),
                                _feature_item("Annotate every @export parameter; avoid underscore names."),
                                _feature_item("Use ctx.caller/ctx.signer and injected globals (now, block_num)."),
                                _feature_item("Validate against the guide checklist before deployment."),
                                _feature_item("Use the contracting guide as a prompt or review checklist for AI workflows."),
                                spacing="2",
                                align_items="start",
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                        padding="1.75rem",
                        background=SURFACE,
                        border=f"1px solid {BORDER_COLOR}",
                        border_radius="14px",
                        width="100%",
                    ),
                    columns={"base": "1", "lg": "2"},
                    spacing="4",
                    width="100%",
                    align="stretch",
                ),
            )
        ),
    )


__all__ = ["tooling_page"]
