
with open("day09/input.txt") as f:
    lines = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

print(lines)
largest = 0
for i, c1 in enumerate(lines):
    for c2 in lines[i + 1:]:
        l = abs((c1[0]-c2[0])+1)
        w = abs((c1[1]-c2[1])+1)
        print(f"{c1}{c2}={l}, {w} = {l*w}")
        largest = max(largest, l*w)

print(largest)