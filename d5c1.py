ranges,fresh = [],0
with open("docs/d5c1.txt") as f:
    for line in f:
        if len(line.strip()) > 0:
            line = [int(x) for x in line.replace("\n", "").split("-")]
            if len(line) == 2:
                ranges.append(line)
            else:
                for r in ranges:
                    if r[0] <= line[0] <= r[1]:
                        fresh += 1
                        break

print(f"There are {fresh:,} fresh products.")