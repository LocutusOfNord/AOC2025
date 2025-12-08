# I am pretty certain that doing this the naive way is going to be SO
# unoptimized and take SO long to run, but here goes
import math

num_to_multiply = 3
points = []
distances = {}
circuits=[]
ans = -1

# Read in points, add points to points list as tuple, create dict entry
# for distance to every previous point (key = point 1 index,point 2 index).
with open("docs/d8c1.txt") as f:
    for line in f.read().splitlines():
        points.append(tuple([int(x) for x in line.split(",")]))
        for i in range(len(points)-1):
            last = len(points)-1
            distances[(i,last)] = math.sqrt(
                abs(points[i][0] - points[last][0])**2 +
                abs(points[i][1] - points[last][1])**2 +
                abs(points[i][2] - points[last][2])**2
            )

# sort the distances and organize the specified number of shortest
# ones into sets of links
sorted_distances = sorted(distances, key=distances.get)
for i in range(len(distances)):
    a_index,b_index = sorted_distances[i][0], sorted_distances[i][1]
    # which indices, if any, contain sets containing these points?
    set_with_a, set_with_b = -1, -1
    for j in range(len(circuits)):
        if a_index in circuits[j]:
            set_with_a = j
        if b_index in circuits[j]:
            set_with_b = j

    # if both ends of link found in existing sets
    if set_with_a > -1 and set_with_b > -1:
        if set_with_a != set_with_b:
            circuits[set_with_a].update(circuits[set_with_b])
            circuits.pop(set_with_b)
    # only a found in existing set
    elif set_with_a > -1:
        circuits[set_with_a].add(b_index)
    # only b found
    elif set_with_b > -1:
        circuits[set_with_b].add(a_index)
    #neither found
    else:
        circuits.append({a_index, b_index})
    # if points in different set, or neither one found,
    # and they therefore need to be linked, multiply x coords
    if set_with_a != set_with_b or set_with_a + set_with_b == -2:
        ans = points[a_index][0]*points[b_index][0]

print(f"The product of the x coords of the last two linked nodes is {ans:,}.")