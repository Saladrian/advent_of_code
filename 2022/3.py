

def item_value(item):
    return ord(item) - item.islower() * 96 - item.isupper() * (64 - 26)


def get_double_part(compartments):
    for item in compartments[0]:
        if item in compartments[1]:
            return item


def run1(data: str, *args):
    backpacks = data.split("\n")
    parts_value = 0
    for backpack in backpacks:
        mid_i = len(backpack) // 2
        compartments = backpack[:mid_i], backpack[mid_i:]
        item = get_double_part(compartments)
        parts_value += item_value(item)
    return parts_value


def get_same_group_part(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return item


def run2(data: str, *args):
    backpacks = data.split("\n")
    groups = [backpacks[x:x+3] for x in range(0, len(backpacks), 3)]
    parts_value = 0
    for group in groups:
        item = get_same_group_part(group)
        parts_value += item_value(item)
    return parts_value
