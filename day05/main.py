with open("day05/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    str_r = lines[:lines.index("")]
    ingredients = map(int, lines[lines.index("")+1:])
    ranges = [tuple(map(int, r.split("-"))) for r in str_r]

# PART 1
ran = [range(r[0], r[1]) for r in ranges]

fresh = []

for ingredient in ingredients:
    if any(ingredient in x for x in ran):
        fresh.append(ingredient)

print(f"FRESH: {len(fresh)}")


# PART 2
ranges.sort(key=lambda x: x[0])

i = 0
while True:

    if i >= len(ranges)-1:
        break

    start, end = ranges[i]
    start2, end2 = ranges[i+1]
    if end >= start2 - 1:
        end = max(end, end2)
        ranges.pop(i+1)
        ranges[i] = (start, end)
        continue
    i += 1

print(sum(end - start + 1 for start, end in ranges))

