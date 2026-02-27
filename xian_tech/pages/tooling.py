import reflex as rx

from ..components.common import (
    hover_icon_chip,
    icon_watermark_hover_card,
    linked_heading,
    page_layout,
    section,
    section_panel,
    subsection,
)
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
        "title": "AI Skills",
        "subtitle": "Agent-ready skills for Xian SDK usage and node operations.",
        "category": "Technology",
        "badge": "Section",
        "href": "/tooling",
        "keywords": ["AI skills", "Agents", "xian-py", "Nodes"],
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
    return icon_watermark_hover_card(
        rx.hstack(
            hover_icon_chip("download"),
            rx.text("Install", size="3", weight="bold", color=TEXT_PRIMARY),
            spacing="3",
            align_items="center",
        ),
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
        icon="download",
        padding="1.75rem",
    )


def _feature_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon(tag="check", size=16, color=ACCENT),
        rx.text(text, size="3", color=TEXT_MUTED),
        spacing="2",
        align_items="center",
    )


def _photoswipe_lightbox_shell() -> rx.Component:
    """PhotoSwipe container used by the tooling page screenshot lightbox."""
    return rx.fragment(
        rx.el.div(
            rx.el.div(class_name="pswp__bg"),
            rx.el.div(
                rx.el.div(
                    rx.el.div(class_name="pswp__item"),
                    rx.el.div(class_name="pswp__item"),
                    rx.el.div(class_name="pswp__item"),
                    class_name="pswp__container",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(class_name="pswp__counter"),
                        rx.el.button(class_name="pswp__button pswp__button--close", title="Close (Esc)"),
                        rx.el.button(class_name="pswp__button pswp__button--share", title="Share"),
                        rx.el.button(class_name="pswp__button pswp__button--fs", title="Toggle fullscreen"),
                        rx.el.button(class_name="pswp__button pswp__button--zoom", title="Zoom in/out"),
                        rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    rx.el.div(class_name="pswp__preloader__donut"),
                                    class_name="pswp__preloader__cut",
                                ),
                                class_name="pswp__preloader__icn",
                            ),
                            class_name="pswp__preloader",
                        ),
                        class_name="pswp__top-bar",
                    ),
                    rx.el.div(
                        rx.el.div(class_name="pswp__share-tooltip"),
                        class_name="pswp__share-modal pswp__share-modal--hidden pswp__single-tap",
                    ),
                    rx.el.button(class_name="pswp__button pswp__button--arrow--left", title="Previous (arrow left)"),
                    rx.el.button(class_name="pswp__button pswp__button--arrow--right", title="Next (arrow right)"),
                    rx.el.div(
                        rx.el.div(class_name="pswp__caption__center"),
                        class_name="pswp__caption",
                    ),
                    class_name="pswp__ui pswp__ui--hidden",
                ),
                class_name="pswp__scroll-wrap",
            ),
            class_name="pswp",
            tabindex="-1",
            role="dialog",
            aria_hidden="true",
        ),
        rx.script(src="/js/photoswipe-init.js"),
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
                                    rx.text("DeepWiki", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://deepwiki.com/xian-technology/xian-py",
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
                        ". The full BDS GraphQL schema can be found ",
                        rx.link(
                            "here",
                            href="https://github.com/xian-technology/xian-ai-guides/blob/main/bds_graphql_schema.json",
                            is_external=True,
                            color=ACCENT,
                        ),
                        ".",
                        size="4",
                        color=TEXT_MUTED,
                        line_height="1.7",
                        width="100%",
                    ),
                    rx.text(
                        "GraphQL is a query language and API runtime that lets clients request exactly the fields they need in a single call. "
                        "For BDS, this improves performance and developer experience by reducing over-fetching, simplifying data access patterns, "
                        "and making it easier to build dashboards, explorers, and backend services on top of chain data.",
                        size="3",
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
                        icon_watermark_hover_card(
                            rx.flex(
                                hover_icon_chip(item["icon"]),
                                rx.heading(item["title"], size="5", weight="bold", color=TEXT_PRIMARY),
                                direction={"base": "row", "lg": "column"},
                                align={"base": "center", "lg": "start"},
                                spacing="3",
                            ),
                            rx.text(item["description"], size="3", color=TEXT_MUTED, line_height="1.7"),
                            icon=item["icon"],
                            padding="2rem",
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
                        "When GraphQL is enabled on a node, the GraphiQL UI is available at the node address under ",
                        rx.el.code(
                            "/graphiql",
                            style={
                                "fontFamily": "'SF Mono', 'Monaco', monospace",
                                "fontSize": "0.9em",
                                "background": CODE_BG,
                                "border": f"1px solid {BORDER_COLOR}",
                                "borderRadius": "6px",
                                "padding": "0.08rem 0.35rem",
                                "color": TEXT_PRIMARY,
                            },
                        ),
                        ". For API access, use ",
                        rx.el.code(
                            "/graphql",
                            style={
                                "fontFamily": "'SF Mono', 'Monaco', monospace",
                                "fontSize": "0.9em",
                                "background": CODE_BG,
                                "border": f"1px solid {BORDER_COLOR}",
                                "borderRadius": "6px",
                                "padding": "0.08rem 0.35rem",
                                "color": TEXT_PRIMARY,
                            },
                        ),
                        ".",
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
                        class_name="trend-image",
                        cursor="zoom-in",
                        border_radius="12px",
                        overflow="hidden",
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
                                    rx.text("DeepWiki", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://deepwiki.com/xian-technology/xian-py",
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
                    rx.text(
                        "An SDK gives you a higher-level, well-tested interface so you can build faster with less low-level node plumbing. "
                        "In practice, xian-py helps teams ship safer automation and integrations by standardizing signing, transaction flow, "
                        "and contract interaction patterns.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                        width="100%",
                    ),
                    spacing="3",
                    align_items="start",
                    width="100%",
                ),
                rx.grid(
                    icon_watermark_hover_card(
                        rx.hstack(
                            hover_icon_chip("list_checks"),
                            rx.text("Features", size="3", weight="bold", color=TEXT_PRIMARY),
                            spacing="3",
                            align_items="center",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="check", size=16, color=ACCENT),
                                rx.text(
                                    "Create wallets, manage keys, and sign transactions with predictable, reusable helpers.",
                                    size="3",
                                    color=TEXT_MUTED,
                                ),
                                spacing="2",
                                align_items="center",
                            ),
                            rx.hstack(
                                rx.icon(tag="check", size=16, color=ACCENT),
                                rx.text(
                                    "Deploy, call, and inspect Python smart contracts from scripts, services, and CI jobs.",
                                    size="3",
                                    color=TEXT_MUTED,
                                ),
                                spacing="2",
                                align_items="center",
                            ),
                            rx.hstack(
                                rx.icon(tag="check", size=16, color=ACCENT),
                                rx.text(
                                    "Build, simulate, and submit transactions with clearer feedback and predictable outcomes.",
                                    size="3",
                                    color=TEXT_MUTED,
                                ),
                                spacing="2",
                                align_items="center",
                            ),
                            rx.hstack(
                                rx.icon(tag="check", size=16, color=ACCENT),
                                rx.text(
                                    "Query node data, balances, and contract state for backend automation and app integrations.",
                                    size="3",
                                    color=TEXT_MUTED,
                                ),
                                spacing="2",
                                align_items="center",
                            ),
                            spacing="2",
                            align_items="start",
                        ),
                        icon="list_checks",
                        padding="1.75rem",
                    ),
                    _sdk_install_card(),
                    columns={"base": "1", "lg": "1"},
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
                                    rx.text("DeepWiki", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://deepwiki.com/xian-technology/xian-mcp-server",
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
                    rx.text(
                        "MCP is an open standard for connecting AI assistants to external tools through a consistent interface. "
                        "Using it here means you can expose Xian capabilities once and reuse them across different assistants, "
                        "reducing custom integration work while improving reliability and portability.",
                        size="3",
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
                    icon_watermark_hover_card(
                        rx.hstack(
                            hover_icon_chip("list_checks"),
                            rx.text("Features", size="3", weight="bold", color=TEXT_PRIMARY),
                            spacing="3",
                            align_items="center",
                        ),
                        rx.vstack(
                            _feature_item("Create or import standard and HD wallets, including BIP39 mnemonic-based flows."),
                            _feature_item("Check balances, send tokens, and simulate transactions before submitting on-chain."),
                            _feature_item("Query contract state, contract source, and token metadata for integrations and audits."),
                            _feature_item("Use DEX helpers for buy and sell workflows with real-time price lookups."),
                            _feature_item("Access crypto utilities for signing, verification, and encryption tasks."),
                            spacing="2",
                            align_items="start",
                        ),
                        icon="list_checks",
                        padding="1.75rem",
                    ),
                    icon_watermark_hover_card(
                        rx.hstack(
                            hover_icon_chip("terminal"),
                            rx.text("Install & use", size="3", weight="bold", color=TEXT_PRIMARY),
                            spacing="3",
                            align_items="center",
                        ),
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
                        icon="terminal",
                        padding="1.75rem",
                    ),
                    columns={"base": "1", "lg": "1"},
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
                    icon_watermark_hover_card(
                        rx.flex(
                            rx.hstack(
                                hover_icon_chip("book_open"),
                                rx.text("Guide highlights", size="3", weight="bold", color=TEXT_PRIMARY),
                                spacing="3",
                                align_items="center",
                            ),
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
                        rx.vstack(
                            _feature_item("Python 3.11 only with strict builtins and no standard imports."),
                            _feature_item("Only @construct and @export; no return type annotations."),
                            _feature_item("Use Variable/Hash for state; no tuple unpacking or Hash membership checks."),
                            _feature_item("importlib for cross-contract calls; no nested imports."),
                            _feature_item("Events, limits, and stamp costs spelled out for safe design."),
                            spacing="2",
                            align_items="start",
                        ),
                        icon="book_open",
                        padding="1.75rem",
                    ),
                    icon_watermark_hover_card(
                        rx.flex(
                            rx.hstack(
                                hover_icon_chip("list_checks"),
                                rx.text("How to use", size="3", weight="bold", color=TEXT_PRIMARY),
                                spacing="3",
                                align_items="center",
                            ),
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
                        rx.vstack(
                            _feature_item("Start from the contract template and keep state at top level."),
                            _feature_item("Annotate every @export parameter; avoid underscore names."),
                            _feature_item("Use ctx.caller/ctx.signer and injected globals (now, block_num)."),
                            _feature_item("Validate against the guide checklist before deployment."),
                            _feature_item("Use the contracting guide as a prompt or review checklist for AI workflows."),
                            spacing="2",
                            align_items="start",
                        ),
                        icon="list_checks",
                        padding="1.75rem",
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
                        linked_heading("AI Skills", size="6", color=TEXT_PRIMARY, weight="bold"),
                        rx.hstack(
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="github", size=18),
                                    rx.text("Repo", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://github.com/xian-technology/xian-ai-skills",
                                is_external=True,
                                color=TEXT_MUTED,
                                _hover={"color": ACCENT},
                            ),
                            rx.link(
                                rx.hstack(
                                    rx.icon(tag="book_open", size=18),
                                    rx.text("DeepWiki", size="3"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                href="https://deepwiki.com/xian-technology/xian-ai-skills",
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
                                href="https://github.com/xian-technology/xian-ai-skills",
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
                        "Agent-ready skill packs that teach AI assistants how to build on Xian, operate nodes, and "
                        "work with the core Python tooling.",
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
                    icon_watermark_hover_card(
                        rx.hstack(
                            hover_icon_chip("code", size=24),
                            rx.heading("xian-sdk-skill", size="5", weight="bold", color=TEXT_PRIMARY),
                            spacing="3",
                            align_items="center",
                        ),
                        rx.text(
                            "Guides agents through xian-py workflows: wallet creation (including HD/BIP39), "
                            "token transfers, contract deployment and calls, state queries, and transaction "
                            "simulation for reliable automation.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        icon="code",
                        padding="1.75rem",
                        height="100%",
                    ),
                    icon_watermark_hover_card(
                        rx.hstack(
                            hover_icon_chip("server", size=24),
                            rx.heading("xian-node-skill", size="5", weight="bold", color=TEXT_PRIMARY),
                            spacing="3",
                            align_items="center",
                        ),
                        rx.text(
                            "Covers node operations via xian-stack: joining mainnet/testnet, creating networks, "
                            "validator and service node setup, monitoring, CometBFT configuration, and Docker "
                            "deployment basics.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        icon="server",
                        padding="1.75rem",
                        height="100%",
                    ),
                    columns={"base": "1", "lg": "2"},
                    spacing="4",
                    width="100%",
                    align="stretch",
                ),
            )
        ),
        _photoswipe_lightbox_shell(),
    )


__all__ = ["tooling_page"]
