import tsp_ls_randstart
import tsp_search
import os
import fnmatch
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from multiprocessing import Pool
from timeit import default_timer as timer

avg_quality = []
avg_time = []

# Global optimal answer from Piazza
global_opt = [316.6776082168322, 324.3082534116089, 315.07667336786403,
              316.13786124656355, 404.4585854022553, 354.55691319058866]
num_randstart = 45

file_count = 0
exclude_dir = ['.DS_Store', '36']
# calculate average quality, steps, percentage for city 14 -- 16
dir = sorted(os.listdir('first_two_instances'))
for folder in dir:
    if not folder in exclude_dir:
        subdir = sorted(os.listdir(os.path.join('first_two_instances', folder)))
        for myfile in subdir:
            fname = os.path.join('first_two_instances', folder, myfile)
            print('Working on %s...' % (fname))
            f = open(fname)
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

            #path_search, cost_search, num_gen, time = tsp_search.tsp(points)
            #print("A* search cost: ", cost_search)
            cost_search = global_opt[file_count]
            file_count += 1

            #steps = 0  # sum of steps to reach local optimum in 100 rounds
            #count = 0 # count of the times that hitting global optimum in 100 rounds
            qual_arr = []
            time_arr = []
            all_runs = []
            for i in range(num_randstart):
                quality = 0  # sum of the qualities over 100 rounds
                execution = 0 # sum of execution time over 100 rounds
                #startTime = timer()
                for j in range(100):
                    all_runs.append((points, i))
                    #path, cost, step, execute = tsp_ls_randstart.hill_climb(points, i)
                    ##print("local search cost: ", cost)
                    #qual = cost / cost_search
                    #quality += qual
                    #execution += execute
                    #if qual <= 1:
                        # print("qual <= 1")
                        # print(qual)
                        #count += 1
                    #steps += step
                #endTime = timer()
                #print('100 randstart took %.2f seconds' % (endTime-startTime))
                #quality = quality / 100.0
                #execution = execution / 100.0
                #print(quality)
                #print(execution)
                #qual_arr.append(quality)
                #time_arr.append(execution)

            workers = Pool()
            results = workers.map(tsp_ls_randstart.hill_climb, all_runs)
            workers.close()
            workers.join()

            for i in range(100, (num_randstart+1)*100, 100):
                qual_arr.append(sum([r[1]/cost_search for r in results[i-100:i]]) / 100.0)
                time_arr.append(sum([r[3] for r in results[i-100:i]]) / 100.0)
            
            avg_quality.append(qual_arr)
            avg_time.append(time_arr)





for j in range(6):
    for i in range(num_randstart):
        if avg_quality[j][i] <= 1.01:
            print("# of restarts that ensures within 1% of the best solution for "
                    + str(j/2 +14) +"-city instance " + str(j%2+1))
            print(i)
            break

for i in range(6):
    plt.figure(i)
    plt.plot(range(1, num_randstart+1), avg_quality[i])
    plt.xlabel("#of random starts")
    plt.ylabel("average quality over 100 rounds")
    plt.title(str(i/2+14) + "-city instance "+str(i%2+1))
    plt.savefig(str(i/2+14) + "_city_instance_"+str(i%2+1) + "_quality.png")

for i in range(6):
    plt.figure(i+6)
    plt.plot(range(1, num_randstart+1), avg_time[i])
    plt.xlabel("#of random starts")
    plt.ylabel("average execution time over 100 rounds")
    plt.title(str(i/2+14) + "-city instance "+str(i%2+1))
    plt.savefig(str(i/2+14) + "_city_instance_"+str(i%2+1) + "_time.png")
