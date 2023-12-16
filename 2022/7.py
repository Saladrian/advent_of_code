
def calculate_size(fs, fs_key) -> dict:
    sizes = {}
    size_sum = 0
    for key, value in fs.items():
        if isinstance(value, dict):
            result = calculate_size(value, key)
            sizes.update(result)
            sizes[key] = result[key]
            size_sum += sum(result.values())
        else:
            size_sum += value
    sizes[fs_key] = size_sum
    return sizes


def run1(data: str, *args):
    fs = {"/": {}}
    current_path = []
    lines = data.split("\n")
    for line in lines:
        parts = line.split(" ")
        currently_at = fs
        for path in current_path:
            currently_at = currently_at[path]
        if line.startswith("$"):
            if parts[1] == "cd":
                if parts[2] == "/":
                    current_path = ["/"]
                elif parts[2] == "..":
                    current_path.pop()
                else:
                    current_path.append(parts[2])
        elif line.startswith("dir"):
            currently_at[parts[1]] = {}
        else:
            currently_at[parts[1]] = int(parts[0])

    dict_sizes = calculate_size(fs["/"], "/")
    print(dict_sizes)
    size_sum = 0
    for size in dict_sizes.values():
        if size < 100000:
            size_sum += size
    return size_sum


def run2(data: str, *args):

    return
