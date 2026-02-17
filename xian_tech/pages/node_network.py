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

QUICKSTART_COMMANDS = """git clone https://github.com/xian-technology/xian-node.git
cd xian-node
make setup"""

CONFIG_SETUP_COMMANDS = """./scripts/setup.sh
./scripts/copy_config.sh
docker compose up -d
docker compose logs -f"""

CORE_NODE_COMMANDS = """make core-build
make core-up
make init
make configure CONFIGURE_ARGS="--moniker node-001 --service-node xian-testnet-04 --copy-genesis true"
make core-shell
make up
pm2 logs --lines 1000
make core-down"""

CORE_BDS_COMMANDS = """make core-bds-build
make core-bds-up
make init
make configure CONFIGURE_ARGS="--moniker node-001 --service-node xian-testnet-04 --copy-genesis true"
make core-bds-shell
make up-bds
pm2 logs --lines 1000
make core-bds-down"""

CORE_DEV_COMMANDS = """make core-dev-build
make core-dev-up
make init
make configure CONFIGURE_ARGS="--moniker node-001 --service-node xian-testnet-04 --copy-genesis true"
make core-dev-shell
make up
pm2 logs --lines 1000
make core-dev-down"""

CONTRACTING_DEV_COMMANDS = """git clone https://github.com/xian-technology/contracting.git
make contracting-dev-build
make contracting-dev-up
pytest contracting/
exit"""

CORE_TEST_COMMANDS = """make core-dev-shell
pytest xian-core/tests/
exit"""

FIREWALL_COMMANDS = """sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 26656
sudo ufw allow 26657
sudo ufw enable
sudo ufw status"""

COMPOSE_COMBINE_COMMAND = """docker compose -f docker-compose.core.yaml -f docker-compose.xian-chain-dev.yml up -d"""

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
        "subtitle": "Clone, configure, and boot the xian-node stack.",
        "category": "Technology",
        "badge": "Section",
        "href": "/node-network",
        "keywords": ["Quickstart", "Docker", "Compose", "Setup"],
    },
    {
        "title": "Run a Core Node",
        "subtitle": "Makefile-driven flow for building and running core.",
        "category": "Technology",
        "badge": "Section",
        "href": "/node-network",
        "keywords": ["Core node", "Makefile", "pm2", "Logs"],
    },
    {
        "title": "Core + BDS",
        "subtitle": "Start the core node with the BDS services enabled.",
        "category": "Technology",
        "badge": "Section",
        "href": "/node-network",
        "keywords": ["BDS", "Core node", "Docker compose"],
    },
    {
        "title": "Dev Mode",
        "subtitle": "Resettable chain profile for local iteration.",
        "category": "Technology",
        "badge": "Section",
        "href": "/node-network",
        "keywords": ["Dev mode", "Local chain", "Reset"],
    },
    {
        "title": "Operations & Security",
        "subtitle": "Firewall, troubleshooting, and reference commands.",
        "category": "Technology",
        "badge": "Section",
        "href": "/node-network",
        "keywords": ["Firewall", "Troubleshooting", "Reference"],
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
            rx.text(text, size="3", color=TEXT_MUTED, line_height="1.7"),
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
            )
        ),
        section(
            section_panel(
                rx.flex(
                    linked_heading("xian-node", size="6", color=TEXT_PRIMARY, weight="bold"),
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
                        "Run a resettable chain for fast local iteration and testing.",
                        "make core-dev-build\nmake core-dev-up\nmake init",
                        "flask_conical",
                    ),
                    columns={"base": "1", "lg": "3"},
                    spacing="4",
                    width="100%",
                    align="stretch",
                ),
                subsection(
                    "Quickstart",
                    rx.text(
                        "Clone the repo, bootstrap the stack, then bring up the containers.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    rx.vstack(
                        bullet("Install Docker and Docker Compose."),
                        bullet("Copy `.env.example` to `.env` if you need to adjust credentials."),
                        bullet("Run the setup and config scripts before starting containers."),
                        spacing="2",
                        align_items="start",
                    ),
                    rx.text("Fast path:", size="3", color=TEXT_PRIMARY, weight="bold"),
                    command_block(QUICKSTART_COMMANDS),
                    rx.text("Manual setup steps:", size="3", color=TEXT_PRIMARY, weight="bold"),
                    command_block(CONFIG_SETUP_COMMANDS),
                ),
                subsection(
                    "Run a core node (Makefile)",
                    rx.text(
                        "Use the Makefile targets to build, configure, and operate the core node.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    command_block(CORE_NODE_COMMANDS),
                ),
                subsection(
                    "Run core + BDS",
                    rx.text(
                        "Enable the BDS stack by using the core + BDS targets.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    command_block(CORE_BDS_COMMANDS),
                ),
                subsection(
                    "Dev mode",
                    rx.text(
                        "The dev profile resets on reboot, making it ideal for local experimentation.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    command_block(CORE_DEV_COMMANDS),
                ),
                subsection(
                    "Contracting dev loop",
                    rx.text(
                        "Clone the contracting repo and run the dev containers to iterate on contracts locally.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    command_block(CONTRACTING_DEV_COMMANDS),
                ),
                subsection(
                    "Run core tests",
                    rx.text(
                        "Drop into the core dev shell and run the xian-core test suite.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    command_block(CORE_TEST_COMMANDS),
                ),
                subsection(
                    "Firewall (UFW)",
                    rx.text(
                        "Allow the standard ports for HTTP(S), P2P, and RPC access.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    command_block(FIREWALL_COMMANDS),
                ),
                subsection(
                    "Troubleshooting",
                    rx.vstack(
                        bullet("If containers are stuck, run `docker compose down` and restart the stack."),
                        bullet("Prune unused networks with `docker network prune` if stale networks linger."),
                        bullet("Use `docker ps` and `docker logs <container_name>` to inspect running services."),
                        bullet("Resolve port conflicts by stopping whatever else is bound to the required ports."),
                        spacing="2",
                        align_items="start",
                    ),
                ),
                subsection(
                    "Reference",
                    rx.text(
                        "Common Docker networks and compose combinations used by the stack.",
                        size="3",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    rx.vstack(
                        bullet("Docker networks: `xian-net`, `xian-db`."),
                        bullet("Compose files: `docker-compose.core.yaml`, `docker-compose.core.bds.yaml`, `docker-compose.core.dev.yaml`, `docker-compose.xian-chain-dev.yml`."),
                        bullet("Combine compose files with `-f` for custom stacks."),
                        spacing="2",
                        align_items="start",
                    ),
                    rx.text("Example compose override:", size="3", color=TEXT_PRIMARY, weight="bold"),
                    command_block(COMPOSE_COMBINE_COMMAND),
                ),
            ),
        )
        ,
        section(
            section_panel(
                rx.flex(
                    linked_heading("xian-node-skill", size="6", color=TEXT_PRIMARY, weight="bold"),
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
                        rx.link(
                            rx.hstack(
                                rx.icon(tag="book_open", size=18),
                                rx.text("DeepWiki", size="3"),
                                spacing="2",
                                align_items="center",
                            ),
                            href="https://deepwiki.com/xian-technology/xian-ai-skills/tree/main/xian-node-skill",
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
                    "Agents can now run and manage Xian nodes end-to-end. The xian-node-skill packages the exact "
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
            padding_top="0",
        ),
    )


__all__ = ["node_network_page"]
