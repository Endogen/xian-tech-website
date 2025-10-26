import reflex as rx

from .pages.community import community_page
from .pages.ecosystem import ecosystem_page
from .pages.home import home_page
from .pages.technology import technology_page


app = rx.App(theme=rx.theme(appearance="light"))

app.add_page(home_page, route="/")
app.add_page(technology_page, route="/technology")
app.add_page(ecosystem_page, route="/ecosystem")
app.add_page(community_page, route="/community")
