from typing import List
from bs4 import BeautifulSoup
import requests
from datetime import datetime

DATE_ID = 0
TIME_ID = 1

YEAR_ID = 2
MOUNTH_ID = 1
DAY_ID = 0

HOUR_ID = 0
MINUTE_ID = 1
SECOND_ID = 2


def get_content(url: str) -> str:
    iframe_url = get_iframe_url(url)
    iframe_response = requests.get(iframe_url)
    return BeautifulSoup(iframe_response.text, "html.parser")


def get_iframe_url(url: str) -> str:
    html_response = requests.get(url)
    soup = BeautifulSoup(html_response.text, "html.parser")
    return soup.find("iframe")["src"]


def str_to_float(num: str) -> float:
    num = int(num)

    if num <= 0:
        return num
    else:
        return float(num / 100)


def str_to_datetime(date_time: str):
    # dd/mm/aaaa hh:mm:ss
    data = date_time.split(" ")
    date = data[DATE_ID].split("/")
    time = data[TIME_ID].split(":")

    year = int(date[YEAR_ID])
    mounth = int(date[MOUNTH_ID])
    day = int(date[DAY_ID])

    hour = int(time[HOUR_ID])
    minute = int(time[MINUTE_ID])
    second = int(time[SECOND_ID])

    return datetime(year, mounth, day, hour, minute, second)


def format_items_values(items: list) -> list:
    for item in items:
        item["value"] = str_to_float(item["value"])

        if item["unit"].lower() == "kg":
            length = len(item["qty"])
            divisor = pow(10, length - 1)

            item["qty"] = float(item["qty"]) / divisor

    return items
