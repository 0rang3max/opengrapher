# encoding: utf-8
import requests
from bs4 import BeautifulSoup


TAGS = ["title", "type", "image", "url", "description"]


class NoHtmlProvided(Exception):
    def __init__(self, message="No HTML was provided for parsed url"):
        self.message = message


class BadResponse(Exception):
    def __init__(self, code):
        self.message = "Server responded with: {}".format(code)


def _parse_tag(soup, tag):
    elem = soup.find("meta", {"property": "og:{}".format(tag)})
    if not elem or not elem.get("content"):
        return None
    return elem["content"]


def parse(url):
    url_tag = "url"

    r = requests.get(url)
    if not r.ok:
        raise BadResponse(r.status_code)
    if not r.content:
        raise NoHtmlProvided

    soup = BeautifulSoup(r.content, features="html.parser")

    parse_tags = TAGS.copy()
    parse_tags.remove(url_tag)
    parsed_data = {url_tag: url}
    for tag in parse_tags:
        parsed_data[tag] = _parse_tag(soup, tag)
    return parsed_data
