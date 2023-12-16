import re


num_pattern = re.compile(r"(?=((^|\D)(\d+)(\D|$)))")
symbol_pattern = re.compile(r"[^\w.\n]")


def run1(data: str):
    lines = data.split("\n")
    part_number_sum = 0
    for i, line in enumerate(lines):
        num_matches = re.finditer(num_pattern, line)
        num_spans = [(m.group(3), m.span(1)) for m in num_matches]
        for numb, span in num_spans:
            for f in range(-1, 2):
                index = i + f
                if 0 <= index <= len(lines)-1:
                    is_match = re.search(symbol_pattern, lines[index][span[0]:span[1]])
                    if is_match:
                        part_number_sum += int(numb)
                        break
    return part_number_sum


def run2(data: str):
    lines = data.split("\n")
    gear_ratio_sum = 0
    for i, line in enumerate(lines):
        gears = [i for i, x in enumerate(line) if x == "*"]
        for i_gear in gears:
            part_numbs = []
            for f in range(-1, 2):
                index = i + f
                if 0 <= index <= len(lines) - 1:
                    num_matches = re.finditer(num_pattern, lines[index])
                    num_spans = [(m.group(3), m.span(1)) for m in num_matches]

                    for numb, span in num_spans:
                        if i_gear in range(span[0], span[1]):
                            part_numbs.append(int(numb))
            if len(part_numbs) == 2:
                gear_ratio_sum += (part_numbs[0] * part_numbs[1])
    return gear_ratio_sum
