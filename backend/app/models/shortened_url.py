import pydantic


class ShortenedUrl(pydantic.BaseModel):
    uuid:  pydantic.UUID4
    original_url: pydantic.HttpUrl
    url_code: str
