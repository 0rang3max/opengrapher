# encoding: utf-8
import requests
from bs4 import BeautifulSoup


PARSE_TAGS = ["url", "title", "type", "image", "description"]


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


def parse(url, parse_tags=PARSE_TAGS):
    r = requests.get(url)
    if not r.ok:
        raise BadResponse(r.status_code)
    if not r.content:
        raise NoHtmlProvided

    soup = BeautifulSoup(r.content, features="html.parser")
    parsed_data = {}
    for tag in parse_tags:
        tag_data = _parse_tag(soup, tag)
        if tag_data:
            parsed_data[tag] = _parse_tag(soup, tag)

    return parsed_data
