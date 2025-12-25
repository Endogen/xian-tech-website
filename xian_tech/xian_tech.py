import reflex as rx

from .pages.abci import abci_page
from .pages.community import community_page
from .pages.consensus import consensus_page
from .pages.contracts import contracts_page
from .pages.home import home_page
from .pages.bds import bds_page
from .pages.developers import developers_page
from .pages.about import about_page
from .pages.contact import contact_page
from .pages.team import team_page
from .pages.technology import technology_page
from .pages.tooling import tooling_page


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="icon", type="image/png", href="/favicon.png"),
        rx.el.link(rel="shortcut icon", type="image/png", href="/favicon.png"),
    ],
)

app.add_page(home_page, route="/", title="Xian Technology Foundation")
app.add_page(consensus_page, route="/consensus", title="CometBFT Consensus")
app.add_page(contracts_page, route="/contracts", title="Python Contracts")
app.add_page(abci_page, route="/abci", title="ABCI for CometBFT")
app.add_page(bds_page, route="/bds", title="Blockchain Data Service")
app.add_page(tooling_page, route="/tooling", title="Tooling & Integrations")
app.add_page(technology_page, route="/technology")
app.add_page(developers_page, route="/developers", title="Developer Hub")
app.add_page(about_page, route="/about", title="About the Foundation")
app.add_page(team_page, route="/team", title="Team")
app.add_page(community_page, route="/community")
app.add_page(contact_page, route="/contact", title="Contact")
