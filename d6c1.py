from math import prod
sumTotal = 0
with open("docs/d6c1.txt") as f:
    problems = [list(col) for col in zip(*[x.split() for x in f.read().splitlines()])]

for p in problems:
    if p[-1] == "+":
        sumTotal += sum(list(map(int,p[0:-1])))
    elif p[-1] == "*":
        sumTotal += prod(list(map(int,p[0:-1])))

print(f"The sum total is {sumTotal:,}.")