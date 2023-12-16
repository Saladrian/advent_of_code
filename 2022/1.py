
def run1(data: str, *args):
    elves = data.split("\n\n")

    elves_calories = []
    for elf in elves:
        food = elf.split("\n")
        food_int = [int(x) for x in food]
        calories = sum(food_int)
        elves_calories.append(calories)
    highest = sorted(elves_calories)[-1]

    return highest


def run2(data: str, *args):
    elves = data.split("\n\n")

    elves_calories = []
    for elf in elves:
        food = elf.split("\n")
        food_int = [int(x) for x in food]
        calories = sum(food_int)
        elves_calories.append(calories)
    highest_three = sorted(elves_calories)[-3:]

    return sum(highest_three)
