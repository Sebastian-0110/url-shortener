from . import url_shortener


@url_shortener.get("/heheh")
def hhehe():
    return "heheh", 200