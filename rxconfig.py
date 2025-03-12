import reflex as rx
from decouple import config

DATABASE_URL = config("DATABASE_URL", default="postgres:///localhost:5432/dbname")

config = rx.Config(
    app_name="reflex_gpt",
    db_url=DATABASE_URL,
)