import pydantic


class ShortenedUrl(pydantic.BaseModel):
    uuid:  pydantic.UUID4
    url: pydantic.HttpUrl
    shortened_url_code: str
