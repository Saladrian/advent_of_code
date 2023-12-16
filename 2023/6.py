import re


data_pattern = re.compile(r"Time:(.+)\nDistance:(.+)")
number_pattern = re.compile(r"(\d+)")


def run1(data: str):
    rows = re.findall(data_pattern, data)[0]
    value_rows = [re.findall(number_pattern, row) for row in rows]
    races = list(zip(*value_rows))

    print(races)
    result = 1
    for duration, distance_record in races:
        possible_wins = 0
        for press_length in range(int(duration)):
            mm_per_ms = press_length
            remaining_duration = int(duration) - press_length
            distance = mm_per_ms * remaining_duration

            if distance > int(distance_record):
                possible_wins += 1
        result *= possible_wins
    return result


def run2(data: str):
    rows = re.findall(data_pattern, data)[0]
    race = [row.replace(" ", "") for row in rows]
    
    possible_wins = 0
    duration, distance_record = race
    for press_length in range(int(duration)):
        mm_per_ms = press_length
        remaining_duration = int(duration) - press_length
        distance = mm_per_ms * remaining_duration

        if distance > int(distance_record):
            possible_wins += 1
    return possible_wins
