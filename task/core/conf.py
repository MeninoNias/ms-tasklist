from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = ""

    class Config:
        env_file = "../../.env"

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            user=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=str(self.POSTGRES_PORT),
            path=f"/{self.POSTGRES_DB}",
        )


settings = Settings()
