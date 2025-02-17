from .domain_exception import DomainException


class ShortenedUrlNotFound(DomainException):
    message = "We couldn't find that url"
    status_code = 404