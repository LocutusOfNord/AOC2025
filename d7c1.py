split = 0
prev_line = []

with open("docs/d7c1.txt") as f:
    for line in [list(x) for x in f.read().splitlines()]:

        for i, char in enumerate(line):

            #is this char a splitter and is there a beam coming in?
            if char == "^" and prev_line[i]=="|":
                split += 1
                if i > 0 and line[i-1] == ".":
                    line[i-1] = "|"
                if i < len(line)-1 and line[i+1] == ".":
                    line[i+1] = "|"
            #starting beam and carrying unsplit beams
            if char == "." and prev_line and prev_line[i] in ("S", "|"):
                line[i] = "|"
        prev_line = line
        print(f"{line} :{split}")
print(f"The beam was split {split:,} times.")