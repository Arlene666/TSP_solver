import numpy as np
import os
import tsp_noheu
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

nomatch = ['.DS_Store', 'problem36', '16', '15']

for folder in os.listdir('tsp_problems'):
    if not str(folder) in nomatch:
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
        results = workers.map(tsp_noheu.tsp_noheu, all_instances)
        workers.close()
        workers.join()

        print("Finished computing %d instances" % (len(results)))

        total = sum([return_val[2] for return_val in results])
        avg_generate[int(folder)-1] = total / 10.0
        if total == 0:
            log_avg[int(folder) -1] = 0
        else:
            log_avg[int(folder) -1] = math.log(total/10, 10)
        time_spent[int(folder)-1] = sum([return_val[3] for return_val in results]) / 10.0

plt.title('TSP without heuristic')
plt.ylabel('log of # of nodes generated')
plt.xlabel('# of cities')
plt.plot(range(1, 17), log_avg)

plt.savefig('tsp_no_neu.png')
np.savetxt('tsp_no_neu.dat', log_avg, "%.6f")
np.savetxt('tsp_no_neu.time', time_spent, "%.3f")

