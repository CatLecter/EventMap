import json

from config import cfg
from models import EventsBrief, FullEvent, FullPlace
from utils import get_from_url


def pars() -> None:
    events_brief: EventsBrief = get_from_url(cfg.brief_events_url, EventsBrief)  # noqa
    events = []
    for event_brief in events_brief.results:
        detail_event_url = cfg.detail_event_url + str(event_brief.id) + "/"
        full_event: FullEvent = get_from_url(detail_event_url, FullEvent)  # noqa
        event = full_event.dict()
        if full_event.place:
            detail_place_url = cfg.detail_place_url + str(full_event.place.id) + "/"
            place: FullPlace = get_from_url(detail_place_url, FullPlace)  # noqa
            event["place"] = place.dict()
        events.append(event)
    with open("./event_parser/events.json", "a", encoding="UTF-8") as f:
        json.dump(events, f, indent=4, separators=(",", ":"))


if __name__ == "__main__":
    try:
        pars()
    except KeyboardInterrupt:
        pass
