import re


data_pattern = re.compile(r"seeds:(.*?)\n|(?=(\n(\w+)-to-(\w+) map:\n(([^a-z]| |$)*)))")


def format_category_maps(data):
    matched_data = re.findall(data_pattern, data)
    seeds_raw = matched_data[0][0]
    seeds = [int(seed) for seed in seeds_raw.split(" ") if seed]

    category_maps = []
    for match in matched_data[1:]:
        from_type = match[2]
        to_type = match[3]
        category_maps_raw = match[4]

        ranges = []
        for category_map_raw in category_maps_raw.split("\n"):
            if category_map_raw:
                to_start, from_start, range_length = category_map_raw.split(" ")
                ranges.append({"from": int(from_start), "to": int(to_start), "range": int(range_length)})

        category_map = {
            "type": {"from": from_type, "to": to_type},
            "ranges": ranges
        }
        category_maps.append(category_map)
    return seeds, category_maps


def map_seed_to_loacation(category_maps):
    seed_to_location = {}
    category_map = [category_map for category_map in category_maps if category_map["type"].get("from") == "seed"][0]
    from_seed_ranges = [(a_range.get("from"), a_range.get("range")) for a_range in category_map.get("ranges")]
    for seed_range in from_seed_ranges:
        for seed in range(seed_range[0], sum(seed_range)):
            location = find_location("seed", seed, category_maps)
            seed_to_location[seed] = location
    print(seed_to_location)


def find_location(from_type, number, category_maps):
    category_map = [category_map for category_map in category_maps if category_map["type"].get("from") == from_type][0]
    from_seeds = []

    next_type = category_map["type"].get("to")

    next_number = None
    for a_range in category_map.get("ranges"):
        from_start = a_range.get("from")
        to_start = a_range.get("to")
        range_lenght = a_range.get("range")

        if number in range(from_start, (from_start + range_lenght)):
            range_diff = number - from_start
            next_number = to_start + range_diff

    if next_number is None:
        next_number = number

    if next_type == "location":
        return next_number
    else:
        return find_location(next_type, next_number, category_maps)


def run1(data: str):
    seeds, category_maps = format_category_maps(data)
    map_seed_to_loacation(category_maps)

    locations = []
    for seed in seeds:
        location = find_location("seed", seed, category_maps)
        locations.append(location)

    locations.sort()
    return locations[0]


def run2(data: str):
    seed_values, category_maps = format_category_maps(data)
    seed_ranges = [(seed_values[i], seed_values[i + 1]) for i in range(0, len(seed_values), 2)]

    locations = []
    for first_seed, seed_range in seed_ranges:
        for seed in range(first_seed, first_seed + seed_range):
            location = find_location("seed", seed, category_maps)
            locations.append(location)

    locations.sort()
    return locations[0]
