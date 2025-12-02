def _slugify(value: str) -> str:
    return (
        value.lower()
        .replace(" ", "-")
        .replace("/", "-")
        .replace("_", "-")
        .replace("—", "-")
    )


NAV_LINKS = [
    {"label": "Home", "href": "/"},
    {"label": "Technology", "href": "/technology"},
    {"label": "Ecosystem", "href": "/ecosystem"},
    {"label": "Community", "href": "/community"},
]

STACK_COMPONENTS = [
    {
        "title": "CometBFT Consensus Engine",
        "description": "Byzantine fault-tolerant, deterministic state machine replication securing every block.",
        "href": "/consensus",
        "icon": "🛰️",
    },
    {
        "title": "Python Smart Contract Engine",
        "description": "Pure Python contracts with deterministic execution—no transpilers or alternate languages.",
        "href": "/contracts",
        "icon": "🐍",
    },
    {
        "title": "Python ABCI for CometBFT",
        "description": "ABCI application in Python bridging consensus with the contracting runtime and state patches.",
        "href": "/abci",
        "icon": "🔗",
    },
    {
        "title": "Tooling & Interfaces",
        "description": "xian-py SDK plus BDS GraphQL for querying chain data and building integrations.",
        "href": "/tooling",
        "icon": "🛠️",
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

def _build_search_entries() -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []

    nav_descriptions = {
        "/": "Landing page for the foundation, stats, and hero messaging.",
        "/technology": "Detailed breakdown of contracting, node, and roadmap work.",
        "/ecosystem": "Programs for researchers, builders, and educators.",
        "/community": "Calls to join missions, open grants, and validator collectives.",
    }

    for link in NAV_LINKS:
        entries.append(
            {
                "id": f"nav-{_slugify(link['label'])}",
                "title": f"{link['label']} page",
                "subtitle": nav_descriptions.get(link["href"], ""),
                "category": "Navigation",
                "badge": "Page",
                "href": link["href"],
                "external": False,
                "keywords": [link["label"], nav_descriptions.get(link["href"], "")],
            }
        )

    # Home: hero + stats + features + CTA
    home_sections = [
        {
            "title": "Python-Native Blockchain Infrastructure",
            "subtitle": "Advancing the contracting library and node that power Xian Network with deterministic execution.",
            "keywords": [
                "Hero",
                "Explore Technology",
                "Pure Python",
                "Deterministic contracts",
            ],
            "badge": "Hero",
        },
        {
            "title": "Pure Python contracts, tooling, and node",
            "subtitle": "Stats highlight describing the 100% Python-first stack.",
            "keywords": ["Stats", "Contracts", "Tooling"],
            "badge": "Stat",
        },
        {
            "title": "Live Mainnet deployments",
            "subtitle": "Xian Network showcases production deployments today.",
            "keywords": ["Stats", "Mainnet", "Production"],
            "badge": "Stat",
        },
        {
            "title": "Contributor-First pathways",
            "subtitle": "Opportunities for researchers, builders, and operators.",
            "keywords": ["Stats", "Community", "Operators"],
            "badge": "Stat",
        },
        {
            "title": "Deterministic Python",
            "subtitle": "Pure Python smart contracts with predictable execution and safety rails.",
            "keywords": ["Feature", "Contracts", "Deterministic"],
            "badge": "Feature",
        },
        {
            "title": "Production Network showcase",
            "subtitle": "Xian Network acts as a live showcase for tooling and governance.",
            "keywords": ["Feature", "Network", "Governance"],
            "badge": "Feature",
        },
        {
            "title": "Foundation Support",
            "subtitle": "Need architecture guidance or audits? Partner with our research and builder guilds.",
            "keywords": ["Request a Brief", "Support", "Guilds"],
            "badge": "CTA",
        },
    ]

    for section in home_sections:
        entries.append(
            {
                "id": f"home-{_slugify(section['title'])}",
                "title": section["title"],
                "subtitle": section["subtitle"],
                "category": "Home",
                "badge": section["badge"],
                "href": "/",
                "external": False,
                "keywords": section["keywords"],
            }
        )

    # Technology tracks
    for track in TECHNOLOGY_TRACKS:
        entries.append(
            {
                "id": f"technology-{_slugify(track['title'])}",
                "title": track["title"],
                "subtitle": track["description"],
                "category": "Technology",
                "badge": "Track",
                "href": "/technology",
                "external": False,
                "keywords": track["points"],
            }
        )

    entries.append(
        {
            "id": "technology-get-started",
            "title": "Deploy your first smart contract",
            "subtitle": "pip install xian-py → xian init → xian deploy",
            "category": "Technology",
            "badge": "Guide",
            "href": "/technology",
            "external": False,
            "keywords": ["Get started", "Terminal prompt", "Documentation"],
        }
    )

    # Ecosystem initiatives
    for item in ECOSYSTEM_INITIATIVES:
        entries.append(
            {
                "id": f"ecosystem-{_slugify(item['title'])}",
                "title": item["title"],
                "subtitle": item["description"],
                "category": "Ecosystem",
                "badge": "Program",
                "href": "/ecosystem",
                "external": False,
                "keywords": item["links"],
            }
        )

    entries.append(
        {
            "id": "ecosystem-partner",
            "title": "Partner With Us",
            "subtitle": "Collaboration pathways for researchers, builders, and educators.",
            "category": "Ecosystem",
            "badge": "CTA",
            "href": "/ecosystem",
            "external": False,
            "keywords": ["Request partnership", "Collaboration"],
        }
    )

    # Community streams
    for stream in COMMUNITY_STREAMS:
        entries.append(
            {
                "id": f"community-{_slugify(stream['title'])}",
                "title": stream["title"],
                "subtitle": stream["description"],
                "category": "Community",
                "badge": "Program",
                "href": "/community",
                "external": False,
                "keywords": [stream["title"]],
            }
        )

    entries += [
        {
            "id": "docs-xian",
            "title": "View Documentation",
            "subtitle": "Open the official Xian documentation site.",
            "category": "Resources",
            "badge": "Docs",
            "href": "https://xian.org",
            "external": True,
            "keywords": ["Documentation", "Guides", "Tutorials"],
        },
        {
            "id": "github-org",
            "title": "GitHub Organization",
            "subtitle": "Review repositories across the Xian Network ecosystem.",
            "category": "Resources",
            "badge": "Code",
            "href": "https://github.com/xian-network",
            "external": True,
            "keywords": ["GitHub", "Repositories", "Code"],
        },
        {
            "id": "contact-foundation",
            "title": "Email the Foundation",
            "subtitle": "foundation@xian.technology — reach the core team.",
            "category": "Resources",
            "badge": "Contact",
            "href": "mailto:foundation@xian.technology",
            "external": True,
            "keywords": ["Contact", "Foundation", "Email"],
        },
    ]

    # Stack components
    for component in STACK_COMPONENTS:
        entries.append(
            {
                "id": f"stack-{_slugify(component['title'])}",
                "title": component["title"],
                "subtitle": component["description"],
                "category": "Stack",
                "badge": "Component",
                "href": component["href"],
                "external": False,
                "keywords": [component["title"], component["description"]],
            }
        )

    return entries


SEARCH_ENTRIES = _build_search_entries()


__all__ = [
    "STACK_COMPONENTS",
    "COMMUNITY_STREAMS",
    "ECOSYSTEM_INITIATIVES",
    "NAV_LINKS",
    "SEARCH_ENTRIES",
    "TECHNOLOGY_TRACKS",
]
