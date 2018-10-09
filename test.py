import numpy as np
import os
import tsp_noheu
import fnmatch
import matplotlib.pyplot as plt
import time
import math

avg_generate = np.zeros((10, 1))

nomatch = ['.DS_Store', 'problem36', '16', '15', '14', '13', '12', '11', '10', '9']

'''for folder in os.listdir('tsp_problems'):
    if not str(folder) in nomatch:
        print(folder)
'''

count = 0
for myfile in os.listdir('tsp_problems/14'):
    f = open(os.path.join('tsp_problems/14', myfile))
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

    path, weight, generate = tsp_noheu.tsp_noheu(time.time(), points)
    f.close()
    avg_generate[count] = generate
    count += 1

    print(generate)

plt.title('tsp with heuristic')
plt.ylabel('log of #of nodes')
plt.xlabel('#of cities')
plt.plot(range(1,11), avg_generate)
plt.savefig("test.png")

