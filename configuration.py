from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")

    APPLICATION_HOST:str = "127.0.0.1"
    APPLICATION_PORT:int = 8000
    APPLICATION_RELOAD_FLAG:bool = True


settings = Settings()