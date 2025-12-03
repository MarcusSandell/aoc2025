with open("day03/input.txt") as f:
    lines = [list(map(int, line)) for line in f.read().splitlines()]

# 2 batteries for part 1 & 12 for part 2
NBR_OF_BATTERIES = 12


joltages = []
for line in lines:
    joltage = ""

    for i in range(0, NBR_OF_BATTERIES):
        x = max(line[:-(NBR_OF_BATTERIES-i-1) or None])
        line = line[line.index(x)+1:]
        joltage += str(x)
    joltages.append(int(joltage))

print(joltages)
print(f"Answer: {sum(joltages)}")
