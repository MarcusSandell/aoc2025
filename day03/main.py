with open("day03/input.txt") as f:
    lines = [list(map(int, line)) for line in f.read().splitlines()]

p1_joltages = []
p2_joltages = []

nbr_of_batteries = 12

for line in lines:
    x = max(line[:-1])
    y = max(line[(line.index(x)+1):])

    p1_joltages.append(int(f"{x}{y}"))

    joltage = ""

    for i in range(0, nbr_of_batteries):
        if i + 1 == nbr_of_batteries:
            r = line
        else:
            r = line[:-(nbr_of_batteries-i-1)]
        x = max(r)
        line = line[line.index(x)+1:]
        joltage += str(x)
    p2_joltages.append(int(joltage))

print(f"Part 1: {sum(p1_joltages)}")
print(p2_joltages)
print(f"Part 2: {sum(p2_joltages)}")
