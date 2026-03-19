from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Awesome FastAPI Project"
    VERSION: str = "0.1.0"
    # 以后可以从 .env 文件自动读取
    API_V1_STR: str = "/api/v1"

settings = Settings()