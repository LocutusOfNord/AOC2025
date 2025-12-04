with open("docs/d2c1.txt") as f:
    input = f.read()
ranges = input.replace("\n","").split(",")
invalid = 0
for r in ranges:
    print(r)
    for i in range(int(r.split("-")[0]),int(r.split("-")[1])+1):
        test = str(i)
        if len(test)%2==0:
            if test[0:len(test)//2] == test[len(test)//2:]:
                invalid += i
print(f"The sum of all invalid IDs was {invalid}.")