import numpy as np
import os
import time
import math
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from heapq import heappush, heappop

f = open('tsp_problems/10/instance_1.txt')
content = f.readlines()
content = [x.strip() for x in content]

size = int(content[0])
info = []
for i in range(1, size+1):
    t = content[i].split()
    city = t[0]
    x = int(t[1])
    y = int(t[2])
    info.append((city, x, y))



def distance(pointA, pointB):
    #print(pointA, pointB)
    x_diff = pointA[1] - pointB[1]
    y_diff = pointA[2] - pointB[2]
    result = pow(x_diff, 2) + pow(y_diff, 2)
    result = math.sqrt(result)
    return result

def min_dist(a, points):
    size = len(points)
    if size == 0:
        return 0
    min_d = float('inf')
    #point = a
    for i in range(size):
        dist = distance(a, points[i])
        if dist < min_d:
            min_d = dist
          #  point = points[i]
    return min_d


'''def adj_mat(points):
    size = len(points)
    mat = np.zeros((size, size))
    if size <= 1:
        return [0]
    for i in range(0, size-1):
        for j in range(i+1, size):
            dist = distance(points[i], points[j])
            mat[i][j] = dist
    return mat


def mst_weight(adj):
    if len(adj) <= 1:
        return 0
    X = csr_matrix(adj)
    Tcsr = minimum_spanning_tree(X)
    return np.sum(Tcsr)
'''
#print(adj_mat(info))


def pathlen(points):
    size = len(points)
    if size <= 1:
        return 0
    plen = 0
    for i in range(size-1):
        plen += distance(points[i], points[i+1])
    return plen


def tsp_noheu(points):
    global num_generate
    num_generate = 0
    if len(points) == 1:
        return points, 0, 0

    def tsp_search(points):
        left = [points[0]]
        right = points[1:]
        # print(right)
        curr = left[len(left)-1]
        g = pathlen(left)
        h = 0
        f = g+h
        frontier = []
        heappush(frontier, (f, (left, right)))
        while frontier:
            node = heappop(frontier)
            left = node[1][0]
            right = node[1][1]
            if len(left) == len(points):
                left.append(points[0])
                plen = pathlen(left)
                return left, plen, num_generate
            else:
                size = len(right)
                for i in range(size):
                    curr = left[len(left)-1]
                    newleft = left + [right[i]]
                    newright = right[:]
                    del newright[i]
                    g = pathlen(newleft)
                    h = 0
                    f = g+h
                    global num_generate
                    num_generate += 1
                    heappush(frontier, (f, (newleft, newright)))
    return tsp_search(points)


start_time = time.time()

print(tsp_noheu(info))
print("--- %s seconds ---" % (time.time() - start_time))
