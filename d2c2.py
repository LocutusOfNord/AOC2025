# read in the file
with open("docs/d2c1.txt") as f:
    inputFile = f.read()
# make a list of the ranges
ranges = inputFile.replace("\n", "").split(",")
total = 0
rangeNum = 0
# loop through ranges
for testedRange in ranges:
    rangeNum += 1
    # get start and end of range and iterate through range,
    # being sure to test final as well
    indexes = [int(x) for x in testedRange.split("-")]
    for testNum in range(indexes[0], indexes[1]+1):
        #        perc = (testNum-indexes[0])/(indexes[1]-indexes[0]) * 100
        perc = "{:.2f}".format((testNum-indexes[0])/(indexes[1]-indexes[0]) * 100)
        print(f"{rangeNum}/{len(ranges)} : {perc}%")
        invalid = False
        # if the substring must be repeated at least twice,
        # logically we only need to test lengths up to half
        for length in range(1,(len(str(testNum))//2)+1):
            # if invalid numbers are made up of repeated substrings,
            # it can't be invalid if the length is not a multiple of the
            # substring's length
            if len(str(testNum))%length==0:
                # chunk tested number into length-long strings and put them in
                # a set. Since sets don't allow duplicates, a tested number made of
                # the same string repeated will have only one item in the set.
                # If one item in set, therefore invalid, kick out, add to the sum.
                chunks = {str(testNum)[x:x+length] for x in range(0,len(str(testNum)),length)}
                if len(chunks) == 1:
                    invalid = True
                    break
        if invalid:
            total += testNum

print(f"The sum of all invalid IDs was {total}.")