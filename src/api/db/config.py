from typing import cast
from decouple import config
from sqlalchemy import URL

POSTGRES_HOST = cast(str, config("POSTGRES_HOST", default=None))
POSTGRES_PORT = cast(int, config("POSTGRES_PORT", default=None))
POSTGRES_USER = cast(str, config("POSTGRES_USER", default=None))
POSTGRES_PASSWORD = cast(str, config("POSTGRES_PASSWORD", default=None))
POSTGRES_DB = cast(str, config("POSTGRES_DB", default=None))

required_settings = {
    "POSTGRES_HOST": POSTGRES_HOST,
    "POSTGRES_PORT": POSTGRES_PORT,
    "POSTGRES_USER": POSTGRES_USER,
    "POSTGRES_PASSWORD": POSTGRES_PASSWORD,
    "POSTGRES_DB": POSTGRES_DB,
}

missing_settings = [
    name for name, value in required_settings.items() if not value
]

if missing_settings:
    raise RuntimeError(
        f"Missing required database settings: {', '.join(missing_settings)}"
    )

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    database=POSTGRES_DB,
)