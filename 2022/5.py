import re


def run1(data: str, *args):
    crates, sorting = data.split("\n\n")
    pattern_boxes = re.compile(r"(.{3} ?)")

    match_lines = [pattern_boxes.findall(line) for line in crates.split('\n') if line.strip()]
    match_lines = reversed(match_lines)

    match_lines_clean = []
    for matches in match_lines:
        matches = [match.strip(" []") for match in matches]
        match_lines_clean.append(matches)

    indexes, matches_container = match_lines_clean[0], match_lines_clean[1:]

    stack_lists = [[] for _ in indexes]
    for i in range(len(indexes)):
        stack_list = []
        for j in range(len(matches_container)):
            crate = matches_container[j][i]
            if crate:
                stack_list.append(crate)
        stack_lists[i] = stack_list

    rows = sorting.split("\n")
    rows = [row for row in rows if row]

    pattern_sorting = re.compile(r"move\s([0-9]+)\sfrom\s([0-9]+)\sto\s([0-9]+)")
    sorting_moves = [pattern_sorting.findall(row)[0] for row in rows]

    for move in sorting_moves:
        move = [int(x) for x in move]
        for i in range(move[0]):
            crate = stack_lists[move[1] - 1].pop()
            stack_lists[move[2] - 1].append(crate)

    top_crates = [stack.pop() for stack in stack_lists]
    return "".join(top_crates)


def run2(data: str, *args):
    crates, sorting = data.split("\n\n")
    pattern_boxes = re.compile(r"(.{3} ?)")

    match_lines = [pattern_boxes.findall(line) for line in crates.split('\n') if line.strip()]
    match_lines = reversed(match_lines)

    match_lines_clean = []
    for matches in match_lines:
        matches = [match.strip(" []") for match in matches]
        match_lines_clean.append(matches)

    indexes, matches_container = match_lines_clean[0], match_lines_clean[1:]

    stack_lists = [[] for _ in indexes]
    for i in range(len(indexes)):
        stack_list = []
        for j in range(len(matches_container)):
            crate = matches_container[j][i]
            if crate:
                stack_list.append(crate)
        stack_lists[i] = stack_list

    rows = sorting.split("\n")
    rows = [row for row in rows if row]

    pattern_sorting = re.compile(r"move\s([0-9]+)\sfrom\s([0-9]+)\sto\s([0-9]+)")
    sorting_moves = [pattern_sorting.findall(row)[0] for row in rows]

    for move in sorting_moves:
        move = [int(x) for x in move]
        moved_crates = [stack_lists[move[1] - 1].pop() for _ in range(move[0])]
        for crate in reversed(moved_crates):
            stack_lists[move[2] - 1].append(crate)

    top_crates = [stack.pop() for stack in stack_lists]
    return "".join(top_crates)
