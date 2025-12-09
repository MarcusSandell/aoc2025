with open("day09/input.txt") as f:
    lines = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]


def part1(lines):
    rectangles = {}
    for i, c1 in enumerate(lines):
        for c2 in lines[i + 1:]:
            l = abs(c1[0]-c2[0]) + 1
            w = abs(c1[1]-c2[1]) + 1
            rectangles[l*w] = (c1, c2)

    return sorted(rectangles, reverse=True), rectangles

def part2_2(verticies:list):
    sizes, d = part1(lines)

    verticies.append(verticies[0])
    for size in sizes:
        failed = False

        v1, v2 = d[size]
        left = min(v1[0], v2[0])
        right = max(v1[0], v2[0])
        top = min(v1[1], v2[1])
        bottom = max(v1[1], v2[1])

        for i, (col, row) in enumerate(verticies[:-1]):
            d_col, d_row = verticies[i + 1]

            if row == d_row:  # Horizontal edge
                v_left = min(col, d_col)
                v_right = max(col, d_col)

                if top < row < bottom and v_left < right and v_right > left:
                    failed = True
                    break

            elif col == d_col:  # Vertical edge
                v_top = min(row, d_row)
                v_bottom = max(row, d_row)
                
                if left < col < right and v_top < bottom and v_bottom > top:
                    failed = True
                    break

        if not failed:
            return size, d[size]

print(part2_2(lines))
