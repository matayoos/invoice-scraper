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
