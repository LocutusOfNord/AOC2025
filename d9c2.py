# This is the third way I've tried to solve this one.
# Hopefully this approach brings joy.
import time
t0 = time.time()

def check_collision(box_corners):
    x_range = (min(box_corners[0][0], box_corners[1][0]), max(box_corners[0][0], box_corners[1][0]))
    y_range = (min(box_corners[0][1], box_corners[1][1]), max(box_corners[0][1], box_corners[1][1]))
    for l in horiz_lines:
        if y_range[0] < l[2] < y_range[1]:
            if (l[0] < x_range[0] < l[1]) or (l[0] < x_range[1] < l[1]):
                return True
            if (x_range[0] < l[0] < x_range[1]) or (x_range[0] < l[1] < x_range[1]):
                return True
            if l[0] == x_range[0] and l[1] == x_range[1]:
                return True
    for l in vert_lines:
        if x_range[0] < l[0] < x_range[1]:
            if (l[2] < y_range[0] < l[3]) or (l[2] < y_range[1] < l[3]):
                return True
            if (y_range[0] < l[2] < y_range[1]) or (y_range[0] < l[3] < y_range[1]):
                return True
            if l[2] == y_range[0] and l[3] == y_range[1]:
                return True
    return False

#TODO add memoization?
# Ran in 2.4 secs, fuck it
vert_lines = []
horiz_lines = []
shape_points = []
biggest_area = 0

with open("docs/d9c1.txt") as f:
    for line in f.read().splitlines():
        x,y = line.split(",")
        point = (int(x),int(y))
        if shape_points:
            if shape_points[-1][0] == point[0]:
                vert_lines.append((min(point[0],shape_points[-1][0]),
                                    max(point[0],shape_points[-1][0]),
                                    min(point[1],shape_points[-1][1]),
                                    max(point[1],shape_points[-1][1])))
            else:
                horiz_lines.append((min(point[0],shape_points[-1][0]),
                                   max(point[0],shape_points[-1][0]),
                                   min(point[1],shape_points[-1][1]),
                                   max(point[1],shape_points[-1][1])))
        shape_points.append(point)

if shape_points[0][0] == shape_points[-1][0]:
    vert_lines.append((min(shape_points[0][0],shape_points[-1][0]),
                       max(shape_points[0][0],shape_points[-1][0]),
                       min(shape_points[0][1],shape_points[-1][1]),
                       max(shape_points[0][1],shape_points[-1][1])))
else:
    horiz_lines.append((min(shape_points[0][0],shape_points[-1][0]),
                       max(shape_points[0][0],shape_points[-1][0]),
                       min(shape_points[0][1],shape_points[-1][1]),
                       max(shape_points[0][1],shape_points[-1][1])))

for i in range(len(shape_points)-1):
    for j in range(i+1,len(shape_points)):
        corners = [shape_points[i], shape_points[j]]
        area = (abs(corners[0][0]-corners[1][0])+1)*(abs(corners[0][1]-corners[1][1])+1)
        if area > biggest_area:
            if not check_collision(corners):
                biggest_area = area
print(f"The biggest area from a valid rectangle was {biggest_area:,}.")
t1 = time.time()
print(f"Ran in {(t1-t0)*1000:,.2f} ms.")