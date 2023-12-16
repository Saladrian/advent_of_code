import re
import time

nodes_pattern = re.compile(r"^(\w+?) = \((\w+?), (\w+?)\)$", re.MULTILINE)


def format_data(data: str) -> (str, str):
    instructions, nodes_raw = data.split("\n\n")

    nodes_list = re.findall(nodes_pattern, nodes_raw)
    nodes = {v1: {"L": v2, "R": v3} for v1, v2, v3 in nodes_list}

    return instructions, nodes


def run1(data: str):
    instructions, nodes = format_data(data)

    current_node = "AAA"
    count = 0
    while not current_node == "ZZZ":
        index = count % len(instructions)

        instruction = instructions[index]
        current_node = nodes.get(current_node).get(instruction)

        count += 1
    return count


def run2(data: str):
    instructions, nodes = format_data(data)

    current_nodes = [node for node in nodes.keys() if node.endswith("A")]
    count = 0
    print(f"Start: {current_nodes}")
    while not all(node.endswith("Z") for node in current_nodes):
        print(all(node.endswith("Z") for node in current_nodes))
        index = count % len(instructions)
        instruction = instructions[index]

        updated_nodes = [nodes.get(node).get(instruction) for node in current_nodes]
        current_nodes = updated_nodes

        count += 1
        print(f"{count}({index}) | {current_nodes} | {instruction}")
        # time.sleep(1)
    return count
