import reflex as rx

from ..components.common import (
    hover_icon_chip,
    icon_watermark_hover_card,
    linked_heading,
    page_layout,
    section,
    section_panel,
    subsection,
    text_with_inline_code,
)
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_SOFT,
    TEXT_MUTED,
    TEXT_PRIMARY,
)

SETUP_FLOW_COMMANDS = """git clone https://github.com/xian-technology/xian-node.git
cd xian-node
make setup
make <profile>-build
make <profile>-up
make init"""

SEARCH_SECTIONS = [
    {
        "title": "Node & Network",
        "subtitle": "Node installation, configuration, and network bootstrapping guides.",
        "category": "Technology",
        "badge": "Page",
        "href": "/node-network",
        "keywords": ["Nodes", "Network", "Installation", "Configuration"],
    },
    {
        "title": "Quickstart",
        "subtitle": "Minimal bootstrap flow to get a node profile running.",
        "category": "Technology",
        "badge": "Section",
        "href": "/node-network",
        "keywords": ["Quickstart", "Docker", "Compose", "Setup"],
    },
    {
        "title": "Node Profiles",
        "subtitle": "Core node, Core + BDS, and Core dev mode at a glance.",
        "category": "Technology",
        "badge": "Section",
        "href": "/node-network",
        "keywords": ["Core node", "BDS", "Dev mode", "Makefile"],
    },
    {
        "title": "Operations Checklist",
        "subtitle": "Key health, logging, and networking checks after startup.",
        "category": "Technology",
        "badge": "Section",
        "href": "/node-network",
        "keywords": ["Logs", "Troubleshooting", "Ports", "Operations"],
    },
]


def node_network_page() -> rx.Component:
    """Node & network page."""
    def command_block(code: str) -> rx.Component:
        return rx.code_block(
            code,
            language="bash",
            show_line_numbers=False,
            wrap_long_lines=False,
            custom_style={"overflowX": "auto"},
            width="100%",
        )

    def bullet(text: str) -> rx.Component:
        return rx.hstack(
            rx.icon(tag="check", size=18, color=ACCENT),
            text_with_inline_code(text, size="3", color=TEXT_MUTED, line_height="1.7"),
            spacing="3",
            align_items="start",
        )

    def stack_card(title: str, body: str, command: str, icon: str) -> rx.Component:
        return icon_watermark_hover_card(
            rx.flex(
                hover_icon_chip(icon, size=22),
                rx.heading(title, size="5", color=TEXT_PRIMARY, weight="bold"),
                direction={"base": "row", "lg": "column"},
                align={"base": "center", "lg": "start"},
                spacing="3",
            ),
            rx.text(body, size="3", color=TEXT_MUTED, line_height="1.7"),
            command_block(command),
            icon=icon,
            padding="2rem",
            content_spacing="4",
        )

    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("NODE & NETWORK", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Node & Network",
                    size="8",
                    color=TEXT_PRIMARY,
                    weight="bold",
                    line_height="1.2",
                ),
                rx.text(
                    "Operational guidance for running Xian nodes: build the stack, configure the network, and keep "
                    "the chain healthy with repeatable Docker + Makefile flows.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    max_width="900px",
                ),
                spacing="6",
                align_items="start",
            ),
        ),
        section(
            section_panel(
                rx.flex(
                    linked_heading("Node Setup", size="6", color=TEXT_PRIMARY, weight="bold"),
                    rx.hstack(
                        rx.link(
                            rx.hstack(
                                rx.icon(tag="github", size=18),
                                rx.text("Repo", size="3"),
                                spacing="2",
                                align_items="center",
                            ),
                            href="https://github.com/xian-technology/xian-node",
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
                            href="https://deepwiki.com/xian-technology/xian-node",
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
                            href="https://docs.xian.technology/",
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
                    "The xian-node repository ships a Docker Compose stack and Makefile shortcuts for running Xian core, "
                    "optional BDS services, and a resettable dev network. Use the quickstart to bootstrap the stack, then "
                    "choose the profile that matches how you want to run the chain.",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    width="100%",
                ),
                rx.grid(
                    stack_card(
                        "Core node",
                        "Build and boot a production-style core node with the core compose profile.",
                        "make core-build\nmake core-up\nmake init",
                        "server",
                    ),
                    stack_card(
                        "Core + BDS",
                        "Run core alongside the BDS services defined in docker-compose.core.bds.yaml.",
                        "make core-bds-build\nmake core-bds-up\nmake init",
                        "database",
                    ),
                    stack_card(
                        "Core dev mode",
                        "Run a resettable chain for fast local iteration, repeatable testing, and safe config experimentation.",
                        "make core-dev-build\nmake core-dev-up\nmake init",
                        "flask_conical",
                    ),
                    columns={"base": "1", "lg": "3"},
                    spacing="4",
                    width="100%",
                    align="stretch",
                ),
                subsection(
                    "Setup Flow",
                    rx.text(
                        "Use this high-level flow to bootstrap the repository and start one profile. "
                        "Pick the profile command from the cards above based on your target environment.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    rx.vstack(
                        bullet("Install Docker and Docker Compose."),
                        bullet("Clone `xian-node`, then run `make setup` once."),
                        bullet("Start one profile (`core`, `core-bds`, or `core-dev`) and initialize it."),
                        spacing="2",
                        align_items="start",
                    ),
                    rx.text("Command template:", size="3", color=TEXT_PRIMARY, weight="bold"),
                    command_block(SETUP_FLOW_COMMANDS),
                ),
                subsection(
                    "Operations Checklist",
                    rx.text(
                        "After startup, focus on observability and basic networking hygiene. "
                        "Use the full repo docs for advanced tuning and environment-specific hardening.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    rx.vstack(
                        bullet("Confirm containers are healthy with `docker ps` and container logs."),
                        bullet("Track chain process output using `pm2 logs --lines 1000`."),
                        bullet("Keep required RPC and P2P ports open (`26656`, `26657`)."),
                        bullet("If startup fails, restart the profile and clear stale Docker resources."),
                        spacing="2",
                        align_items="start",
                    ),
                ),
            ),
        )
        ,
        section(
            section_panel(
                rx.flex(
                    linked_heading("Agent Node Skill", size="6", color=TEXT_PRIMARY, weight="bold"),
                    rx.hstack(
                        rx.link(
                            rx.hstack(
                                rx.icon(tag="github", size=18),
                                rx.text("Repo", size="3"),
                                spacing="2",
                                align_items="center",
                            ),
                            href="https://github.com/xian-technology/xian-ai-skills/tree/main/xian-node-skill",
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
                    "Agents can now run and manage Xian nodes end-to-end. The Agent Node Skill packages the exact "
                    "steps for provisioning, configuration, and operations so assistants can safely help bootstrap "
                    "mainnet/testnet nodes and keep them healthy.",
                    size="3",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    width="100%",
                ),
                rx.box(
                    rx.text(
                        "Use it to standardize node workflows for AI assistants or internal automation.",
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
            ),
        ),
    )


__all__ = ["node_network_page"]
