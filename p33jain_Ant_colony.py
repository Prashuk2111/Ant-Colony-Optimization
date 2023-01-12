import random 
import math
from matplotlib import pyplot as plt
import numpy as np
# from matplotlib import pyplot as plt


def ant_colony(Pheremones_table, Distance_table, ants_population):

    Pheremones = Pheremones_table[:]
    Distances = Distance_table[:]

    iter = 0
    alpha = 1
    Beta = 1
    evaporation = 0.1
    # Q is the contant value being added for diffusion
    Q = 1

    global_optimum = [0.0,0.0]
    average_distance = []
    best_distance = []
    minimum_distance = 10000000
    iterations =[]

    while (iter < 100):


        All_paths_cost = []

        for i in range(ants_population):
            Path_left = [i for i in range(29)]

            Intial_postion = random.randint(0,28)
            Path_Traveled = []
            Path_left.remove(Intial_postion)
            Path_Traveled.append(Intial_postion)

            while(len(Path_left) > 0):

                total_probablity = 0
                list_probablity = []

                # Calculating the best path for each ant node by node
                for index in Path_left:
                    a = min(Intial_postion,index)
                    b = max (Intial_postion,index)
                    indiviual_problity = math.pow(Pheremones[a,b],alpha)/math.pow(Distances[a,b],Beta)
                    list_probablity.append(indiviual_problity)
                    total_probablity = total_probablity + indiviual_problity

                list_probablity = np.array(list_probablity, dtype=float)
                list_probablity_1 = list(list_probablity/total_probablity)
        
                max_1 = max(list_probablity_1)
                index = Path_left[list_probablity_1.index(max_1)]
                Path_left.remove(index)
                Intial_postion = index
                Path_Traveled.append(Intial_postion)
            
            # list that stores path travelled by an ant
            All_paths_cost.append([i,Path_Traveled])
        
        distance_avg = 0

        # Calculating the cost of all the paths travelled in one iteration

        for val in All_paths_cost:
            temp_path = val[1]
            min_distance = 0

            for i in range(len(temp_path)-1):
                a = min(temp_path[i],temp_path[i+1])
                b = max(temp_path[i],temp_path[i+1])
                min_distance = min_distance + Distances[a,b]
                distance_avg = distance_avg + Distances[a,b]

            for i in range(len(temp_path)-1):
                a = min(temp_path[i],temp_path[i+1])
                b = max(temp_path[i],temp_path[i+1])

                Pheremones[a,b] = (1- evaporation)*Pheremones[a,b] + Q/min_distance

            #  Storing global minimum
            if min_distance < minimum_distance:
                minimum_distance = min_distance
                best_path = temp_path
                global_optimum[0] = minimum_distance
                global_optimum[1] = best_path
        
        average_distance.append(distance_avg/Ants_population)
        best_distance.append(minimum_distance)
        iterations.append(iter)
        iter = iter+1
    

    print(global_optimum)

    fig, [ax1,ax2] = plt.subplots(2)
    ax1.plot( iterations,average_distance)
    ax1.set_title("average_fitness")
    ax2.plot(iterations,best_distance)
    ax2.set_title("best_fitness")
    plt.show()


if __name__ =='__main__':

    Intial_pheremones_val = 0.02
    Ants_population = 100

    City_cordinates = [[1,1150,1760],
                        [2,630,1660],  
                        [3,40,2090],
                        [4,750,1100],
                        [5,750,2030],
                        [6,1030,2070],
                        [7,1650,650],
                        [8,1490,1630],
                        [9,790,2260],
                        [10,710,1310],
                        [11,840,550],
                        [12,1170,2300],
                        [13,970,1340],
                        [14,510,700],
                        [15,750,900],
                        [16,1280,1200],
                        [17,230,590],
                        [18,460,860],
                        [19,1040,950],
                        [20,590,1390],
                        [21,830,1770],
                        [22,490,500],
                        [23,1840,1240],
                        [24,1260,1500],
                        [25,1280,790],
                        [26,490,2130],
                        [27,1460,1420],
                        [28,1260,1910],
                        [29,360,1980]]


    Distance_matrix = np.zeros((29,29), dtype=float)
    Pheromones_matrix = np.zeros((29,29), dtype=float)
    Pheromones_matrix = Pheromones_matrix + Intial_pheremones_val

    for i in range(len(City_cordinates)-1):
        for j in range(i+1,len(City_cordinates)):
            Distance_matrix[i,j] = math.sqrt(pow(City_cordinates[i][1] - City_cordinates[j][1],2) + pow(City_cordinates[i][2] - City_cordinates[j][2],2))

    ant_colony(Pheromones_matrix,Distance_matrix,Ants_population)

                   