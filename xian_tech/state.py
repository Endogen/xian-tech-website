from typing import Any, TypedDict

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

    theme_mode: str = "light"
    mobile_nav_open: bool = False
    command_palette_open: bool = False
    command_query: str = ""
    command_palette_active_id: str | None = None

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        self.theme_mode = "light" if self.theme_mode == "dark" else "dark"

    def toggle_mobile_nav(self):
        """Toggle the mobile navigation drawer."""
        self.mobile_nav_open = not self.mobile_nav_open

    def close_mobile_nav(self):
        """Close the mobile navigation."""
        self.mobile_nav_open = False

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
