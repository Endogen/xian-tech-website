import reflex as rx

config = rx.Config(
    app_name="xian_tech",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)