import os
from dotenv import load_dotenv
from datetime import timedelta
import requests
import requests_cache

load_dotenv()
RAWG_KEY = os.getenv("RAWG_API_KEY")
RAWG_URL = "https://api.rawg.io/api"

rawg_session = requests_cache.CachedSession(
    "rawg_cache", expire_after=timedelta(days=7)
)
base_params = {
    "key": RAWG_KEY,
}


def search_rawg_api(search: str):
    new_params = {"search": f"{search}"}
    new_params.update(base_params)
    response = rawg_session.get(RAWG_URL + "/games", params=new_params)
    return response


def clear_cache():
    rawg_session.cache.clear()
