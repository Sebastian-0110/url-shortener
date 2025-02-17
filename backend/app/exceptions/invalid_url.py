from .domain_exception import DomainException


class InvalidUrlException(DomainException):
    message = "The introduced url is not valid"
    status_code = 400