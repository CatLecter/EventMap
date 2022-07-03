from http import HTTPStatus

import backoff
import requests  # type: ignore[import]
from pydantic import BaseModel
from requests import ConnectionError


@backoff.on_exception(backoff.expo, ConnectionError, max_tries=3)
def get_from_url(url: str, model: BaseModel) -> BaseModel:
    response = requests.get(url=url, timeout=5)
    if response.status_code == HTTPStatus.OK:
        return model(**response.json())  # noqa
