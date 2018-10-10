import numpy as np
import os
import tsp
import fnmatch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import time
from multiprocessing import Pool

avg_generate = np.zeros((16, 1))
log_avg = np.zeros((16, 1))
time_spent = np.zeros((16,1))

for folder in os.listdir('tsp_problems'):
    if not fnmatch.fnmatch(folder, '.DS_Store') and not fnmatch.fnmatch(folder, 'problem36'):
        print("City count = %s..." % (folder))
        total = 0
        all_instances = []
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

            all_instances.append(points)
            f.close()

        workers = Pool(4)
        results = workers.map(tsp.tsp, all_instances)
        workers.close()
        workers.join()

        print("Finished computing %d instances" % (len(results)))

        total = sum([return_val[2] for return_val in results])
        avg_generate[int(folder)-1] = total / 10
        if total == 0:
            log_avg[int(folder) -1] = 0
        else:
            log_avg[int(folder) -1] = math.log(total/10, 10)
        time_spent[int(folder)-1] = sum([return_val[3] for return_val in results]) / 10.0

plt.title('tsp with heuristic')
plt.ylabel('log of # of nodes')
plt.xlabel('# of cities')
plt.plot(range(1,17), avg_generate)

plt.savefig("tsp_with_heu.png")
np.savetxt('tsp_with_heu.dat', log_avg, "%.6f")
np.savetxt('tsp_with_heu.time', time_spent, "%.3f")
