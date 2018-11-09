import numpy as np
import os
import copy
import math
import random
import time




# distance(pointA, pointB) calculates the Euclidean distance between two points A and B
def distance(pointA, pointB):
    #print(pointA, pointB)
    x_diff = pointA[1] - pointB[1]
    y_diff = pointA[2] - pointB[2]
    result = pow(x_diff, 2) + pow(y_diff, 2)
    result = math.sqrt(result)
    return result

# pathlen(points) returns the length of the path points
def pathlen(points):
    size = len(points)
    if size <= 1:
        return 0
    plen = 0
    for i in range(size-1):
        plen += distance(points[i], points[i+1])
    return plen

# best_neighbor returns the minimum-length path of swapping two nodes in points
def best_neighbor(points):
    min_len = float('inf')
    size = len(points)
    for i in range(1, size-2):
        for j in range(i+1, size-1):
            new_points = copy.deepcopy(points)
            new_points[i], new_points[j] = new_points[j], new_points[i]
            plen = pathlen(new_points)
            if plen < min_len:
                min_len = plen
                neighbor = new_points
    return min_len, neighbor

# rand_state(points) returns a random TSP tour
def rand_state(points):
    inter_points = points[1:len(points)-1]
    random.shuffle(inter_points)
    inter_points = [points[0]] + inter_points + [points[0]]
    return inter_points

def hill_climb(points):
    start_time = time.time()
    curr = rand_state(points)
    cost = pathlen(curr)
    steps = 0
    while True:
        if time.time() - start_time > 300:
            print("hill_climb---time exceeds 5 minutes---")
            return curr, cost, steps
        new_cost, next = best_neighbor(curr)
        if cost <= new_cost:
            break
        steps += 1
        curr = next
        cost = new_cost
    return curr, cost, steps

'''f = open('tsp_problems/16/instance_4.txt')
content = f.readlines()
content = [x.strip() for x in content]

size = int(content[0])
points = []
for i in range(1, size + 1):
    t = content[i].split()
    city = t[0]
    x = int(t[1])
    y = int(t[2])
    points.append((city, x, y))

t = content[1].split()
city = t[0]
x = int(t[1])
y = int(t[2])
points.append((city, x, y))

print(hill_climb(points))
'''



