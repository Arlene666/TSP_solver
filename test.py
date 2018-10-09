import numpy as np
import os
#import tsp_noheu
import fnmatch
import matplotlib.pyplot as plt

import math

avg_generate = np.zeros((8, 1))

nomatch = ['.DS_Store', 'problem36', '16', '15', '14', '13', '12', '11', '10', '9']

'''for folder in os.listdir('tsp_problems'):
    if not str(folder) in nomatch:
        print(folder)



for myfile in os.listdir('tsp_problems/8'):
    f = open(os.path.join('tsp_problems/8', myfile))
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

    path, weight, generate = tsp_noheu.tsp_noheu(points)
    f.close()
    print(generate)
'''
x = math.log(10/10)
print(x)

math.