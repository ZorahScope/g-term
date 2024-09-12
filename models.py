from typing import List, Optional
from pydantic import BaseModel, HttpUrl, ValidationError


class PlatformDetails(BaseModel):
    id: Optional[int]
    name: Optional[str]
    slug: Optional[str]


class StoreDetails(BaseModel):
    id: Optional[int]
    name: Optional[str]
    slug: Optional[str]


class Platform(BaseModel):
    platform: PlatformDetails


class Store(BaseModel):
    store: StoreDetails


class Rating(BaseModel):
    id: Optional[int]
    title: Optional[str]
    count: Optional[int]
    percent: Optional[float]


class AddedByStatus(BaseModel):
    yet: Optional[int]
    owned: Optional[int]
    beaten: Optional[int]
    toplay: Optional[int]
    dropped: Optional[int]
    playing: Optional[int]


class Tag(BaseModel):
    id: Optional[int]
    name: Optional[str]
    slug: Optional[str]
    language: Optional[str]
    games_count: Optional[int]
    image_background: Optional[HttpUrl]


class Screenshot(BaseModel):
    id: Optional[int]
    image: Optional[HttpUrl]


class Genre(BaseModel):
    id: Optional[int]
    name: Optional[str]
    slug: Optional[str]


class ParentPlatform(BaseModel):
    platform: PlatformDetails


class Game(BaseModel):
    slug: Optional[str]
    name: Optional[str]
    playtime: Optional[int]
    platforms: Optional[List[Platform]]
    stores: Optional[List[Store]]
    released: Optional[str]
    tba: Optional[bool]
    background_image: Optional[HttpUrl]
    rating: Optional[float]
    rating_top: Optional[int]
    ratings: Optional[List[Rating]]
    ratings_count: Optional[int]
    reviews_text_count: Optional[int]
    added: Optional[int]
    added_by_status: Optional[AddedByStatus]
    metacritic: Optional[int]
    suggestions_count: Optional[int]
    updated: Optional[str]
    id: Optional[int]
    score: Optional[str]
    clip: Optional[str]
    tags: Optional[List[Tag]]
    esrb_rating: Optional[str]
    reviews_count: Optional[int]
    saturated_color: Optional[str]
    dominant_color: Optional[str]
    short_screenshots: Optional[List[Screenshot]]
    parent_platforms: Optional[List[ParentPlatform]]
    genres: Optional[List[Genre]]
