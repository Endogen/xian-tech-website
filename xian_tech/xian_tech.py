import reflex as rx

from .pages.community import community_page
from .pages.ecosystem import ecosystem_page
from .pages.home import home_page
from .pages.technology import technology_page


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="icon", type="image/png", href="/favicon.png"),
        rx.el.link(rel="shortcut icon", type="image/png", href="/favicon.png"),
    ],
)

app.add_page(home_page, route="/", title="Xian Technology")
app.add_page(technology_page, route="/technology")
app.add_page(ecosystem_page, route="/ecosystem")
app.add_page(community_page, route="/community")
