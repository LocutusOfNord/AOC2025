from math import prod
problems, sumTotal = [], 0
with open("docs/d6c1.txt") as f:
    for line in f.read().splitlines():
        problems.append(line)

nums = []
for i in range(len(problems[0])-1,-1,-1):
    num = ""
    for j in range(len(problems)-1):
        num += problems[j][i]
    if num.strip():
        nums.append(int(num))
    if problems[-1][i] == "+":
        sumTotal += sum(nums)
        nums = []
    elif problems[-1][i] == "*":
        sumTotal += prod(nums)
        nums = []
    elif problems[-1][i] != " ":
        print("Somethin' strange in the neighborhood")

print(f"The sum total of the answers is {sumTotal:,}.")