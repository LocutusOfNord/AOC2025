pos=50
zcount=0
with open("docs/d1c1.txt") as f:
    for line in f:
        direc = -1 if str(line[:1]).upper() == "L" else 1
        for i in range(0,int(line[1:])):
            pos = (pos + direc) % 100
            zcount += (pos == 0)
print("The arrow hit the 0 marker " + str(zcount) + " times.")