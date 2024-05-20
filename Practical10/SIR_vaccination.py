import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
N=10000
Infected=[]
I=1
R=0
rate=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

#set the color
cmap = cm.plasma
norm = Normalize(vmin=0, vmax=1)
#use for loop to go through all the rate
for x in rate:
    I=1
    R=0
    N=N-N*x
    S=int(N-I-R)
    beta=0.3
    gamma=0.05
    Infected=[1]
    time=range(1001)
    if x!=1:
        #use for loop to get infected, recovered
        for i in range(1000):
            additional_R=sum(np.random.choice(range(2),I,p=[1-gamma, gamma]))
            additional_I=sum(np.random.choice(range(2),S,p=[1-beta*I/N,beta*I/N]))
            R=R+additional_R
            I=I-additional_R+additional_I
            S=int(N-I-R)
            Infected.append(I)
        plt.plot(time, Infected,label=str(int(x*100))+'%',color=cmap(norm(x)))
    else:
        for i in range(1000):
            additional_R=sum(np.random.choice(range(2),I,p=[1-gamma, gamma]))
            additional_I=0
            R=R+additional_R
            I=I-additional_R+additional_I
            S=int(N-I-R)
            Infected.append(I)
        plt.plot(time, Infected,'y',label=str(int(x*100))+'%')
#draw the figure
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model with different vaccination rate',fontsize=15)
plt.legend()
plt.show()
plt.clf()


    


    


