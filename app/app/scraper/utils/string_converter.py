from datetime import datetime

DATE_ID = 0
TIME_ID = 1
YEAR_ID = 2
MOUNTH_ID = 1
DAY_ID = 0
HOUR_ID = 0
MINUTE_ID = 1
SECOND_ID = 2
MONEY_FORMAT = 100
CONVERSOR_BASE = 10


def str_to_money(num: str) -> float:
    num = int(num)

    if num <= 0:
        return num
    else:
        return float(num) / MONEY_FORMAT


def str_to_datetime(date_time: str) -> datetime:
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


def str_to_kg(kg: str) -> float:
    length = len(kg)
    conversor = pow(CONVERSOR_BASE, length - 1)

    return float(kg) / conversor
