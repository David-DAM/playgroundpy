from datetime import datetime, timedelta

import pytz


def iso_format(date_string: str) -> datetime:
    return datetime.fromisoformat(date_string)


def str_format(date_string: str, date_format: str) -> datetime:
    return datetime.strptime(date_string, date_format)


def apply_format(date_time: datetime, date_format: str) -> str:
    return date_time.strftime(date_format)


def add_days(date_time, days_to_add):
    return date_time + timedelta(days=days_to_add)


def difference_days(date_time_one, date_time_two):
    return date_time_two - date_time_one


def now_in_time_zone(time_zone):
    zone = pytz.timezone(time_zone)
    return datetime.now(zone)


if __name__ == "__main__":
    date = datetime(2025, 1, 5)
    print(f"The date created is {date}")

    iso_format = iso_format("2024-12-12")
    print(f"The date with iso format is {iso_format}")

    now = datetime.now()
    print(f"Today is {now}")

    string_format = str_format("12/12/2024", "%d/%m/%Y")
    formated = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"The date formated is {formated}")

    tomorrow = add_days(now, 1)
    print(f"Today + 5 days is {tomorrow}")

    difference = difference_days(now, tomorrow)
    print(f"Tomorrow minus today is {difference}")

    now_mexico = now_in_time_zone('America/Mexico_City')
    print(f"Today is {now_mexico} in Mexico")
