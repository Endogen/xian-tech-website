from typing import Any, TypedDict
from urllib.parse import quote

import reflex as rx

from .data import SEARCH_ENTRIES


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

    @rx.var
    def command_palette_actions(self) -> list[CommandAction]:
        """Return filtered actions for the command palette."""
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
