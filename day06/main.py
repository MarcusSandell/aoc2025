with open("day06/input.txt") as f:
    lines = list(zip(*[line.strip().split() for line in f.readlines()]))

ans = 0
for col in lines:
    ans += eval(f"{col[-1]}".join(col[:-1]))

print(f"Part 1: {ans}")

with open("day06/input.txt") as f:
    lines = list(zip(*f.readlines()))

ans = 0
nums = []
j = 0
for i, line in enumerate(lines):
    if line[-1] != " " and i != 0:
        nums.append(lines[j:i-1])

        j = i
nums.append(lines[j:])

for line in nums:
    n = []
    sign = line[0][-1]
    for l in line:
        n.append("".join(l[:-1]).strip())

    print(f"{sign}".join(n))
    ans += eval(f"{sign}".join(n))

print(ans)
