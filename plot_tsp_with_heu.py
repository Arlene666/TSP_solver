import numpy as np
import os
import tsp
import fnmatch
import matplotlib.pyplot as plt
import math
import time

avg_generate = np.zeros((16, 1))

log_avg = np.zeros((16, 1))

for folder in os.listdir('tsp_problems'):
    print(folder)
    if not fnmatch.fnmatch(folder, '.DS_Store') and not fnmatch.fnmatch(folder, 'problem36'):
        sum = 0
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

            path, weight, generate = tsp.tsp(time.time(), points)
            sum += generate
            f.close()
        avg_generate[int(folder)-1] = sum / 10
        if sum == 0:
            log_avg[int(folder) -1] = 0
        else:
            log_avg[int(folder) -1] = math.log(sum/10)

#print(avg_generate)
plt.title('tsp with heuristic')
plt.ylabel('log of #of nodes')
plt.xlabel('#of cities')
plt.plot(range(1,17), avg_generate)
plt.savefig("tsp_with_heu.png")

#print(log_avg)
#plt.plot(range(16), log_avg)
