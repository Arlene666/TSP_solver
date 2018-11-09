import tsp_ls_sdmove
import tsp_search
import os
import fnmatch
import csv

avg_quality = []
avg_steps = []
avg_percentage = []


# calculate average quality, steps, percentage for city 14 -- 16
dir = sorted(os.listdir('tsp_problems'))
for folder in dir:
    if not fnmatch.fnmatch(folder, '.DS_Store') and not fnmatch.fnmatch(folder, '36'):
        #total_cost = 0
       # total_steps = 0\
        avg_qual = []
        avg_step = []
        avg_percen = []
        subdir = sorted(os.listdir(os.path.join('tsp_problems', folder)))
        for myfile in subdir:
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
            t = content[1].split()
            city = t[0]
            x = int(t[1])
            y = int(t[2])
            points.append((city, x, y))

            path_search, cost_search, num_gen, time = tsp_search.tsp(points)
            print("A* search cost: ", cost_search)
            quality = 0
            steps = 0
            count = 0
            for i in range(100):
                path, cost, step = tsp_ls_sdmove.hill_climb(points, 100)
                print("local search cost: ", cost)
                qual = cost/cost_search
                quality += qual
                if qual <= 1:
                    #print("qual <= 1")
                    #print(qual)
                    count += 1
                steps += step

            quality = quality / 100.0
            steps = steps/100
            percen = count/100.0
            avg_qual.append(quality)
            avg_step.append(steps)
            avg_percen.append(percen)
        avg_quality.append(avg_qual)
        avg_steps.append(avg_step)
        avg_percentage.append(avg_percen)


qual_avg = [sum(x)/10 for x in avg_quality]
steps_avg = [sum(x)/10 for x in avg_steps]
percen_avg = [sum(x)/10 for x in avg_percentage]

with open('q104_sdmove_quality.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["num_cities", "instance_1", "instance_2", "instance_3", "instance_4", "instance_5",
                     "instance_6", "instance_7", "instance_8", "instance_9", "instance_10", "average"])
    for i in range(len(avg_quality)):
        writer.writerow([i+14] + avg_quality[i] + [qual_avg[i]])
        #else:
         #   writer.writerow([36] + avg_quality[i] + qual_avg[i])

with open('q104_sdmove_steps.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["num_cities", "instance_1", "instance_2", "instance_3", "instance_4", "instance_5",
                     "instance_6", "instance_7", "instance_8", "instance_9", "instance_10", "average"])
    for i in range(len(avg_steps)):
        writer.writerow([i+14] + avg_steps[i] + [steps_avg[i]])
        #else:
         #   writer.writerow([36] + avg_steps[i] + steps_avg[i])


with open('q104_sdmove_percentage.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["num_cities", "instance_1", "instance_2", "instance_3", "instance_4", "instance_5",
                     "instance_6", "instance_7", "instance_8", "instance_9", "instance_10", "average"])
    for i in range(len(avg_percentage)):
        writer.writerow([i+14] + avg_percentage[i] + [percen_avg[i]])
       # else:
        #    writer.writerow([36] + avg_percentage[i] + percen_avg[i])


'''#compute avg quality, steps, and percentage for 36-city problem
cost_other = 462.76093083911462145
f = open('tsp_problems/36/instance_1.txt')

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

quality_36 = 0
steps_36 = 0
count_36 = 0
for i in range(100):
    path_36, cost_36, step_36 = tsp_ls.hill_climb(points)
    qual_36 = cost_36 / cost_other
    quality_36 += qual_36
    if qual_36 <= 1:
        # print("qual <= 1")
        # print(qual)
        count_36 += 1
    steps_36 += step_36

quality_36 = quality_36 / 100.0
steps_36 = steps_36 / 100
percen_36 = count_36 / 100.0
'''

print("sideway move (100) percentage of finding best solutions: ")
print(avg_percentage)
print("sideway move (100) average steps to reach local minimum: ")
print(avg_steps)
print("sideway move (100) average quality of local search solutions: ")
print(avg_quality)
print("sideway move (100) average percentage of finding best solutions over 10 instances: ")
print(percen_avg)
print("sideway move (100) average steps to reach local minimum over 10 instances: ")
print(steps_avg)
print("sideway move (100) average quality of local search solutions over 10 10 instances: ")
print(qual_avg)
'''print("average quality of local search solution on 36-city problem: ")
print(quality_36)
print("average steps to reach local minimum on 36-city problem: ")
print(steps_36)
print("percentage of finding the best solution on 36-city problem: ")
print(percen_36)
'''