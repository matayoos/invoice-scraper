from typing import List
from app.scraper import utils
from bs4 import BeautifulSoup
import requests


def get_content(url: str) -> str:
    iframe_url = get_iframe_url(url)
    iframe_response = requests.get(iframe_url)
    return BeautifulSoup(iframe_response.text, "html.parser")


def get_iframe_url(url: str) -> str:
    html_response = requests.get(url)
    soup = BeautifulSoup(html_response.text, "html.parser")
    return soup.find("iframe")["src"]


def format_items_values(items: list) -> list:
    for item in items:
        item["value"] = utils.str_to_money(item["value"])

        if item["unit"].lower() == "kg":
            item["qty"] = utils.str_to_kg(item["qty"])

    return items
