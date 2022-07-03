from typing import Any, Optional

from pydantic import BaseModel


class EventBrief(BaseModel):
    id: int
    title: str
    slug: str


class EventsBrief(BaseModel):
    next: Optional[str]
    previous: Optional[str]
    results: list[EventBrief]


class PlaceBrief(BaseModel):
    id: int


class FullEvent(BaseModel):
    id: int
    publication_date: int
    dates: list
    title: str
    slug: str
    place: Optional[PlaceBrief] = None
    description: str
    body_text: str
    location: dict
    categories: list[str]
    tagline: str
    age_restriction: Any
    price: str
    is_free: bool
    images: list[dict]
    favorites_count: int
    comments_count: int
    site_url: str
    short_title: str
    tags: list[str]
    disable_comments: bool
    participants: list


class FullPlace(BaseModel):
    id: int
    title: str
    slug: str
    address: str
    timetable: Optional[str]
    phone: Optional[str]
    is_stub: bool
    body_text: Optional[str]
    description: Optional[str]
    site_url: Optional[str]
    foreign_url: Optional[str]
    coords: dict
    subway: Optional[str]
    favorites_count: Optional[int]
    images: Optional[list[dict]]
    comments_count: Optional[int]
    is_closed: bool
    categories: Optional[list]
    short_title: Optional[str]
    tags: Optional[list[str]]
    location: str
    age_restriction: Optional[Any]
    disable_comments: Optional[bool]
    has_parking_lot: Optional[bool]


class FullEvents(BaseModel):
    events: list[FullEvent]
