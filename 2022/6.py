
def run1(data: str, *args):
    length = 4
    last_chars = []
    for index, char in enumerate(data):
        last_chars.append(char)
        if len(last_chars) == len(set(last_chars)) == length:
            return index + 1

        if len(last_chars) >= length:
            last_chars.pop(0)


def run2(data: str, *args):
    length = 14
    last_chars = []
    for index, char in enumerate(data):
        last_chars.append(char)
        if len(last_chars) == len(set(last_chars)) == length:
            return index + 1

        if len(last_chars) >= length:
            last_chars.pop(0)
    return
