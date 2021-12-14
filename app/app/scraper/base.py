from bs4 import BeautifulSoup
import requests
from datetime import datetime


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
    date = data[0].split("/")
    time = data[1].split(":")

    year = int(date[2])
    mounth = int(date[1])
    day = int(date[0])

    hour = int(time[0])
    minute = int(time[1])
    second = int(time[2])

    return datetime(year, mounth, day, hour, minute, second)


def items_value_to_float(items: list) -> list:
    for item in items:
        item["value"] = str_to_float(item["value"])

    return items
