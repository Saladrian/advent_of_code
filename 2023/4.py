import re

line_pattern = re.compile(r"^Card\s+(\d+):(.*)\|(.*)$", re.MULTILINE)


def run1(data: str):
    line_matches = re.findall(line_pattern, data)
    total_value = 0
    for match in line_matches:
        card_value = 0
        winning_numbers = [int(numb) for numb in match[1].split(" ") if numb]
        my_numbers = [int(numb) for numb in match[2].split(" ") if numb]
        for numb in my_numbers:
            if numb in winning_numbers:
                card_value = (not card_value) * 1 + card_value * 2
        total_value += card_value
    return total_value


def run2(data: str):
    line_matches = re.findall(line_pattern, data)
    card_instances = {}
    for match in line_matches:
        winning_numbers = [int(numb) for numb in match[1].split(" ") if numb]
        my_numbers = [int(numb) for numb in match[2].split(" ") if numb]

        card_id = int(match[0])
        card_instances[str(card_id)] = card_instances.get(str(card_id), 0) + 1
        matching_numbs = 0
        for numb in my_numbers:
            matching_numbs += (numb in winning_numbers)
        for j in range(1, matching_numbs+1):
            next_card_id = card_id + j
            if next_card_id <= len(line_matches) + 1:
                card_instances[str(next_card_id)] = card_instances.get(str(next_card_id), 0) + card_instances.get(str(card_id))
    return sum(card_instances.values())
