NAV_LINKS = [
    {"label": "Home", "href": "/"},
    {"label": "Technology", "href": "/technology"},
    {"label": "Ecosystem", "href": "/ecosystem"},
    {"label": "Community", "href": "/community"},
]

COMMAND_ACTIONS = [
    {
        "label": link["label"],
        "href": link["href"],
        "description": f"Navigate to the {link['label']} page",
        "badge": "Page",
        "external": False,
    }
    for link in NAV_LINKS
]

COMMAND_ACTIONS += [
    {
        "label": "View Documentation",
        "href": "https://xian.org",
        "description": "Open the official Xian documentation",
        "badge": "Docs",
        "external": True,
    },
    {
        "label": "GitHub Organization",
        "href": "https://github.com/xian-network",
        "description": "Review repositories on GitHub",
        "badge": "Code",
        "external": True,
    },
    {
        "label": "Email the Foundation",
        "href": "mailto:foundation@xian.technology",
        "description": "Reach out to the Xian Technology Foundation",
        "badge": "Contact",
        "external": True,
    },
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
        "code_sample": (
            "# Deploy a contract\n"
            "@export\n"
            "def transfer(to: str, amount: int):\n"
            "    assert amount > 0\n"
            "    balances[to] += amount"
        ),
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
        "code_sample": (
            "# Node configuration\n"
            "xian_node = Node(\n"
            "    network='mainnet',\n"
            "    sync_mode='fast',\n"
            "    metrics=True\n"
            ")"
        ),
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
        "code_sample": (
            "# Upgrade contract\n"
            "upgrade_contract(\n"
            "    name='token',\n"
            "    version='2.0.0',\n"
            "    migration=migrate_v2\n"
            ")"
        ),
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

__all__ = [
    "COMMAND_ACTIONS",
    "NAV_LINKS",
    "TECHNOLOGY_TRACKS",
    "ECOSYSTEM_INITIATIVES",
    "COMMUNITY_STREAMS",
]
