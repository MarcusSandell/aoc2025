
with open("day07/input.txt") as f:
    lines = [list(line.strip()) for line in f]

tachyons = [(0, lines[0].index("S"))]

def part1(lines):
    splits = set()
    seen = set()
    while tachyons:
        row, col = tachyons.pop()

        if row+1 >= len(lines):
            continue

        if lines[row+1][col] == "^":

            splits.add((row,col))
            if (row+1, col-1) not in seen:
                seen.add((row+1, col-1))
                lines[row+1][col-1] = "|"
                tachyons.append((row+1, col-1))

            if (row+1, col+1) not in seen:
                seen.add((row+1, col+1))
                lines[row+1][col-1] = "|"
                tachyons.append((row+1, col+1))


        elif (row+1, col) not in seen:
            tachyons.extend([(row+1, col)])
            lines[row+1][col] = "|"
    return len(splits)


def part2(lines):

    d = {lines[0].index("S"): 1}

    for row_i, row in enumerate(lines[1:]):
        if "^" not in row:
            continue

        rd = {}

        for col_i, timelines in d.items():
            if row[col_i] == ".":
                rd[col_i] = rd.get(col_i, 0) + timelines

            elif row[col_i] == "^":
                rd[col_i + 1] = rd.get(col_i + 1, 0) + timelines
                rd[col_i - 1] = rd.get(col_i - 1, 0) + timelines

            lines[row_i][col_i] = str(timelines)

        d = rd

        for line in lines:
            print(line)
        print()
    return sum(d.values())

print(part2(lines))

