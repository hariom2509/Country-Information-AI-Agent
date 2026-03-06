import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

    REST_COUNTRIES_BASE_URL = "https://restcountries.com/v3.1/name/"

    REQUEST_TIMEOUT = 5

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")