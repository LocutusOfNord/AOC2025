with open("docs/d7c1.txt") as f:

    # Read in the file as a list of lists (matrix) of ints,
    # replacing . with 0, start with 1, and ^ with -1
    grid = [[{".": 0, "S": 1, "^": -1}[c] for c in line] for line in f.read().splitlines()]

    # loop through each character in each line
    for x,row in enumerate(grid):
        if x<len(grid)-1:
            for y,col in enumerate(row):
                # if this is > 0, it contains particle timelines
                if col > 0:
                    # if the spot below the particle is not a splitter
                    # add col more particles (timeline) to that space
                    if grid[x + 1][y] > -1:
                        grid[x + 1][y] += col
                    # if it IS a splitter, add col particles (timeline) to the
                    # spaces on either side of the space directly below (split it)
                    else:
                        if y > 0:
                            grid[x + 1][y - 1] += col
                        if y < len(grid[0])-1:
                            grid[x + 1][y + 1] += col

# now the last line, containing no splitters, is just a list
# of positive ints indicating how many particle timelines pass
# through each spot. Add em up for answer.
print(f"There are {sum(grid[-1]):,} timelines.")