total = 0
with open("docs/d3c1.txt") as f:
    for bank in f:
        nums = list(bank.replace("\n",""))
        tens = max(nums[0:-1])
        ones = max(nums[nums.index(tens)+1:])
        total += (int(tens) * 10) + int(ones)
print(f"The banks can generate maximum {total} jolts.")