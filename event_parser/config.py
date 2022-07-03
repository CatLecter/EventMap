from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings

load_dotenv(find_dotenv())


class Config(BaseSettings):
    base_url: str
    brief_events_url: str
    detail_event_url: str
    detail_place_url: str
    db_uri: str


cfg = Config()
