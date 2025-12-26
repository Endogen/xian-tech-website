import reflex as rx

from ..components.common import page_layout, section
from ..state import State
from ..theme import (
    ACCENT,
    ACCENT_GLOW,
    ACCENT_HOVER,
    ACCENT_SOFT,
    BORDER_COLOR,
    PRIMARY_BG,
    SURFACE,
    SURFACE_BRIGHT,
    TEXT_MUTED,
    TEXT_PRIMARY,
)


def contact_page() -> rx.Component:
    """Contact page with message form."""

    def form_field(
        label: str,
        name: str,
        placeholder: str,
        *,
        field_type: str = "text",
        required: bool = False,
    ) -> rx.Component:
        return rx.vstack(
            rx.text(label, size="2", weight="medium", color=TEXT_MUTED),
            rx.input(
                name=name,
                id=name,
                placeholder=placeholder,
                type=field_type,
                required=required,
                width="100%",
                height="3.5rem",
                padding="0.9rem 1rem",
                border=f"1px solid {BORDER_COLOR}",
                border_radius="10px",
                background=SURFACE_BRIGHT,
                color=TEXT_PRIMARY,
                font_size="1rem",
                line_height="1.6",
                _focus={"borderColor": ACCENT, "outline": "none"},
            ),
            spacing="2",
            align_items="start",
            width="100%",
        )

    def message_field() -> rx.Component:
        return rx.vstack(
            rx.text("Message", size="2", weight="medium", color=TEXT_MUTED),
            rx.text_area(
                name="message",
                id="message",
                placeholder="Tell us what you are working on, and how we can help.",
                required=True,
                rows="6",
                resize="vertical",
                width="100%",
                min_height="220px",
                padding="0.9rem 1rem",
                border=f"1px solid {BORDER_COLOR}",
                border_radius="10px",
                background=SURFACE_BRIGHT,
                color=TEXT_PRIMARY,
                font_size="1rem",
                line_height="1.6",
                _focus={"borderColor": ACCENT, "outline": "none"},
            ),
            spacing="2",
            align_items="start",
            width="100%",
        )

    return page_layout(
        section(
            rx.vstack(
                rx.el.style(
                    rx.cond(
                        State.theme_mode == "light",
                        ".contact-form input::placeholder, .contact-form textarea::placeholder { color: #6b7280; opacity: 1; }",
                        ".contact-form input::placeholder, .contact-form textarea::placeholder { color: #9ca3af; opacity: 1; }",
                    )
                ),
                rx.box(
                    rx.text("CONTACT", size="2", letter_spacing="0.15em", color=ACCENT, weight="medium"),
                    padding="0.625rem 1.25rem",
                    background=ACCENT_SOFT,
                    border=f"1px solid {ACCENT_GLOW}",
                    border_radius="8px",
                ),
                rx.heading(
                    "Contact the Foundation",
                    size="8",
                    color=TEXT_PRIMARY,
                    weight="bold",
                    line_height="1.2",
                ),
                rx.text(
                    "Send us a note about partnerships, support, or questions about the Xian stack.",
                    size="4",
                    color=TEXT_MUTED,
                    line_height="1.7",
                    max_width="900px",
                ),
                rx.box(
                    rx.form(
                        rx.vstack(
                            rx.grid(
                                form_field("Full name", "name", "Jane Doe"),
                                form_field(
                                    "Email address",
                                    "email",
                                    "jane@company.com",
                                    field_type="email",
                                    required=True,
                                ),
                                columns={
                                    "base": "repeat(1, minmax(0, 1fr))",
                                    "md": "repeat(2, minmax(0, 1fr))",
                                },
                                spacing="4",
                                width="100%",
                            ),
                            rx.grid(
                                form_field("Organization", "organization", "Company or DAO"),
                                form_field("Topic", "topic", "Partnership, support, or other"),
                                columns={
                                    "base": "repeat(1, minmax(0, 1fr))",
                                    "md": "repeat(2, minmax(0, 1fr))",
                                },
                                spacing="4",
                                width="100%",
                            ),
                            message_field(),
                            rx.button(
                                "Send message",
                                type="submit",
                                size="4",
                                background_color=ACCENT,
                                color=PRIMARY_BG,
                                border_radius="10px",
                                padding="1.1rem 1.6rem",
                                width="100%",
                                cursor="pointer",
                                _hover={"backgroundColor": ACCENT_HOVER},
                            ),
                            spacing="4",
                            align_items="start",
                            width="100%",
                        ),
                        on_submit=State.submit_contact_form,
                        reset_on_submit=True,
                    ),
                    padding="3rem",
                    background=SURFACE,
                    border=f"1px solid {BORDER_COLOR}",
                    border_radius="14px",
                    class_name="contact-form",
                    width="100%",
                ),
                spacing="6",
                align_items="start",
                width="100%",
            )
        )
    )


__all__ = ["contact_page"]
