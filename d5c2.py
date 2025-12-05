ranges = []
numOfProds = 0
#read 'em in
with open("docs/d5c1.txt") as f:
    for line in f:
        if len(line.strip()) > 0:
            ranges.append([int(x) for x in line.replace("\n", "").split("-")])
        else:
            break
i=0
ranges.sort()
while i < len(ranges)-1:
    #if the upper bound of this range extends into the next
    if ranges[i][1] >= ranges[i+1][0]:
        #does this range end in the next range, or is next range contained WITHIN this range?
        if ranges[i][1] < ranges[i+1][1]:
            ranges[i][1] = ranges[i+1][1]
        ranges.pop(i+1)
    else:
        #this range has no overlap with next highest range
        numOfProds += ranges[i][1] - ranges[i][0] + 1
        i += 1
#gotta get that last range too
numOfProds += ranges[-1][1] - ranges[-1][0] + 1
print(f"{numOfProds:,} products are considered fresh.")