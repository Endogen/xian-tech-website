from typing import Any

import reflex as rx

from .data import COMMAND_ACTIONS


class State(rx.State):
    """Global application state."""

    theme_mode: str = "light"
    command_palette_open: bool = False
    command_query: str = ""

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        self.theme_mode = "light" if self.theme_mode == "dark" else "dark"

    def open_command_palette(self):
        """Show the command palette."""
        self.command_palette_open = True

    def close_command_palette(self):
        """Hide the command palette and reset the query."""
        self.command_palette_open = False
        self.command_query = ""

    def set_command_query(self, value: str):
        """Update the palette query."""
        self.command_query = value

    @rx.var
    def command_palette_actions(self) -> list[dict[str, Any]]:
        """Return filtered actions for the command palette."""
        query = self.command_query.strip().lower()
        if not query:
            return COMMAND_ACTIONS
        return [
            action
            for action in COMMAND_ACTIONS
            if query in action["label"].lower() or query in action["description"].lower()
        ]

    @rx.var
    def command_palette_empty(self) -> bool:
        """Determine if the palette has no search matches."""
        return len(self.command_palette_actions) == 0


__all__ = ["State"]
