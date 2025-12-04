with open("docs/d2c1.txt") as f:
    inputFile = f.read()
'''This one takes FOREVER to run!'''
total = 0
rangeNum = 0
# make a list of the ranges and loop through
ranges = inputFile.replace("\n", "").split(",")
for testedRange in ranges:
    rangeNum += 1
    indexes = [int(x) for x in testedRange.split("-")]
    for testNum in range(indexes[0], indexes[1]+1):
        invalid = False
        # if substring must be repeated >=x2,logically we only need to test first half
        for length in range(1,(len(str(testNum))//2)+1):
            # if repeated substrings, total length must be multiple of substring length
            if len(str(testNum))%length==0:
                # chunk into substrings and add to set (no dups). If set contains only one, invalid.
                chunks = {str(testNum)[x:x+length] for x in range(0,len(str(testNum)),length)}
                if len(chunks) == 1:
                    invalid = True
                    break
        if invalid:
            total += testNum

print(f"The sum of all invalid IDs was {total:,}.")