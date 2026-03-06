import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MODEL_NAME = os.getenv("MODEL_NAME", "llama3-8b-8192")

    REST_COUNTRIES_BASE_URL = "https://restcountries.com/v3.1/name/"

    REQUEST_TIMEOUT = 5

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")