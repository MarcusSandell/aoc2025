with open("day02/input.txt") as f:
    line = f.readline()
    ids = [list(map(int, r.split("-"))) for r in line.split(",")]
    # flatened_ids = sum(ids, [])

invalid_ids = []

for first, last in ids:
    print(f"{first}-{last}")
    for id in range(first, last+1):

        id = str(id)

        # Perhaps a bit brute forcy but it works xd

        permutations = [id[:x] for x in range(1, (len(id)) // 2 + 1)]
        permutations = [p * int(len(id) / len(p)) for p in permutations]

        if any(p == id for p in permutations):
            invalid_ids.append(int(id))

        # Part 1
        # left = id[:len(id)//2]
        # right = id[len(id)//2:]

        # if left == right:
        #     invalid_ids.append(int(id))



print(invalid_ids)
print(sum(invalid_ids))