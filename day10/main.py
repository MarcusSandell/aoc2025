from dataclasses import dataclass
from itertools import combinations, combinations_with_replacement
import pulp

@dataclass
class Machine:
    light: str
    buttons: list[tuple[int]]
    joltage: list[int]


with open("day10/input.txt") as f:
    lines = [l.split(" ") for l in f.readlines()]
    machines = [Machine(l[0].replace("[","").replace("]",""),
                        [tuple(map(int, b.replace("(","").replace(")","").split(","))) for b in l[1:-1]],
                        list(map(int, l[-1].replace("{","").replace("}","").strip().split(",")))) for l in lines]


def find_light_combination(machine: Machine):
    for i in range(1, len(machine.buttons)):
        for comb in combinations(machine.buttons, i):
            s = [0 for _ in range(len(machine.light))]
            for button in comb:
                for index in button:
                    s[index] += 1

            s = "".join(["." if x%2==0 else "#" for x in s])
            if s == machine.light:
                return comb
    return None


def find_joltage_combination(machine: Machine):
    """This is all new to me"""
    prob = pulp.LpProblem("Minimize_button_presses", pulp.LpMinimize)

    upper_bound = sum(machine.joltage)
    variables = []

    for b in machine.buttons:
        variables.append(pulp.LpVariable(f"Button_{b}",
                                         lowBound=0,
                                         upBound=upper_bound,
                                         cat="Integer"))

    prob += sum(variables)

    for i, joltage in enumerate(machine.joltage):
        # Buttons affecting this joltage
        buttons = [variables[idx] for idx, button in enumerate(machine.buttons) if i in button]

        if buttons:
            prob += sum(buttons) == joltage

    prob.solve()

    print("Status:", pulp.LpStatus[prob.status])
    return int(pulp.value(prob.objective))


part1 = 0
part2 = 0
for i, machine in enumerate(machines):
    part1 += len(find_light_combination(machine))
    part2 += find_joltage_combination(machine)
    print(f"{i}/{len(machines)}")

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
