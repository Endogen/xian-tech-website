import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""


# Professional developer color palette
ACCENT = "#00ff88"
ACCENT_HOVER = "#00cc6a"
ACCENT_SOFT = "rgba(0, 255, 136, 0.08)"
ACCENT_GLOW = "rgba(0, 255, 136, 0.25)"
PRIMARY_BG = "#0a0e14"
SURFACE = "rgba(15, 20, 28, 0.6)"
SURFACE_HOVER = "rgba(20, 28, 38, 0.8)"
SURFACE_BRIGHT = "rgba(25, 35, 48, 0.9)"
CODE_BG = "#0d1117"
TEXT_PRIMARY = "#e6edf3"
TEXT_MUTED = "#8b949e"
TEXT_ACCENT = "#58a6ff"
BORDER_COLOR = "rgba(48, 54, 61, 0.6)"
BORDER_BRIGHT = "rgba(72, 80, 90, 0.8)"
MAX_CONTENT_WIDTH = "1200px"

NAV_LINKS = [
    {"label": "Home", "href": "/"},
    {"label": "Technology", "href": "/technology"},
    {"label": "Ecosystem", "href": "/ecosystem"},
    {"label": "Community", "href": "/community"},
]

TECHNOLOGY_TRACKS = [
    {
        "title": "Pure Python Contracts",
        "icon": "🐍",
        "description": (
            "Advance libraries that let developers express complex financial and governance "
            "logic in idiomatic Python, with deterministic execution and precise tooling."
        ),
        "points": [
            "Comprehensive standard library with battle-tested primitives",
            "Robust audit harnesses and differential testing utilities",
            "Accelerated developer onboarding with curated blueprints",
        ],
        "code_sample": "# Deploy a contract\n@export\ndef transfer(to: str, amount: int):\n    assert amount > 0\n    balances[to] += amount"
    },
    {
        "title": "High-Assurance Node",
        "icon": "⚡",
        "description": (
            "Refine the Xian node with next generation instrumentation, blazing sync times, "
            "and transparent performance dashboards for operators."
        ),
        "points": [
            "Deterministic Python runtime tuned for blockchain workloads",
            "Observability-first metrics, structured logs, and tracing adapters",
            "Optimized networking stack ready for institutional deployments",
        ],
        "code_sample": "# Node configuration\nxian_node = Node(\n    network='mainnet',\n    sync_mode='fast',\n    metrics=True\n)"
    },
    {
        "title": "Secure Upgrades",
        "icon": "🔒",
        "description": (
            "Provide governance tooling that keeps production contracts evolving without "
            "downtime, leveraging migration kits and formal verification hooks."
        ),
        "points": [
            "Versioned contract archetypes with automated changelog diffing",
            "On-chain governance frameworks aligned with community mandates",
            "Gradual rollout pipelines with rigorous rollback strategies",
        ],
        "code_sample": "# Upgrade contract\nupgrade_contract(\n    name='token',\n    version='2.0.0',\n    migration=migrate_v2\n)"
    },
]

ECOSYSTEM_INITIATIVES = [
    {
        "title": "Research Guild",
        "emoji": "🔬",
        "description": (
            "Collaborative working group dedicated to provable correctness, type-safe "
            "smart contract patterns, and cryptographic resilience."
        ),
        "links": ["Research papers", "Technical specifications", "Formal verification"],
    },
    {
        "title": "Builder Studio",
        "emoji": "🏗️",
        "description": (
            "Hands-on support for teams shipping production dApps on Xian Network, "
            "from architecture reviews to on-call debugging."
        ),
        "links": ["Architecture review", "Code audits", "Performance optimization"],
    },
    {
        "title": "Education Program",
        "emoji": "📚",
        "description": (
            "Curriculum, workshops, and tooling walkthroughs that help Python engineers "
            "become confident blockchain developers in weeks, not months."
        ),
        "links": ["Getting started guide", "Video tutorials", "Live workshops"],
    },
]

COMMUNITY_STREAMS = [
    {
        "title": "Contract Uplift Missions",
        "description": (
            "Audit, refactor, and extend flagship contracts already live on Xian Network "
            "to keep pace with new standards and evolving market requirements."
        ),
    },
    {
        "title": "Open Grants",
        "description": (
            "Targeted funding rounds for ecosystem teams building ADA-compliant wallets, "
            "analytics dashboards, or protocol integrations."
        ),
    },
    {
        "title": "Validator Collective",
        "description": (
            "Operator consortium focused on resilience, upgrade rehearsal, and coordinated "
            "responses across mainnet and testnet environments."
        ),
    },
]


def section(*children: rx.Component, **kwargs) -> rx.Component:
    """Wrap content in a centered section with generous spacing."""
    id_val = kwargs.pop("id", None)
    style = {
        "width": "100%",
        "maxWidth": MAX_CONTENT_WIDTH,
        "margin": "0 auto",
        "paddingLeft": "2rem",
        "paddingRight": "2rem",
        "paddingTop": "5rem",
        "paddingBottom": "5rem",
    }
    style.update(kwargs.pop("style", {}))
    return rx.box(*children, id=id_val, style=style, **kwargs)


def nav_link(link: dict[str, str]) -> rx.Component:
    """Navigation link with proper spacing."""
    return rx.link(
        rx.text(
            link["label"],
            size="3",
            weight="medium",
            color=TEXT_MUTED,
        ),
        href=link["href"],
        style={
            "padding": "0.75rem 1.25rem",
            "borderRadius": "8px",
            "transition": "all 0.2s ease",
        },
        _hover={
            "textDecoration": "none",
            "color": ACCENT,
            "backgroundColor": ACCENT_SOFT,
        },
    )


def nav_bar() -> rx.Component:
    """Professional navigation bar."""
    return rx.box(
        rx.box(
            rx.flex(
                rx.link(
                    rx.flex(
                        rx.box(
                            rx.text(
                                ">_",
                                size="5",
                                weight="bold",
                                color=ACCENT,
                            ),
                            padding="0.625rem 0.875rem",
                            background=CODE_BG,
                            border=f"2px solid {BORDER_BRIGHT}",
                            border_radius="8px",
                        ),
                        rx.vstack(
                            rx.text("Xian Technology", weight="bold", size="4", color=TEXT_PRIMARY),
                            rx.text("Python-native blockchain", size="2", color=TEXT_MUTED),
                            align_items="start",
                            spacing="0",
                        ),
                        gap="1rem",
                        align_items="center",
                    ),
                    href="/",
                    _hover={"textDecoration": "none"},
                ),
                rx.flex(
                    *[nav_link(link) for link in NAV_LINKS],
                    gap="0.5rem",
                    display={"base": "none", "md": "flex"},
                ),
                align_items="center",
                justify="between",
                width="100%",
            ),
            max_width=MAX_CONTENT_WIDTH,
            margin="0 auto",
            padding="0 2rem",
        ),
        position="sticky",
        top="0",
        z_index="100",
        background_color="rgba(10, 14, 20, 0.95)",
        backdrop_filter="blur(20px)",
        border_bottom=f"1px solid {BORDER_COLOR}",
        padding="1.25rem 0",
        width="100%",
    )


def code_block(code: str) -> rx.Component:
    """Professional code block."""
    return rx.box(
        rx.text(
            code,
            font_family="'SF Mono', 'Monaco', 'Menlo', 'Courier New', monospace",
            size="2",
            color="#c9d1d9",
            white_space="pre",
            line_height="1.6",
        ),
        background=CODE_BG,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="10px",
        padding="1.5rem",
        overflow_x="auto",
        width="100%",
    )


def feature_card(title: str, description: str, icon: str) -> rx.Component:
    """Feature card with proper spacing and hover effects."""
    return rx.box(
        rx.vstack(
            rx.text(icon, size="9", line_height="1"),
            rx.heading(title, size="5", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                description,
                size="3",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            spacing="5",
            align_items="start",
        ),
        padding="2.5rem",
        background=SURFACE,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="14px",
        transition="all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
        _hover={
            "borderColor": ACCENT,
            "backgroundColor": SURFACE_HOVER,
            "transform": "translateY(-8px)",
            "boxShadow": f"0 20px 40px {ACCENT_SOFT}",
        },
        height="100%",
    )


def terminal_prompt(command: str) -> rx.Component:
    """Terminal-style command prompt."""
    return rx.flex(
        rx.text("$", color=ACCENT, weight="bold", size="3"),
        rx.text(
            command,
            color=TEXT_PRIMARY,
            size="3",
            font_family="'SF Mono', 'Monaco', monospace"
        ),
        gap="1rem",
        padding="1rem 1.5rem",
        background=CODE_BG,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="8px",
        align_items="center",
        width="100%",
    )


def hero_section() -> rx.Component:
    """Professional hero section with generous spacing."""
    return section(
        rx.vstack(
            rx.box(
                rx.text(
                    "XIAN_TECHNOLOGY_FOUNDATION",
                    size="2",
                    letter_spacing="0.15em",
                    color=ACCENT,
                    weight="medium",
                ),
                padding="0.625rem 1.25rem",
                background=ACCENT_SOFT,
                border=f"1px solid {ACCENT_GLOW}",
                border_radius="8px",
            ),
            rx.heading(
                "Python-Native Blockchain Infrastructure",
                size="9",
                line_height="1.1",
                color=TEXT_PRIMARY,
                max_width="900px",
                text_align="center",
                weight="bold",
            ),
            rx.text(
                "Advancing the contracting library and node that power Xian Network. "
                "Production-ready, pure Python smart contracts with deterministic execution.",
                size="5",
                color=TEXT_MUTED,
                max_width="700px",
                text_align="center",
                line_height="1.7",
            ),
            rx.flex(
                rx.link(
                    rx.button(
                        rx.flex(
                            rx.text("Explore Technology", size="3", weight="medium"),
                            rx.text("→", weight="bold", size="4"),
                            gap="0.75rem",
                            align_items="center",
                        ),
                        size="4",
                        background_color=ACCENT,
                        color=PRIMARY_BG,
                        border_radius="10px",
                        cursor="pointer",
                        padding="1.25rem 2rem",
                        _hover={
                            "backgroundColor": ACCENT_HOVER,
                            "transform": "translateY(-2px)",
                        },
                        style={"transition": "all 0.2s ease"},
                    ),
                    href="/technology",
                ),
                rx.link(
                    rx.button(
                        "View on GitHub",
                        variant="outline",
                        size="4",
                        border_color=BORDER_BRIGHT,
                        color=TEXT_PRIMARY,
                        background_color="transparent",
                        border_radius="10px",
                        padding="1.25rem 2rem",
                        cursor="pointer",
                        _hover={
                            "backgroundColor": SURFACE,
                            "borderColor": TEXT_MUTED,
                        },
                        style={"transition": "all 0.2s ease"},
                    ),
                    href="https://github.com/xian-network",
                    is_external=True,
                ),
                gap="1.5rem",
                wrap="wrap",
                justify="center",
            ),
            spacing="8",
            align_items="center",
            width="100%",
        ),
        style={"paddingTop": "8rem", "paddingBottom": "8rem"},
    )


def stats_grid() -> rx.Component:
    """Statistics with improved spacing."""
    return section(
        rx.grid(
            rx.box(
                rx.vstack(
                    rx.text("100%", size="9", weight="bold", color=ACCENT, line_height="1"),
                    rx.text("Python", size="5", weight="bold", color=TEXT_PRIMARY),
                    rx.text(
                        "Pure Python contracts, tooling, and node",
                        size="3",
                        color=TEXT_MUTED,
                        text_align="center",
                        line_height="1.6",
                    ),
                    spacing="3",
                    align_items="center",
                ),
                padding="3rem 2rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
            ),
            rx.box(
                rx.vstack(
                    rx.text("Live", size="9", weight="bold", color=ACCENT, line_height="1"),
                    rx.text("Mainnet", size="5", weight="bold", color=TEXT_PRIMARY),
                    rx.text(
                        "Production deployments today on Xian Network",
                        size="3",
                        color=TEXT_MUTED,
                        text_align="center",
                        line_height="1.6",
                    ),
                    spacing="3",
                    align_items="center",
                ),
                padding="3rem 2rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
            ),
            rx.box(
                rx.vstack(
                    rx.text("Open", size="9", weight="bold", color=ACCENT, line_height="1"),
                    rx.text("Source", size="5", weight="bold", color=TEXT_PRIMARY),
                    rx.text(
                        "Community-driven development and governance",
                        size="3",
                        color=TEXT_MUTED,
                        text_align="center",
                        line_height="1.6",
                    ),
                    spacing="3",
                    align_items="center",
                ),
                padding="3rem 2rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
            ),
            template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
            gap="2rem",
        )
    )


def quick_features() -> rx.Component:
    """Features section with proper spacing."""
    return section(
        rx.vstack(
            rx.vstack(
                rx.heading("Why Xian Technology?", size="8", color=TEXT_PRIMARY, weight="bold"),
                rx.text(
                    "Pioneering the future of blockchain development with Python-first infrastructure",
                    size="4",
                    color=TEXT_MUTED,
                    max_width="720px",
                    text_align="center",
                    line_height="1.7",
                ),
                spacing="4",
                align_items="center",
            ),
            rx.grid(
                feature_card(
                    "Developer Experience",
                    "Write smart contracts in pure Python with full IDE support, type checking, and familiar tooling.",
                    "👨‍💻"
                ),
                feature_card(
                    "Deterministic Execution",
                    "Guaranteed consistent behavior across all nodes with a purpose-built Python runtime.",
                    "⚙️"
                ),
                feature_card(
                    "Production Ready",
                    "Battle-tested on Xian Network mainnet with real-world financial applications.",
                    "✅"
                ),
                template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                gap="2rem",
            ),
            spacing="9",
            align_items="center",
            width="100%",
        )
    )


def cta_section() -> rx.Component:
    """Call-to-action with proper spacing."""
    return section(
        rx.box(
            rx.vstack(
                rx.heading("Ready to Build?", size="8", color=TEXT_PRIMARY, weight="bold"),
                rx.text(
                    "Join the community of developers building the future of Python-native blockchain technology.",
                    size="4",
                    color=TEXT_MUTED,
                    text_align="center",
                    max_width="600px",
                    line_height="1.7",
                ),
                rx.flex(
                    rx.link(
                        rx.button(
                            "Explore Ecosystem",
                            size="4",
                            background_color=ACCENT,
                            color=PRIMARY_BG,
                            border_radius="10px",
                            padding="1.25rem 2rem",
                            cursor="pointer",
                            _hover={"backgroundColor": ACCENT_HOVER},
                        ),
                        href="/ecosystem",
                    ),
                    rx.link(
                        rx.button(
                            "Join Community",
                            size="4",
                            background_color="transparent",
                            color=TEXT_PRIMARY,
                            border_radius="10px",
                            padding="1.25rem 2rem",
                            border=f"1px solid {BORDER_BRIGHT}",
                            cursor="pointer",
                            _hover={"backgroundColor": SURFACE},
                        ),
                        href="/community",
                    ),
                    gap="1.5rem",
                    wrap="wrap",
                    justify="center",
                ),
                spacing="7",
                align_items="center",
            ),
            padding="5rem 3rem",
            background=SURFACE,
            border=f"1px solid {BORDER_COLOR}",
            border_radius="16px",
        )
    )


def footer() -> rx.Component:
    """Professional footer with proper spacing."""
    return rx.box(
        rx.box(
            rx.vstack(
                rx.flex(
                    rx.vstack(
                        rx.text("Xian Technology Foundation", size="4", weight="bold", color=TEXT_PRIMARY),
                        rx.text("Python-native blockchain infrastructure", size="3", color=TEXT_MUTED, line_height="1.6"),
                        spacing="2",
                        align_items="start",
                    ),
                    rx.vstack(
                        rx.text("Resources", size="3", weight="bold", color=TEXT_PRIMARY),
                        rx.vstack(
                            rx.link("Documentation", href="https://xian.org", is_external=True, color=TEXT_MUTED, size="3"),
                            rx.link("GitHub", href="https://github.com/xian-network", is_external=True, color=TEXT_MUTED, size="3"),
                            rx.link("Community", href="/community", color=TEXT_MUTED, size="3"),
                            spacing="3",
                            align_items="start",
                        ),
                        spacing="3",
                        align_items="start",
                    ),
                    rx.vstack(
                        rx.text("Contact", size="3", weight="bold", color=TEXT_PRIMARY),
                        rx.link("foundation@xian.technology", href="mailto:foundation@xian.technology", color=TEXT_MUTED, size="3"),
                        spacing="3",
                        align_items="start",
                    ),
                    justify="between",
                    width="100%",
                    direction={"base": "column", "md": "row"},
                    gap="4rem",
                    align_items={"base": "start", "md": "start"},
                ),
                rx.box(
                    rx.text(
                        "© 2024 Xian Technology Foundation. Built for the Xian Network community.",
                        size="2",
                        color=TEXT_MUTED,
                        text_align="center",
                    ),
                    padding_top="3rem",
                    border_top=f"1px solid {BORDER_COLOR}",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
            max_width=MAX_CONTENT_WIDTH,
            margin="0 auto",
            padding="4rem 2rem",
        ),
        background_color=CODE_BG,
        width="100%",
    )


def page_layout(*children: rx.Component) -> rx.Component:
    """Base layout wrapper for all pages."""
    return rx.box(
        nav_bar(),
        rx.box(
            *children,
            min_height="calc(100vh - 200px)",
        ),
        footer(),
        background=PRIMARY_BG,
        color=TEXT_PRIMARY,
        min_height="100vh",
    )


def index() -> rx.Component:
    """Home page."""
    return page_layout(
        hero_section(),
        stats_grid(),
        quick_features(),
        cta_section(),
    )


def technology_card_detailed(track: dict) -> rx.Component:
    """Detailed technology card with proper spacing."""
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.text(track["icon"], size="8", line_height="1"),
                rx.heading(track["title"], size="6", color=TEXT_PRIMARY, weight="bold"),
                gap="1.25rem",
                align_items="center",
            ),
            rx.text(
                track["description"],
                size="4",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            rx.vstack(
                *[
                    rx.flex(
                        rx.text("▹", color=ACCENT, weight="bold", size="4"),
                        rx.text(point, size="3", color=TEXT_MUTED, line_height="1.6"),
                        gap="1rem",
                        align_items="start",
                    )
                    for point in track["points"]
                ],
                spacing="4",
                align_items="start",
                width="100%",
            ),
            code_block(track["code_sample"]),
            spacing="6",
            align_items="start",
        ),
        padding="3rem",
        background=SURFACE,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="14px",
        transition="all 0.3s ease",
        _hover={
            "borderColor": BORDER_BRIGHT,
            "backgroundColor": SURFACE_HOVER,
        },
    )


def technology_page() -> rx.Component:
    """Technology page."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("TECHNOLOGY", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Building the Future of Python Blockchain",
                    size="9",
                    color=TEXT_PRIMARY,
                    line_height="1.2",
                    weight="bold",
                ),
                rx.text(
                    "Our teams extend the contracting library and node underpinning Xian Network, "
                    "keeping Python-native infrastructure performant, observable, and secure.",
                    size="4",
                    color=TEXT_MUTED,
                    max_width="800px",
                    line_height="1.7",
                ),
                spacing="6",
                align_items="start",
            ),
            style={"paddingBottom": "3rem"},
        ),
        section(
            rx.vstack(
                *[technology_card_detailed(track) for track in TECHNOLOGY_TRACKS],
                spacing="9",
            ),
            style={"paddingTop": "0"},
        ),
        section(
            rx.box(
                rx.vstack(
                    rx.heading("Get Started", size="7", color=TEXT_PRIMARY, weight="bold"),
                    rx.text(
                        "Deploy your first smart contract on Xian Network",
                        size="4",
                        color=TEXT_MUTED,
                        line_height="1.7",
                    ),
                    rx.vstack(
                        terminal_prompt("pip install xian-py"),
                        terminal_prompt("xian init my-contract"),
                        terminal_prompt("xian deploy"),
                        spacing="3",
                        width="100%",
                    ),
                    rx.link(
                        rx.button(
                            "View Documentation",
                            size="4",
                            background_color=ACCENT,
                            color=PRIMARY_BG,
                            border_radius="10px",
                            padding="1.25rem 2rem",
                            cursor="pointer",
                            _hover={"backgroundColor": ACCENT_HOVER},
                        ),
                        href="https://xian.org",
                        is_external=True,
                    ),
                    spacing="6",
                    align_items="start",
                    width="100%",
                ),
                padding="3.5rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
            )
        ),
    )


def ecosystem_card_detailed(item: dict) -> rx.Component:
    """Detailed ecosystem card."""
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.text(item["emoji"], size="8", line_height="1"),
                rx.heading(item["title"], size="6", color=TEXT_PRIMARY, weight="bold"),
                gap="1.25rem",
                align_items="center",
            ),
            rx.text(
                item["description"],
                size="3",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            rx.vstack(
                *[
                    rx.flex(
                        rx.text("→", color=ACCENT, size="4"),
                        rx.text(link, size="3", color=TEXT_ACCENT),
                        gap="1rem",
                        align_items="center",
                    )
                    for link in item["links"]
                ],
                spacing="3",
                align_items="start",
                width="100%",
            ),
            spacing="6",
            align_items="start",
        ),
        padding="3rem",
        background=SURFACE,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="14px",
        transition="all 0.3s ease",
        _hover={
            "borderColor": BORDER_BRIGHT,
            "transform": "translateY(-4px)",
        },
        height="100%",
    )


def ecosystem_page() -> rx.Component:
    """Ecosystem page."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("ECOSYSTEM", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Supporting the Python Blockchain Community",
                    size="9",
                    color=TEXT_PRIMARY,
                    line_height="1.2",
                    weight="bold",
                ),
                rx.text(
                    "We maintain an open collaboration model with researchers, builders, and operators. "
                    "Explore the pathways to shape the future of Python-powered decentralized systems.",
                    size="4",
                    color=TEXT_MUTED,
                    max_width="800px",
                    line_height="1.7",
                ),
                spacing="6",
                align_items="start",
            ),
            style={"paddingBottom": "3rem"},
        ),
        section(
            rx.grid(
                *[ecosystem_card_detailed(item) for item in ECOSYSTEM_INITIATIVES],
                template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                gap="2rem",
            ),
            style={"paddingTop": "0"},
        ),
        section(
            rx.box(
                rx.vstack(
                    rx.heading("Partner With Us", size="7", color=TEXT_PRIMARY, weight="bold"),
                    rx.text(
                        "Whether you're a researcher, builder, or educator, we'd love to collaborate.",
                        size="4",
                        color=TEXT_MUTED,
                        max_width="600px",
                        text_align="center",
                        line_height="1.7",
                    ),
                    rx.link(
                        rx.button(
                            "Request Partnership",
                            size="4",
                            background_color=ACCENT,
                            color=PRIMARY_BG,
                            border_radius="10px",
                            padding="1.25rem 2rem",
                            cursor="pointer",
                            _hover={"backgroundColor": ACCENT_HOVER},
                        ),
                        href="mailto:foundation@xian.technology",
                    ),
                    spacing="6",
                    align_items="center",
                ),
                padding="5rem 3rem",
                background=SURFACE,
                border=f"1px solid {BORDER_COLOR}",
                border_radius="14px",
                text_align="center",
            )
        ),
    )


def community_card_detailed(item: dict) -> rx.Component:
    """Community program card."""
    return rx.box(
        rx.vstack(
            rx.heading(item["title"], size="5", color=TEXT_PRIMARY, weight="bold"),
            rx.text(
                item["description"],
                size="3",
                color=TEXT_MUTED,
                line_height="1.7",
            ),
            spacing="4",
            align_items="start",
        ),
        padding="2.5rem",
        background=SURFACE,
        border=f"1px solid {BORDER_COLOR}",
        border_radius="14px",
        border_left=f"4px solid {ACCENT}",
        transition="all 0.3s ease",
        _hover={
            "borderColor": BORDER_BRIGHT,
            "backgroundColor": SURFACE_HOVER,
        },
    )


def community_page() -> rx.Component:
    """Community page."""
    return page_layout(
        section(
            rx.vstack(
                rx.box(
                    rx.text("COMMUNITY", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Join the Xian Network Community",
                    size="9",
                    color=TEXT_PRIMARY,
                    line_height="1.2",
                    weight="bold",
                ),
                rx.text(
                    "Enhance existing contracts, stress test network upgrades, and coordinate rollouts "
                    "with a foundation that values precision engineering over hype.",
                    size="4",
                    color=TEXT_MUTED,
                    max_width="800px",
                    line_height="1.7",
                ),
                spacing="6",
                align_items="start",
            ),
            style={"paddingBottom": "3rem"},
        ),
        section(
            rx.vstack(
                rx.heading("How to Contribute", size="7", color=TEXT_PRIMARY, weight="bold"),
                rx.grid(
                    *[community_card_detailed(item) for item in COMMUNITY_STREAMS],
                    template_columns={"base": "1fr", "md": "repeat(3, 1fr)"},
                    gap="2rem",
                ),
                spacing="6",
                align_items="start",
                width="100%",
            ),
            style={"paddingTop": "0"},
        ),
        section(
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.heading("Developer Resources", size="6", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Access documentation, tutorials, and tools to build on Xian Network.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        rx.vstack(
                            rx.link("📖 Documentation", href="https://xian.org", is_external=True, color=TEXT_ACCENT, size="3"),
                            rx.link("💻 GitHub Repository", href="https://github.com/xian-network", is_external=True, color=TEXT_ACCENT, size="3"),
                            rx.link("🎓 Tutorials & Guides", href="https://xian.org", is_external=True, color=TEXT_ACCENT, size="3"),
                            spacing="3",
                            align_items="start",
                        ),
                        spacing="5",
                        align_items="start",
                    ),
                    padding="3rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("Get in Touch", size="6", color=TEXT_PRIMARY, weight="bold"),
                        rx.text(
                            "Have questions or want to collaborate? Reach out to our team.",
                            size="3",
                            color=TEXT_MUTED,
                            line_height="1.7",
                        ),
                        rx.link(
                            rx.button(
                                "Contact Foundation",
                                size="4",
                                background_color=ACCENT,
                                color=PRIMARY_BG,
                                border_radius="10px",
                                padding="1.25rem 2rem",
                                width="100%",
                                cursor="pointer",
                                _hover={"backgroundColor": ACCENT_HOVER},
                            ),
                            href="mailto:foundation@xian.technology",
                        ),
                        spacing="5",
                        align_items="start",
                    ),
                    padding="3rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                ),
                template_columns={"base": "1fr", "md": "repeat(2, 1fr)"},
                gap="2rem",
            )
        ),
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(technology_page, route="/technology")
app.add_page(ecosystem_page, route="/ecosystem")
app.add_page(community_page, route="/community")
