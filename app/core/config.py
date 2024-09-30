from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field, field_validator


# Load the appropriate .env file based on the environment
load_dotenv(".env")

class Settings(BaseSettings):
    # Database settings
    DB_HOST: str = Field("localhost", env="DB_HOST")
    DB_USERNAME: str = Field("postgres", env="DB_USERNAME")
    DB_PASSWORD: str = Field("postgres", env="DB_PASSWORD")
    DB_NAME: str = Field("investmind_db", env="DB_NAME")
    DATABASE_URL: Optional[str] = None
    ENVIRONMENT: str = Field("production", env="ENVIRONMENT")

    # Application settings

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = True


    @field_validator("DATABASE_URL", mode="before")
    def assemble_db_connection(cls, v: Optional[str], info) -> str:
        if isinstance(v, str):
            return v
        return f"postgresql://{info.data['DB_USERNAME']}:{info.data['DB_PASSWORD']}@{info.data['DB_HOST']}/{info.data['DB_NAME']}"

settings = Settings()