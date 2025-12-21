from dataclasses import dataclass

@dataclass
class Shape:
    index: int
    shape: list[str]

    @property
    def area(self):
        return "".join(self.shape).count("#")

@dataclass
class Instruction:
    size: tuple[int]
    shapes: list[tuple[int, Shape]]

with open("day12/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    shapes: dict[int, Shape] = {}
    instructions: list[Instruction] = []

    for i, line in enumerate(lines):
        if line and line[-1] == ":":
            s = Shape(int(line[:-1]), [])

            for x in lines[i+1:lines[i:].index("")+i]:
                s.shape.append(x)
            shapes[s.index] = s

        elif "x" in line:
            size, y = line.split(": ")
            size = list(map(int, size.split("x")))
            s = []
            for i, x in enumerate(y.split()):
                s.append((int(x), shapes[i]))
            instructions.append(Instruction(size, s))

part1 = 0
for instruction in instructions:

    total_area = sum(i*s.area for i, s in instruction.shapes)
    region_area = instruction.size[0] * instruction.size[1]

    if total_area <= region_area:
        part1 += 1


# Thank god the stupid approach worked!
print(part1)