import logging
from .tools import fetch_country_data

logger = logging.getLogger(__name__)


def identify_intent(state):

    question = state["question"].lower()

    fields = []

    if "capital" in question:
        fields.append("capital")

    if "population" in question:
        fields.append("population")

    if "currency" in question:
        fields.append("currency")

    words = question.replace("?", "").split()

    stop_words = ["what", "is", "the", "of", "does", "use"]

    country = None

    for word in words:
        if word not in stop_words:
            country = word

    state["country"] = country
    state["fields"] = fields

    return state


def invoke_tool(state):

    country = state.get("country")

    if not country:
        state["country_data"] = None
        return state

    state["country_data"] = fetch_country_data(country)

    return state


def synthesize_answer(state):

    data = state.get("country_data")
    fields = state.get("fields", [])

    if not data:
        state["answer"] = "Sorry, I couldn't find information for that country."
        return state

    parts = []

    if "capital" in fields:
        capital = data.get("capital", ["Unknown"])[0]
        parts.append(f"capital is {capital}")

    if "population" in fields:
        population = data.get("population")
        parts.append(f"population is {population:,}")

    if "currency" in fields:
        currencies = data.get("currencies", {})
        if currencies:
            currency = list(currencies.values())[0]["name"]
            parts.append(f"currency is {currency}")

    country_name = data["name"]["common"]

    state["answer"] = f"For {country_name}, the " + " and the ".join(parts) + "."

    return state