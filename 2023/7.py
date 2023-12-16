import copy
from collections import Counter


def card_sort1(item):
    card_order = "AKQJT98765432"
    return [card_order.index(char) for char in item]


def card_sort_dict1(dictonary):
    return card_sort1(dictonary["hand"])


class HandType:
    FIVE_OF_A_KIND = 0
    FOUR_OF_A_KIND = 1
    FULL_HOUSE = 2
    THREE_OF_A_KIND = 3
    TWO_PAIR = 4
    ONE_PAIR = 5
    HIGH_CARD = 6


def give_hand_type1(hand):
    count = Counter(Counter(hand).values())

    if count == Counter([5]):
        hand_type = HandType.FIVE_OF_A_KIND
    elif count == Counter([4, 1]):
        hand_type = HandType.FOUR_OF_A_KIND
    elif count == Counter([3, 2]):
        hand_type = HandType.FULL_HOUSE
    elif count == Counter([3, 1, 1]):
        hand_type = HandType.THREE_OF_A_KIND
    elif count == Counter([2, 2, 1]):
        hand_type = HandType.TWO_PAIR
    elif count == Counter([2, 1, 1, 1]):
        hand_type = HandType.ONE_PAIR
    elif count == Counter([1, 1, 1, 1, 1]):
        hand_type = HandType.HIGH_CARD
    else:
        raise ValueError(f"Unknown Hand Type for hand: {hand}")
    return hand_type


def run1(data: str):
    lines = data.split("\n")
    hands = [line.split(" ") for line in lines]
    groups = [[] for _ in range(8)]
    for hand, bid in hands:
        hand_type = give_hand_type1(hand)
        groups[hand_type].append({"hand": hand, "bid": bid})

    ordered_hands = []
    for group in groups:
        ordered_group = sorted(group, key=card_sort_dict1)
        [ordered_hands.append(hand) for hand in ordered_group]

    total_winnings = 0
    for i, hand in enumerate(reversed(ordered_hands)):
        total_winnings += int(hand.get("bid")) * (i+1)
    return total_winnings


def card_sort2(item):
    card_order = "AKQT98765432J"
    return [card_order.index(char) for char in item]


def card_sort_dict2(dictonary):
    return card_sort2(dictonary["hand"])


def give_hand_type2(hand):
    char_counts = Counter(hand)
    jockers = char_counts.get("J")
    char_count_values = list(char_counts.values())
    if not jockers == len(hand):
        del char_counts["J"]
        char_count_values = list(char_counts.values())
        char_count_values.sort(reverse=True)

        if jockers:
            try:
                char_count_values[0] += jockers
            except IndexError:
                print("[===]", char_count_values)
    count = Counter(char_count_values)
    print(f"{hand} | {char_count_values} | {count}")

    if count == Counter([5]):
        hand_type = HandType.FIVE_OF_A_KIND
    elif count == Counter([4, 1]):
        hand_type = HandType.FOUR_OF_A_KIND
    elif count == Counter([3, 2]):
        hand_type = HandType.FULL_HOUSE
    elif count == Counter([3, 1, 1]):
        hand_type = HandType.THREE_OF_A_KIND
    elif count == Counter([2, 2, 1]):
        hand_type = HandType.TWO_PAIR
    elif count == Counter([2, 1, 1, 1]):
        hand_type = HandType.ONE_PAIR
    elif count == Counter([1, 1, 1, 1, 1]):
        hand_type = HandType.HIGH_CARD
    else:
        raise ValueError(f"Unknown Hand Type for hand: {hand}")
    return hand_type


def run2(data: str):
    lines = data.split("\n")
    hands = [line.split(" ") for line in lines]
    groups = [[] for _ in range(8)]
    for hand, bid in hands:
        hand_type = give_hand_type2(hand)
        groups[hand_type].append({"hand": hand, "bid": bid})

    ordered_hands = []
    for group in groups:
        ordered_group = sorted(group, key=card_sort_dict2)
        [ordered_hands.append(hand) for hand in ordered_group]

    total_winnings = 0
    for i, hand in enumerate(reversed(ordered_hands)):
        total_winnings += int(hand.get("bid")) * (i + 1)
    return total_winnings
