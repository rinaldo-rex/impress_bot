import requests


def get_joke(category="stupid"):
    """Return a JSON representation of a joke based on a given category

    Args:
        category (str, optional): One of "stupid", "dumb", "fat". Defaults to "stupid".
    """

    joke_json = requests.get(f"https://v2.jokeapi.dev/joke/Any?contains={str(category)}")
    # joke_json = requests.get(f"https://dad-jokes.p.rapidapi.com/joke/search?term={str(category)}")

    if joke_json.status_code == 200:
        # Send a joke only if the request was successful.
        return joke_json.json()
    else:
        return {
            "joke": "Sorry, we couldn't find a joke. Please try again'"
        }
