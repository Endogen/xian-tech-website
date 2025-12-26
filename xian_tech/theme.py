import reflex as rx

from .state import State

# Dark palette
DARK_ACCENT = "#00ff88"
DARK_ACCENT_HOVER = "#00cc6a"
DARK_ACCENT_SOFT = "rgba(0, 255, 136, 0.08)"
DARK_ACCENT_GLOW = "rgba(0, 255, 136, 0.25)"
DARK_PRIMARY_BG = "#0a0e14"
DARK_SURFACE = "rgba(15, 20, 28, 0.98)"
DARK_SURFACE_HOVER = "rgba(20, 28, 38, 0.8)"
DARK_SURFACE_BRIGHT = "rgba(25, 35, 48, 0.9)"
DARK_CODE_BG = "#0d1117"
DARK_TEXT_PRIMARY = "#e6edf3"
DARK_TEXT_MUTED = "#8b949e"
DARK_TEXT_ACCENT = "#58a6ff"
DARK_BORDER_COLOR = "rgba(48, 54, 61, 0.6)"
DARK_BORDER_BRIGHT = "rgba(72, 80, 90, 0.8)"
DARK_TOP_GRADIENT = "linear-gradient(180deg, rgba(0, 255, 136, 0.2), rgba(10, 14, 20, 0))"

# Light palette
LIGHT_ACCENT = "#50b165"
LIGHT_ACCENT_HOVER = "#408d50"
LIGHT_ACCENT_SOFT = "rgba(80, 177, 101, 0.08)"
LIGHT_ACCENT_GLOW = "rgba(80, 177, 101, 0.25)"
LIGHT_PRIMARY_BG = "#ffffff"
LIGHT_SURFACE = "rgba(248, 249, 250, 0.97)"
LIGHT_SURFACE_HOVER = "rgba(241, 243, 245, 0.9)"
LIGHT_SURFACE_BRIGHT = "rgba(255, 255, 255, 0.95)"
LIGHT_CODE_BG = "#f6f8fa"
LIGHT_TEXT_PRIMARY = "#1f2937"
LIGHT_TEXT_MUTED = "#6b7280"
LIGHT_TEXT_ACCENT = "#0066cc"
LIGHT_BORDER_COLOR = "rgba(209, 213, 219, 0.6)"
LIGHT_BORDER_BRIGHT = "rgba(156, 163, 175, 0.8)"
LIGHT_TOP_GRADIENT = "linear-gradient(180deg, rgba(80, 177, 101, 0.28), rgba(255, 255, 255, 0))"

MAX_CONTENT_WIDTH = "1200px"

# Theme-aware tokens
ACCENT = rx.cond(State.theme_mode == "light", LIGHT_ACCENT, DARK_ACCENT)
ACCENT_HOVER = rx.cond(State.theme_mode == "light", LIGHT_ACCENT_HOVER, DARK_ACCENT_HOVER)
ACCENT_SOFT = rx.cond(State.theme_mode == "light", LIGHT_ACCENT_SOFT, DARK_ACCENT_SOFT)
ACCENT_GLOW = rx.cond(State.theme_mode == "light", LIGHT_ACCENT_GLOW, DARK_ACCENT_GLOW)
PRIMARY_BG = rx.cond(State.theme_mode == "light", LIGHT_PRIMARY_BG, DARK_PRIMARY_BG)
SURFACE = rx.cond(State.theme_mode == "light", LIGHT_SURFACE, DARK_SURFACE)
SURFACE_HOVER = rx.cond(State.theme_mode == "light", LIGHT_SURFACE_HOVER, DARK_SURFACE_HOVER)
SURFACE_BRIGHT = rx.cond(State.theme_mode == "light", LIGHT_SURFACE_BRIGHT, DARK_SURFACE_BRIGHT)
CODE_BG = rx.cond(State.theme_mode == "light", LIGHT_CODE_BG, DARK_CODE_BG)
TEXT_PRIMARY = rx.cond(State.theme_mode == "light", LIGHT_TEXT_PRIMARY, DARK_TEXT_PRIMARY)
TEXT_MUTED = rx.cond(State.theme_mode == "light", LIGHT_TEXT_MUTED, DARK_TEXT_MUTED)
TEXT_ACCENT = rx.cond(State.theme_mode == "light", LIGHT_TEXT_ACCENT, DARK_TEXT_ACCENT)
BORDER_COLOR = rx.cond(State.theme_mode == "light", LIGHT_BORDER_COLOR, DARK_BORDER_COLOR)
BORDER_BRIGHT = rx.cond(State.theme_mode == "light", LIGHT_BORDER_BRIGHT, DARK_BORDER_BRIGHT)
TOP_GRADIENT = rx.cond(State.theme_mode == "light", LIGHT_TOP_GRADIENT, DARK_TOP_GRADIENT)

__all__ = [
    "ACCENT",
    "ACCENT_GLOW",
    "ACCENT_HOVER",
    "ACCENT_SOFT",
    "BORDER_BRIGHT",
    "BORDER_COLOR",
    "CODE_BG",
    "MAX_CONTENT_WIDTH",
    "PRIMARY_BG",
    "SURFACE",
    "SURFACE_BRIGHT",
    "SURFACE_HOVER",
    "TEXT_ACCENT",
    "TEXT_MUTED",
    "TEXT_PRIMARY",
    "TOP_GRADIENT",
]
