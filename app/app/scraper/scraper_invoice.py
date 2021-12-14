import pandas as pd
from datetime import datetime


RESUME_INDEX = 4

DATE_INDEX = 2
ACESS_KEY_INDEX = 5
AUTH_PROTOCOLE_INDEX = 6
CONSUMER = 8

KEYS_INDEX = 0
CONTENT_INDEX = 0


def get_invoice_info(iframe_content, iframe_url) -> dict:
    details = get_details(iframe_content, iframe_url)
    resume = get_resume(iframe_content)

    return dict(**details, **resume)


def get_details(iframe_content, iframe_url) -> dict:
    content = iframe_content.findAll("td", "NFCCabecalho_SubTitulo")
    date = content[DATE_INDEX].text.split("\n")

    del date[KEYS_INDEX]

    def invoice_date_treatment(word: str) -> str:
        index = word.index(":")
        return word[slice(index + 1, len(word))].strip()

    date = map(invoice_date_treatment, date)
    date = list(date)

    nfce_number = date[0]
    series = date[1]
    date_time = str_to_datetime(date[2])

    acess_key = content[ACESS_KEY_INDEX].text
    acess_key = "".join(acess_key.split(" "))

    auth_protocole = content[AUTH_PROTOCOLE_INDEX].text.split(":")
    auth_protocole = auth_protocole[1].strip()

    # consumer = content[CONSUMER].text.strip()

    return {
        "url": iframe_url,
        "date_time": date_time,
        "acess_key": acess_key,
        "series": series,
        "auth_protocole": auth_protocole,
        "nfce_number": nfce_number,
        # "consumer": consumer,
    }


def get_resume(iframe_content) -> dict:
    content = iframe_content.findAll("table", "NFCCabecalho")[RESUME_INDEX]

    # Get first tables
    resume_df = pd.read_html(str(content))[CONTENT_INDEX]
    resume_dict = resume_df.to_dict("records")

    final_value = int(resume_dict[0][1])
    discount = int(resume_dict[1][1])

    return {"final_value": final_value, "discount": discount}


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
