import numpy as np
import os
import tsp_noheu
import fnmatch
import matplotlib.pyplot as plt
import math
import time

avg_generate = np.zeros((14, 1))
log_avg = np.zeros((14, 1))

nomatch = ['.DS_Store', 'problem36', '16', '15']

for folder in os.listdir('tsp_problems'):
    print(folder)
    if not str(folder) in nomatch:
        total = 0
        for myfile in os.listdir(os.path.join('tsp_problems', folder)):
            f = open(os.path.join('tsp_problems', folder, myfile))
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
            total += generate
            f.close()
        avg_generate[int(folder)-1] = total / 10.0
        if total == 0:
            log_avg[int(folder) -1] = 0
        else:
            log_avg[int(folder) -1] = math.log(total/10, 10)

plt.title('TSP without heuristic')
plt.ylabel('log of #of nodes generated')
plt.xlabel('#of cities')
plt.plot(range(1, 15), log_avg)
plt.savefig("tsp_no_neu.png")

print(log_avg)
