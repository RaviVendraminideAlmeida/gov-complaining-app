from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import MultiHostUrl
from pydantic import (
    HttpUrl,
    PostgresDsn,
    computed_field,
)


class Settings(BaseSettings):
    emails_enabled: bool = True
    PROJECT_NAME: str = "gov_complaining_app"
    SENTRY_DSN: HttpUrl | None = None

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5433
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postdba"
    POSTGRES_DB: str = "gov-complaining-db"

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()
