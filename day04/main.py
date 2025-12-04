with open("day04/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def get_neighbours(lines:list[list], row:int, col:int):
    neighbours = []

    for drow, dcol in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        new_row = row + drow
        new_col = col + dcol
        if 0 <= new_row < len(lines) and 0 <= new_col < len(lines[0]) and lines[new_row][new_col] in ["@", "X"]:
            neighbours.append((new_row, new_col))
    
    return neighbours

removed = True
while removed:
    removed = False
    for row, x in enumerate(lines):
        for col, y in enumerate(lines[0]):
            if lines[row][col] == "@":

                n = get_neighbours(lines, row, col)
                if len(n) < 4:
                    s = list(lines[row])
                    s[col] = "X"
                    lines[row] = "".join(s)

                    removed = True
    


    for line in lines:
        print(line)

    print("")

flattened = "".join(lines)

print(flattened.count("X"))
