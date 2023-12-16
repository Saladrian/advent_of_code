import math
import re


color_cubes_amount = {"red": 12, "green": 13, "blue": 14}


def is_valid_game(game):
    for color in color_cubes_amount.keys():
        color_pattern = re.compile(r"(\d+)\s" + color)
        color_matches = re.findall(color_pattern, game)
        for color_match in color_matches:
            if int(color_match) > color_cubes_amount.get(color):
                return False
    return True


def run1(data: str):
    game_pattern = re.compile(r"^Game\s(\d*):(.*?)$", re.MULTILINE)
    matches = re.findall(game_pattern, data)
    valid_game_ids = []
    for match in matches:
        if is_valid_game(match[1]):
            valid_game_ids.append(int(match[0]))
    return sum(valid_game_ids)


def game_min_values(game):
    color_cubes_min = {"red": 0, "green": 0, "blue": 0}
    for color in color_cubes_min.keys():
        color_pattern = re.compile(r"(\d+)\s" + color)
        color_matches = re.findall(color_pattern, game)
        for color_match in color_matches:
            if int(color_match) > color_cubes_min.get(color):
                color_cubes_min[color] = int(color_match)
    return color_cubes_min.values()


def run2(data: str):
    game_pattern = re.compile(r"^Game\s(\d*):(.*?)$", re.MULTILINE)
    matches = re.findall(game_pattern, data)
    sum_prod = 0
    for match in matches:
        min_values = game_min_values(match[1])
        sum_prod += math.prod(min_values)
    return sum_prod
