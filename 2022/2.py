
draw_value = {
    "A": 1, "B": 2, "C": 3,
    "X": 1, "Y": 2, "Z": 3
    }


def run1(data: str, *args):
    matches = data.split("\n")

    score = 0
    for match in matches:
        draws = match.split(" ")

        draw_opponent = draw_value.get(draws[0])
        draw_me = draw_value.get(draws[1])

        if draw_opponent % 3 == draw_me % 3:
            score += draw_me + 3
        elif draw_opponent % 3 == (draw_me - 1) % 3:
            score += draw_me + 6
        elif draw_opponent % 3 == (draw_me + 1) % 3:
            score += draw_me
        else:
            raise ValueError(f"Draw couldn't be calculated: {draws}")
    return score


wld = {"X": -1, "Y": 0, "Z": 1}


def run2(data: str, *args):
    matches = data.split("\n")

    score = 0
    for match in matches:
        draws = match.split(" ")

        draw_opponent = draw_value.get(draws[0])
        draw_me = draw_opponent + wld.get(draws[1])
        draw_score = 3 if draw_me % 3 == 0 else draw_me % 3

        if draw_opponent % 3 == draw_me % 3:
            score += draw_score + 3
            if draws[1] != "Y":
                raise ValueError(draws)
        elif draw_opponent % 3 == (draw_me - 1) % 3:
            score += draw_score + 6
            if draws[1] != "Z":
                raise ValueError(draws)
        elif draw_opponent % 3 == (draw_me + 1) % 3:
            score += draw_score
            if draws[1] != "X":
                raise ValueError(draws)
        else:
            raise ValueError(f"Draw couldn't be calculated: {draws}")
    return score
