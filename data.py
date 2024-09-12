import os
from datetime import timedelta
from dotenv import load_dotenv
import requests_cache
import models

load_dotenv()
RAWG_KEY = os.getenv("RAWG_API_KEY")
RAWG_URL = "https://api.rawg.io/api"

rawg_session = requests_cache.CachedSession(
    "rawg_cache", expire_after=timedelta(days=7)
)
base_params = {
    "key": RAWG_KEY,
}


def query_rawg_api(keyword: str, endpoint: str = "/games"):
    """Queries KEYWORD from RAWG API"""
    new_params = {"search": f"{keyword}"}
    new_params.update(base_params)
    response = rawg_session.get(RAWG_URL + endpoint, params=new_params)
    return response


def clear_cache():
    """clear cached api responses"""
    rawg_session.cache.clear()


def is_cached(response) -> bool:
    """return BOOL on response being cached or not"""
    cache_obj = requests_cache.models.response.CachedResponse
    return isinstance(response, cache_obj)


def transform(game_search_results: dict) -> list[models.Game]:
    """convert raw json results to list of Game() objects"""
    transformed_results: list = []
    games: list = game_search_results.get("results")
    for game in games:
        transformed_results.append(models.Game.construct(**game))
    return transformed_results
