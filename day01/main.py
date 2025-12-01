with open("day01/input.txt") as f:
    lines = [(line.strip()[0], int(line.strip()[1:])) for line in f.readlines()]

positions = [50]
over_underflows = 0

for direction, distance in lines:

    new_pos = (positions[-1] + distance * (-1 if direction == "L" else 1)) % 100

    # Tried to make this work with this janky truncate divide but it was messy
    # int(str(abs((positions[-1] + distance) / 100)).split(".")[0])

    if direction == "R":
        over_underflows += (positions[-1] + distance) // 100
    else:
        over_underflows += ((100 - positions[-1]) % 100 + distance) // 100

    positions.append(new_pos)

print(positions.count(0))
print(over_underflows)
