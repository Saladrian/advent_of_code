
def run1(data: str, *args):
    pairs = data.split("\n")
    fully_contains = 0
    for pair in pairs:
        sections = [s.split("-") for s in pair.split(",")]
        a = int(sections[0][0]) <= int(sections[1][0])
        b = int(sections[0][1]) >= int(sections[1][1])
        c = int(sections[0][0]) >= int(sections[1][0])
        d = int(sections[0][1]) <= int(sections[1][1])
        fully_contains += a and b or c and d
    return fully_contains


def run2(data: str, *args):
    pairs = data.split("\n")
    fully_contains = 0
    for pair in pairs:
        sections = [s.split("-") for s in pair.split(",")]
        a = int(sections[1][0]) <= int(sections[0][1]) <= int(sections[1][1])
        b = int(sections[0][0]) <= int(sections[1][1]) <= int(sections[0][1])
        fully_contains += a or b
    return fully_contains
