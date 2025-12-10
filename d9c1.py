import time
t0 = time.time()
biggest_area = 0
points = []
with open("docs/d9c1.txt") as f:
    for p in f.read().splitlines():
        x,y = p.split(",")
        points.append((int(x),int(y)))
for i in range(len(points)-1):
    for j in range(i,len(points)):
        delta_x = abs(points[i][0]-points[j][0])+1
        delta_y = abs(points[i][1]-points[j][1])+1
        area = delta_x * delta_y
        if area > biggest_area:
            biggest_area = area
print(f"The biggest area found was: {biggest_area:,}.")
t1 = time.time()
print(f"Ran in {(t1-t0)*1000:,.2f}")