counter=50
zcount=0
with open("docs/d1c1.txt") as f:
    for line in f:
        amount = int(line[1:])%100
        if line[:1] == "L":
            amount = -amount
        counter = (counter+amount)%100
        if counter == 0:
            zcount += 1
f.close()
print("The arrow pointed at 0 " + str(zcount) + " times.")