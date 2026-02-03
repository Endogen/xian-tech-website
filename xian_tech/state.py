import asyncio
import os
from typing import Any, TypedDict
from urllib.parse import quote

import reflex as rx
from dotenv import load_dotenv

load_dotenv()


class CommandAction(TypedDict):
    id: str
    title: str
    subtitle: str
    category: str
    badge: str
    href: str
    external: bool
    keywords: list[str]


class CommandSection(TypedDict, total=False):
    type: str
    category: str
    id: str
    title: str
    subtitle: str
    badge: str
    href: str
    external: bool
    keywords: list[str]


class ActiveCommandInfo(TypedDict):
    id: str
    title: str
    subtitle: str
    category: str
    badge: str
    href: str
    external: bool
    keywords: list[str]
    placeholder: bool


class RoadmapCard(TypedDict):
    id: str
    number: int
    title: str
    status: str
    url: str
    tags: list[str]
    tags_text: str
    golden: bool


class RoadmapColumn(TypedDict):
    id: str
    name: str
    count: int
    cards: list[RoadmapCard]


class State(rx.State):
    """Global application state."""

    mobile_nav_open: bool = False
    nav_hover_label: str = ""
    command_palette_open: bool = False
    command_query: str = ""
    command_palette_active_id: str | None = None
    image_lightbox_open: bool = False
    image_lightbox_src: str = ""
    image_lightbox_alt: str = ""
    sdk_install_copied: bool = False
    roadmap_loading: bool = False
    roadmap_error: str = ""
    roadmap_columns: list[RoadmapColumn] = []
    roadmap_done_cards: list[RoadmapCard] = []
    roadmap_done_count: int = 0

    @rx.var
    def roadmap_show_loading(self) -> bool:
        """Show skeletons while the roadmap data is still empty."""
        return self.roadmap_loading or (not self.roadmap_columns and not self.roadmap_error)

    def toggle_mobile_nav(self):
        """Toggle the mobile navigation drawer."""
        self.mobile_nav_open = not self.mobile_nav_open

    def close_mobile_nav(self):
        """Close the mobile navigation."""
        self.mobile_nav_open = False

    def set_nav_hover(self, label: str):
        """Track which nav item is hovered."""
        self.nav_hover_label = label

    def clear_nav_hover(self):
        """Clear nav hover state."""
        self.nav_hover_label = ""

    def open_command_palette(self):
        """Show the command palette."""
        self.command_palette_open = True
        actions = self.command_palette_actions
        self.command_palette_active_id = actions[0]["id"] if actions else None

    def close_command_palette(self):
        """Hide the command palette and reset the query."""
        self.command_palette_open = False
        self.command_query = ""
        self.command_palette_active_id = None

    def set_command_query(self, value: str):
        """Update the palette query."""
        self.command_query = value
        actions = self.command_palette_actions
        self.command_palette_active_id = actions[0]["id"] if actions else None

    def set_command_palette_selection(self, value: str):
        """Highlight a palette item."""
        self.command_palette_active_id = value

    def command_palette_move_up(self):
        """Move selection to previous item in the palette."""
        actions = self.command_palette_actions
        if not actions:
            return
        ids = [a["id"] for a in actions]
        current = self.command_palette_active_id
        if current is None or current not in ids:
            self.command_palette_active_id = ids[-1]
        else:
            idx = ids.index(current)
            self.command_palette_active_id = ids[idx - 1] if idx > 0 else ids[-1]

    def command_palette_move_down(self):
        """Move selection to next item in the palette."""
        actions = self.command_palette_actions
        if not actions:
            return
        ids = [a["id"] for a in actions]
        current = self.command_palette_active_id
        if current is None or current not in ids:
            self.command_palette_active_id = ids[0]
        else:
            idx = ids.index(current)
            self.command_palette_active_id = ids[idx + 1] if idx < len(ids) - 1 else ids[0]

    def open_image_lightbox(self, src: str, alt: str = ""):
        """Show the image lightbox."""
        self.image_lightbox_open = True
        self.image_lightbox_src = src
        self.image_lightbox_alt = alt

    def close_image_lightbox(self):
        """Hide the image lightbox."""
        self.image_lightbox_open = False
        self.image_lightbox_src = ""
        self.image_lightbox_alt = ""

    async def copy_sdk_install_command(self):
        """Copy the SDK install command and flash copy feedback."""
        self.sdk_install_copied = True
        yield rx.set_clipboard("pip install xian-py")
        await asyncio.sleep(1.4)
        self.sdk_install_copied = False

    async def load_roadmap(self):
        """Load the Fizzy roadmap board into state."""
        if self.roadmap_columns or self.roadmap_loading:
            return

        column_name_overrides = {
            "specification": "Design",
            "working on": "Execute",
            "testing": "Validate",
        }

        self.roadmap_loading = True
        self.roadmap_error = ""
        yield

        def fetch_board() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
            from fizzy import FizzyClient

            token = os.getenv("FIZZY_TOKEN", "").strip()
            account_slug = os.getenv("FIZZY_ACCOUNT_SLUG", "1").strip().lstrip("/")
            board_id = os.getenv("FIZZY_BOARD_ID", "03fiomkit5oknquymk0ooi26m").strip()
            base_url = os.getenv("FIZZY_BASE_URL", "https://tasks.xian.technology").strip()

            if not token:
                raise ValueError("Missing FIZZY_TOKEN for Fizzy API access.")
            if not account_slug or not board_id:
                raise ValueError("Missing FIZZY_ACCOUNT_SLUG or FIZZY_BOARD_ID.")

            client = FizzyClient(
                token=token,
                account_slug=account_slug,
                base_url=base_url,
            )
            try:
                columns = client.columns.list(board_id)
                cards = client.cards.list(board_id=board_id)
                closed_cards = client.cards.list(board_id=board_id, status="closed")
            finally:
                client._http.close()

            board_id_value = str(board_id)

            def is_same_board(card: Any) -> bool:
                if getattr(card, "board_id", None) is not None:
                    return str(card.board_id) == board_id_value
                if getattr(card, "board", None) is not None and getattr(card.board, "id", None) is not None:
                    return str(card.board.id) == board_id_value
                return False

            cards = [card for card in cards if is_same_board(card)]
            closed_cards = [card for card in closed_cards if is_same_board(card)]

            def normalize_id(value: Any) -> str:
                return str(value).strip()

            columns_sorted = sorted(columns, key=lambda col: (col.position is None, col.position or 0))
            done_column_ids = {
                normalize_id(col.id)
                for col in columns_sorted
                if col.name.strip().lower() in {"done", "complete", "completed"}
            }
            cards_by_column: dict[str, list[dict[str, Any]]] = {
                normalize_id(col.id): [] for col in columns_sorted if normalize_id(col.id) not in done_column_ids
            }
            untriaged: list[dict[str, Any]] = []

            for card in cards:
                column_id = None
                if getattr(card, "column_id", None) is not None:
                    column_id = normalize_id(card.column_id)
                elif getattr(card, "column", None) is not None and getattr(card.column, "id", None) is not None:
                    column_id = normalize_id(card.column.id)

                card_payload = {
                    "id": card.id,
                    "number": card.number,
                    "title": card.title,
                    "status": card.status,
                    "url": card.url or "",
                    "tags": [tag.name for tag in card.tags],
                    "tags_text": ", ".join(tag.name for tag in card.tags),
                    "golden": bool(card.golden),
                }
                if column_id in done_column_ids:
                    continue
                if column_id and column_id in cards_by_column:
                    cards_by_column[column_id].append(card_payload)
                else:
                    untriaged.append(card_payload)

            for column_id, items in cards_by_column.items():
                items.sort(key=lambda item: item["number"])

            done_payload: list[dict[str, Any]] = []
            for card in closed_cards:
                done_payload.append(
                    {
                        "id": card.id,
                        "number": card.number,
                        "title": card.title,
                        "status": card.status,
                        "url": card.url or "",
                        "tags": [tag.name for tag in card.tags],
                        "tags_text": ", ".join(tag.name for tag in card.tags),
                        "golden": bool(card.golden),
                    }
                )
            done_payload.sort(key=lambda item: item["number"])

            columns_payload = []
            for col in columns_sorted:
                if col.id in done_column_ids:
                    continue
                normalized = col.name.strip().lower()
                columns_payload.append(
                    {
                        "id": col.id,
                        "name": column_name_overrides.get(normalized, col.name),
                    "cards": cards_by_column.get(normalize_id(col.id), []),
                    "count": len(cards_by_column.get(normalize_id(col.id), [])),
                }
                )

            if untriaged:
                untriaged_sorted = sorted(untriaged, key=lambda item: item["number"])
                columns_payload.insert(
                    0,
                    {
                        "id": "untriaged",
                        "name": "Investigate",
                        "cards": untriaged_sorted,
                        "count": len(untriaged_sorted),
                    },
                )

            return columns_payload, done_payload

        try:
            columns_payload, done_payload = await asyncio.to_thread(fetch_board)
            self.roadmap_columns = columns_payload
            self.roadmap_done_cards = done_payload
            self.roadmap_done_count = len(done_payload)
        except Exception as exc:  # pragma: no cover - surface user-friendly errors
            self.roadmap_error = str(exc)
        finally:
            self.roadmap_loading = False

    def submit_contact_form(self, form_data: dict[str, Any]):
        """Open a pre-filled email draft with the contact form details."""
        name = (form_data.get("name") or "").strip()
        email = (form_data.get("email") or "").strip()
        organization = (form_data.get("organization") or "").strip()
        topic = (form_data.get("topic") or "").strip()
        message = (form_data.get("message") or "").strip()

        subject_bits = [topic or "Foundation contact"]
        if name:
            subject_bits.append(name)
        elif email:
            subject_bits.append(email)
        subject = " - ".join(subject_bits)

        body_lines = []
        if name:
            body_lines.append(f"Name: {name}")
        if email:
            body_lines.append(f"Email: {email}")
        if organization:
            body_lines.append(f"Organization: {organization}")
        if topic:
            body_lines.append(f"Topic: {topic}")
        body_lines.append("")
        body_lines.append(message or "(No message provided)")

        body = "\n".join(body_lines)
        mailto = (
            "mailto:foundation@xian.technology"
            f"?subject={quote(subject)}"
            f"&body={quote(body)}"
        )
        return rx.redirect(mailto, is_external=True)

    def command_palette_select_active(self):
        """Navigate to the currently selected item."""
        active = self.command_palette_active_action
        if not active["placeholder"]:
            self.close_command_palette()
        return rx.redirect(active["href"])

    @rx.var(cache=True, auto_deps=False, deps=["command_query"])
    def command_palette_actions(self) -> list[CommandAction]:
        """Return filtered actions for the command palette."""
        from .search import SEARCH_ENTRIES

        query = self.command_query.strip().lower()
        if not query:
            return SEARCH_ENTRIES

        def matches(action: CommandAction) -> bool:
            haystack = " ".join(
                [
                    action.get("title", ""),
                    action.get("subtitle", ""),
                    " ".join(action.get("keywords", [])),
                    action.get("category", ""),
                ]
            ).lower()
            return query in haystack

        return [
            action
            for action in SEARCH_ENTRIES
            if matches(action)
        ]

    @rx.var
    def command_palette_empty(self) -> bool:
        """Determine if the palette has no search matches."""
        return len(self.command_palette_actions) == 0

    @rx.var
    def command_palette_sections(self) -> list[CommandSection]:
        """Flatten grouped actions into header + item sections."""
        sections: list[CommandSection] = []
        current_category = ""
        for action in self.command_palette_actions:
            category = action.get("category", "")
            if category != current_category:
                sections.append(
                    {
                        "type": "header",
                        "category": category,
                        "id": f"header-{category}",
                    }
                )
                current_category = category
            sections.append(
                {
                    "type": "item",
                    "category": category,
                    "id": action["id"],
                    "title": action["title"],
                    "subtitle": action["subtitle"],
                    "badge": action["badge"],
                    "href": action["href"],
                    "external": action["external"],
                    "keywords": action["keywords"],
                }
            )
        return sections

    @rx.var
    def command_palette_active_action(self) -> ActiveCommandInfo:
        """Return the currently highlighted action or a placeholder."""
        placeholder: ActiveCommandInfo = {
            "id": "palette-placeholder",
            "title": "Search the Xian Technology site",
            "subtitle": "Use keywords from any page — hero copy, stats, programs, or docs — to jump directly to the right section.",
            "category": "Hint",
            "badge": "Tip",
            "href": "#",
            "external": False,
            "keywords": [
                "Try 'deterministic python', 'research guild', or 'foundation contact'."
            ],
            "placeholder": True,
        }
        active_id = self.command_palette_active_id
        for action in self.command_palette_actions:
            if action["id"] == active_id:
                result: ActiveCommandInfo = {
                    **action,
                    "placeholder": False,
                }
                return result
        return placeholder

    @rx.var
    def has_command_palette_selection(self) -> bool:
        """Convenience flag for template logic."""
        return not self.command_palette_active_action["placeholder"]


__all__ = ["State"]
