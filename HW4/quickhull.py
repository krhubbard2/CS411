# Kelby Hubbard
# Started: 2021-10-30
# Updated: 2021-11-03
# CS411 -- Analysis of Algorithims HW4
# quickhull.py

# NOTICE: This program uses Pyplot (matplotlib) which is not standard in the Python library. Pyplot must be installed on your machine for use of this program. Visit https://matplotlib.org/stable/users/installing.html for more information.

import random # For pseudo-random number generation
import time # For timer
import matplotlib.pyplot as plt # For plotting
import math # For base_10 rounding

# Point Class
# Point contains an X and Y value corresponding to a 2D point.
class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    
    # Prints point in form "(X,Y)"
    def print(self):
        print("({}, {}) ".format(self.X, self.Y), end='')

# Number of randomly distributed 2D points inside unit square.
# Ensures positive integer entries only.
def size_n():
    n = 0
    while True:
        try:
            n = int(input("What would you like `n` to be: "))
            if n < 0:
                print("Must be a positive integer.")
                continue
            break
        except ValueError or n < 0:
            print("Please enter a positive integer.")
            continue
    return n
    
# Hull Input -- Contains randomly generated Points within the unit square.
hull_input = []

# Stores points of convex hull
hull = []

# Returns side of line point lies in
def point_side(p1, p2, p):
    val = ((p.Y - p1.Y) * (p2.X - p1.X) - (p2.Y - p1.Y) * (p.X - p1.X))
    if (val > 0):
        return 1
    if (val < 0):
        return -1
    else: 
        return 0

# Returns distance between point p and the line from p1 -> p2
def line_dist(p1, p2, p):
    val = ((p.Y - p1.Y) * (p2.X - p1.X) - (p2.Y - p1.Y) * (p.X - p1.X))
    return abs(val)

# Recursive main driver for quick hull algorithim
def quick_hull(hull_input, n, p1, p2, side):
    index = -1
    max_dist = 0

    for i in range(0, n):
        temp = line_dist(p1, p2, hull_input[i])
        if ((point_side(p1, p2, hull_input[i]) == side) and (temp > max_dist)):
            index = i
            max_dist = temp
    
    # Adds convex hull to final hull list (if not already added)
    if (index == -1):
        if p1 not in hull: hull.append(p1)
        if p2 not in hull: hull.append(p2)
        return

    # Recursive implementation (divide & conquer)
    quick_hull(hull_input, n, hull_input[index], p1, -(point_side(hull_input[index], p1, p2)))
    quick_hull(hull_input, n, hull_input[index], p2, -(point_side(hull_input[index], p2, p1)))

# Main function to be called to perform quick hull. 
def quick(hull_input, n):
    # Base case
    if (n < 3):
        print("Convex hull not possible")
        return
    
    # Find x minimum and x maximum coord
    x_min, x_max = 0, 0
    for i in range(1, n):
        if (hull_input[i].X < hull_input[x_min].X):
            x_min = i
        if (hull_input[i].X > hull_input[x_max].X):
            x_max = i
    
    # Recursive call joining x_min and x_max
    quick_hull(hull_input, n, hull_input[x_min], hull_input[x_max], 1)
    quick_hull(hull_input, n, hull_input[x_min], hull_input[x_max], -1)
 
# Used for rounding. Ensures numbers generated are porportional to how many points are being requested.
def round_base_10(x):
    if x < 0:
        return 0
    elif x == 0:
        return 10
    return 10**math.ceil(math.log10(x))

# Grab user input for size of N
n = size_n()
n_places = round_base_10(n)
print("Generating {} random points within the unit square".format(n))
# Fills hull_input with n randomly generated points.
for i in range(n):
    point = Point(round(random.random(), n_places), round(random.random(), n_places))
    hull_input.append(point)
print("{} points generated.".format(len(hull_input)))

print("Performing quickhull. Starting timer.")
start_time = time.time()
quick(hull_input, n)
total_time = time.time()-start_time
print("Quickhull complete. Run time was {} seconds".format(total_time))

print("Now generating graph. Black points are inside the convex hull whereas red points are the convex hull.")

# Grab x and y coordinates from all points for use in pyplot.
xs = []
ys = []
for i in range(len(hull_input)):
    xs.append(hull_input[i].X)
    ys.append(hull_input[i].Y)

# Grab x and y coordinates from convex hull points for use in pyplot.
xs_hull = []
ys_hull = []
for i in range(len(hull)):
    xs_hull.append(hull[i].X)
    ys_hull.append(hull[i].Y)

# Show plot
plt.scatter(xs, ys, color='k', label="Inside Convex Hull")
plt.scatter(xs_hull, ys_hull, color='r', label="Convex Hull")
plt.ylabel('Y Coordinate')
plt.xlabel('X Coordinate')
plt.title('Convex Hull')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
plt.show()