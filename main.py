import datetime
import importlib
import json
import sys

import requests


DEBUG = False
USE_CURRENT = False
year = 2023
day = 8


session = requests.Session()


def current_date():
    now = datetime.datetime.now()
    global year, day
    year = now.year
    day = now.day


def import_from_id(module_id):
    package_name = f"{year}.{module_id}"
    try:
        module = importlib.import_module(package_name)
        return module
    except ImportError:
        raise ImportError(f"Could not import module: {module_id}")


def save_data_to_file(level_data):
    save_data = {"year": year, "day": day, "data": level_data}
    with open("data/cache.json") as file:
        json.dump(save_data, file, indent=4)


if __name__ == '__main__':
    if USE_CURRENT:
        current_date()
    runner = import_from_id(day)

    with open(f"./{year}/data/{day}.txt", "r") as f:
        data = f.read()

    # data_file = f"./{year}/data/{'cache' * DEBUG + 'test' * (not DEBUG)}.json"
    # with open(data_file) as f:
    #     json_data = json.load(f)
    #     data = json_data.get("data")

    # if json_data.get("year") == year and json_data.get("day") == day or DEBUG:
    #     data = json_data.get("data")
    # else:
    #     try:
    #         response = session.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": "a53616c7465645f5f62aa5406044b788416263673edf0194bc365f72e762fe2ca1f7e76ed85c00fa8daff9f9f64d225623dc1f17ecddefa8bdd97d2c958a5054f"})
    #         print(response.content)
    #         data = response.text
    #     except Exception as e:
    #         print(e)
    #         sys.exit(0)

    result1 = runner.run1(data=data)
    result2 = runner.run2(data=data)

    print(f"== {year} Tag {day} ==")
    print(f"Part 1: {result1}\nPart 2: {result2}")
