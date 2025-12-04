grid = []
with open("docs/d4c1.txt") as f:
    for line in f:
        grid.append(list(line.replace("\n","")))
removed = 0
x_dist, y_dist = len(grid[0]), len(grid)
while True:
    prev = removed
    for y in range(0,y_dist):
        for x in range(0,x_dist):
            if grid[y][x] == "@":
                neighbors = 0
                if y>0:
                    neighbors += grid[y-1][max(x-1,0):min(x+2,x_dist)].count("@")
                if y<(y_dist-1):
                    neighbors += grid[y+1][max(x-1,0):min(x+2,x_dist)].count("@")
                neighbors += 1 if x>0 and grid[y][x-1] == "@" else 0
                neighbors += 1 if x<x_dist-1 and grid[y][x+1] == "@" else 0
                if neighbors<4:
                    grid[y][x] = "."
                    removed += 1
    if removed==prev:
        break
print(f"{removed} rolls could be removed.")