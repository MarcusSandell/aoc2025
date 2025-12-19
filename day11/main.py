from functools import lru_cache

with open("day11/input.txt") as f:
    nodes = {l.split(": ")[0]: l.strip().split(" ")[1:] for l in f.readlines()}

# def get_paths(pos:str, path: list):

#     path.append(pos)

#     if pos == "out":
#         return [path]

#     connections = nodes[pos]

#     paths = []
#     for c in connections:
#         if c not in path:
#             x = path.copy()
#             paths.extend(get_paths(c, x))

#     return paths

# paths = get_paths("you", [])
# print(f"Part 1: {len(paths)}")

@lru_cache
def get_nbr_of_paths(src, dst):
    if src == dst:
        return 1
    if src == "out":
        return 0

    return sum(get_nbr_of_paths(x, dst) for x in nodes[src])

print(f"Part 1: {get_nbr_of_paths("you", "out")}")

part2 = get_nbr_of_paths("svr", "fft") * get_nbr_of_paths("fft", "dac") * get_nbr_of_paths("dac", "out")
part2 += get_nbr_of_paths("svr", "dac") * get_nbr_of_paths("dac", "fft") * get_nbr_of_paths("fft", "out")

print(f"Part 2: {part2}")