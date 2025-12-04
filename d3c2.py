# numDigits = 2 for part 1, 12 for part 2
total,numDigits = 0,12
with open("docs/d3c1.txt") as f:
    for bank in f:
        ans,nums = "",list(bank.replace("\n",""))
        for i in range(numDigits,0,-1):
            ans += max(nums[:len(nums)-(i-1)])
            nums[:] = nums[nums.index(ans[-1])+1:]
        total += int(ans)
print(f"The banks can generate maximum {total} jolts.",end="")