import requests
from sample_jokes import *

from random import choice

def get_joke(category="stupid"):
    """Return a JSON representation of a joke based on a given category

    Args:
        category (str, optional): One of "stupid", "dumb", "fat". Defaults to "stupid".
    """

    joke_json = requests.get(f"https://v2.jokeapi.dev/joke/Any?contains={str(category)}")
    # joke_json = requests.get(f"https://dad-jokes.p.rapidapi.com/joke/search?term={str(category)}")

    def fetch_sample_joke(category=category):
        # Probably fetch one from our default seed values
        if category == "stupid":
            return {
                "joke": choice(STUPID_JOKES),
            }
        elif category == "dumb":
            return {
                "joke": choice(DUMB_JOKES),
            }
        elif category == "fat":
            return {
                "joke": choice(FAT_JOKES),
            }
        else:
            return None
    if joke_json.status_code == 200:

        if joke_json.json().get('error') == True:
            joke = fetch_sample_joke()
            return joke
        # Send a joke only if the request was successful.
        return joke_json.json()
    else:
        joke = fetch_sample_joke()
        if joke is not None:
            return joke
        return {
            "joke": "Sorry, we couldn't find a joke. Please try again"
        }
