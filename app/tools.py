import requests
import logging
from .config import Config

logger = logging.getLogger(__name__)

def fetch_country_data(country: str):

    url = f"{Config.REST_COUNTRIES_BASE_URL}{country}"

    try:

        response = requests.get(url, timeout=Config.REQUEST_TIMEOUT)

        if response.status_code != 200:
            logger.warning(f"Country not found: {country}")
            return None

        data = response.json()

        if not data:
            return None

        return data[0]

    except requests.RequestException as e:

        logger.error(f"Country API failed: {e}")

        return None