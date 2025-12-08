# This is a totally scrapped attempt at this problem.
# I was on completely the wrong track because I misunderstood
# what exactly I was supposed to be calculating, and went down
# an unnecessary recursion rabbithole.
# Uploading with successful answers because failure is always an option.
def analyse_branch(rem):
    global timelines
    if len(rem) > 1:
        print(rem[0])
        print(rem[1])
        for i, char in enumerate(rem[1]):
            #            print(i)
            #            print(rem)
            #            print(rem[0][i])
            if rem[0][i] == "|":
                print("TRUE")
                print(char)
                if char == ".":
                    temp = [row[:] for row in rem[1:]]
                    temp[0][i] = "|"
                    print("CONTINUE")
                    analyse_branch(temp)
                elif char == "^":
                    if i>0 and rem[1][i-1] == ".":
                        timelines += 1
                        temp = [row[:] for row in rem[1:]]
                        temp[0][i-1] = "|"
                        print("LEFT")
                        analyse_branch(temp)
                    if i < len(rem[1])-1 and rem[1][i+1] == ".":
                        timelines += 1
                        temp = [row[:] for row in rem[1:]]
                        temp[0][i+1] = "|"
                        print("RIGHT")
                        analyse_branch(temp)

timelines = 0
with open("docs/d7c1.txt") as f:
    schema = [list(x.replace("S","|")) for x in f.read().splitlines()]
analyse_branch(schema)

print(timelines)