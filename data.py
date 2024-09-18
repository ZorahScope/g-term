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


def search_games(keyword: str, filter: dict = {}):
    """Queries KEYWORD from RAWG API"""
    ENDPOINT = "/games"
    new_params = {"search": f"{keyword}"}
    new_params.update(base_params)
    return rawg_session.get(RAWG_URL + ENDPOINT, params=new_params).json()


def list_platforms(
    parent: bool, page: int = 1, page_size: int = 10, ordering: str = ""
):
    """return list of parent or child platforms"""
    ENDPOINT = "/platforms/lists/parents" if parent else "/platforms"
    params = {ordering: ordering, page: page, page_size: page_size}
    params.update(base_params)
    return rawg_session.get(RAWG_URL + ENDPOINT, params=params).json()


def list_endpoint(endpoint, page: int = 1, page_size: int = 10, ordering: str = ""):
    """returns list from designated endpoint"""
    params = {ordering: ordering, page: page, page_size: page_size}
    params.update(base_params)
    return rawg_session.get(RAWG_URL + endpoint, params=params).json()


def get_details(id: int, endpoint: str):
    """return details on ID from ENDPOINT"""
    pass


def next_page(url: str):
    """requests next page of search/list results"""
    pass


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
