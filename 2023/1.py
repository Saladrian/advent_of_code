import re


def run1(data: str):
    pattern = re.compile(r"^(?=\D*(\d)).*?(\d)\D*$", re.MULTILINE)
    matches = re.findall(pattern, data)
    numb = [int("".join(match)) for match in matches]
    return sum(numb)


def run1_oneline(data: str):
    return sum([int("".join(match)) for match in re.findall(re.compile(r"^(?=\D*(\d)).*?(\d)\D*$", re.MULTILINE), data)])


num_replace = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def run2(data: str):
    match = "|".join(num_replace.keys())
    pattern = re.compile(r"^(?=.*?(\d|" + match + r")).*(\d|" + match + r").*?$", re.MULTILINE)

    matches = re.findall(pattern, data)
    num_matches = []
    for match in matches:
        num_match = [num_replace.get(group, group) for group in match]
        num_matches.append(int("".join(num_match)))

    return sum(num_matches)
