import tsp_ls_simulated_annealing
import tsp_search
import os
import fnmatch
import csv
import matplotlib.pyplot as plt


avg_quality_exp = []
avg_quality_log = []
avg_quality_linear = []
#avg_steps = []
#avg_percentage = []

avg_time_exp = []
avg_time_log = []
avg_time_linear = []

global_opt = [316.6776082168322, 324.3082534116089, 315.07667336786403,
              316.13786124656355, 404.4585854022553, 354.55691319058866]

file_count = 0

# calculate average quality, steps, percentage for city 14 -- 16
dir = sorted(os.listdir('first_two_instances'))
for folder in dir:
    if not fnmatch.fnmatch(folder, '.DS_Store') and not fnmatch.fnmatch(folder, '36'):
        #total_cost = 0
       # total_steps = 0\
        #avg_qual = []
        #avg_step = []
        #avg_percen = []
        subdir = sorted(os.listdir(os.path.join('first_two_instances', folder)))
        for myfile in subdir:
            print(file_count)

            f = open(os.path.join('first_two_instances', folder, myfile))
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

          #  path_search, cost_search, num_gen, time = tsp_search.tsp(points)
            cost_search = global_opt[file_count]
            file_count += 1
       #     print("A* search cost: ", cost_search)

            #steps = 0  # sum of steps to reach local optimum in 100 rounds
            #count = 0 # count of the times that hitting global optimum in 100 rounds
            #qual_arr = []
            #time_arr = []
            #for i in range(50):
            quality = 0  # sum of the qualities over 100 rounds
            execution = 0  # sum of execution time over 100 rounds
            for j in range(100):
                path, cost, execute = tsp_ls_simulated_annealing.simu_exp(points)

                # print("local search cost: ", cost)
                qual = cost / cost_search
                quality += qual
                execution += execute
                # if qual <= 1:
                # print("qual <= 1")
                # print(qual)
                # count += 1
                # steps += step
            quality = quality / 100.0
            execution = execution / 100.0
           # print(quality)
           # print(execution)
            avg_quality_exp.append(quality)
            avg_time_exp.append(execution)


            quality = 0  # sum of the qualities over 100 rounds
            execution = 0  # sum of execution time over 100 rounds
            for j in range(100):
                path, cost, execute = tsp_ls_simulated_annealing.simu_log(points)

                # print("local search cost: ", cost)
                qual = cost / cost_search
                quality += qual
                execution += execute
                # if qual <= 1:
                # print("qual <= 1")
                # print(qual)
                # count += 1
                # steps += step
            quality = quality / 100.0
            execution = execution / 100.0
            # print(quality)
            # print(execution)
            avg_quality_log.append(quality)
            avg_time_log.append(execution)

            quality = 0  # sum of the qualities over 100 rounds
            execution = 0  # sum of execution time over 100 rounds
            for j in range(100):
                path, cost, execute = tsp_ls_simulated_annealing.simu_linear(points)

                # print("local search cost: ", cost)
                qual = cost / cost_search
                quality += qual
                execution += execute
                # if qual <= 1:
                # print("qual <= 1")
                # print(qual)
                # count += 1
                # steps += step
            quality = quality / 100.0
            execution = execution / 100.0
            # print(quality)
            # print(execution)
            avg_quality_linear.append(quality)
            avg_time_linear.append(execution)





'''for j in range(6):
    for i in range(50):
        if avg_quality[j][i] <= 1.01:
            print("#of restarts that ensures within 1% of the best solution for "+str(j/2 +14) +"-city instance "
                  +str(j%2+1))
            print(i)
'''

for i in range(6):
    x = [1, 2, 3]
    y = [avg_quality_exp[i], avg_quality_log[i], avg_quality_linear[i]]
    plt.figure(i)
    plt.plot(x, y)
    plt.xlabel("different annealing schedules (exp, log, linear)")
    plt.ylabel('average quality over 100 rounds')
    plt.title(str(i / 2 + 14) + "-city instance " + str(i % 2 + 1) +" quality")
    plt.savefig("simu_" + str(i / 2 + 14) + "_city_instance_" + str(i % 2 + 1) + "_quality.png")

for i in range(6):
    x = [1, 2, 3]
    y = [avg_time_exp[i], avg_time_log[i], avg_time_linear[i]]
    plt.figure(i+6)
    plt.plot(x, y)
    plt.xlabel("different annealing schedules (exp, log, linear)")
    plt.ylabel('average execution time over 100 rounds')
    plt.title(str(i/2 + 14) + "-city instance " + str(i % 2 + 1) + " time")
    plt.savefig("simu_" + str(i/2 + 14) + "_city_instance_" + str(i % 2 + 1) + "_time.png")


'''for i in range(6):
    plt.plot(range(50), avg_quality[i])
    plt.xlabel("#of random starts")
    plt.ylabel("average quality over 100 rounds")
    plt.title(str(i/2+14) + "-city instance "+str(i%2+1))
    plt.savefig(str(i/2+14) + "_city_instance_"+str(i%2+1) + "_quality.png")

for i in range(6):
    plt.plot(range(50), avg_time[i])
    plt.xlabel("#of random starts")
    plt.ylabel("average execution time over 100 rounds")
    plt.title(str(i/2+14) + "-city instance "+str(i%2+1))
    plt.savefig(str(i/2+14) + "_city_instance_"+str(i%2+1) + "_time.png")
'''