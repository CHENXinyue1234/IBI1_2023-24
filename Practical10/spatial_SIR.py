import numpy as np 
import matplotlib . pyplot as plt
from matplotlib.colors import ListedColormap

colors = ['indigo', 'cyan', 'yellow']  # dark-purple =susceptible, blue-green=infected, yellow=recovered 
custom_cmap = ListedColormap(colors)
population = np.zeros((100, 100)) 
# randomly select an outbreak point
outbreak=np.random.choice(range(100) ,2)
print(outbreak)
# 0=susceptible, 1=infected, 2=recovered, the outbreak point is infected, so the value=1
population[outbreak[0], outbreak[1]] = 1
#draw the first point
plt.figure(figsize =(6,4) , dpi=150) 
plt.imshow(population , cmap=custom_cmap, interpolation='nearest')
plt.show()
#set beta and gamma
beta=0.3
gamma=0.05

#loop through 100 time points
for k in range(100):
    # find points that are infected 
    infectedIndex = np.where(population==1)
    # infecting its neighbours
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        #if the neighbour is susceptible
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    # recover
    for i in range(population.shape[0]):
        for j in range(population.shape[1]):
            if population[i, j] == 1:
                population[i,j]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0]
    #output a graph every 10 cycles
    if k % 10 == 0:
        plt.imshow(population , cmap=custom_cmap, interpolation='nearest')
        plt.show()