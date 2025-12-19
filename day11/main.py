from functools import lru_cache

with open("day11/input.txt") as f:
    nodes = {l.split(": ")[0]: l.strip().split(" ")[1:] for l in f.readlines()}

def get_paths(pos:str, path: list):

    path.append(pos)

    if pos == "out":
        return [path]

    connections = nodes[pos]

    paths = []
    for c in connections:
        if c not in path:
            x = path.copy()
            paths.extend(get_paths(c, x))

    return paths

# paths = get_paths("you", [])
# print(f"Part 1: {len(paths)}")



def part2():
    nodes_tuple = {k: tuple(v) for k, v in nodes.items()}
    
    @lru_cache(maxsize=None)
    def count_paths_through(pos: str, seen_fft: bool, seen_dac: bool):
        
        if pos == "end":
            # Only count if we've visited both required nodes
            return 1 if seen_fft and seen_dac else 0
        
        if pos not in nodes_tuple:
            return 0
        
        # Update flags if we're at a required node
        seen_fft = seen_fft or pos == "fft"
        seen_dac = seen_dac or pos == "dac"
        
        connections = nodes_tuple[pos]
        
        total = 0
        for c in connections:
            total += count_paths_through(c, seen_fft, seen_dac)
        
        return total
    
    count = count_paths_through("svr", False, False)
    print(f"Part 2: {count}")

part2()
