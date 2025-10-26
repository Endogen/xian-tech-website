import reflex as rx


class State(rx.State):
    """Global application state."""

    theme_mode: str = "light"

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        self.theme_mode = "light" if self.theme_mode == "dark" else "dark"


__all__ = ["State"]
