import numpy as np 
import matplotlib.pyplot as plt
#initialize
N=10000
Infected=[]
Susceptible=[]
Recovered=[]
I=1
S=9999
R=0
beta=0.3
gamma=0.05
Recovered.append(0)
Infected.append(1)
Susceptible.append(9999)
#use for loop to get recovered, infected
for i in range(1000):
    additional_R=sum(np.random.choice(range(2),I,p=[1-gamma, gamma]))
    additional_I=sum(np.random.choice(range(2),S,p=[1-beta*I/N,beta*I/N]))
    R=R+additional_R
    I=I-additional_R+additional_I
    S=S-additional_I
    Recovered.append(R)
    Infected.append(I)
    Susceptible.append(S)


#Draw the figure
time=range(1001)
plt.figure ( figsize =(6 ,4) , dpi=150) 
plt.plot(time, Recovered, 'g',label='Recovered')
plt.plot(time, Infected, 'r',label='Infected')
plt.plot(time, Susceptible,'b', label='Susceptible')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model',fontsize=15)
plt.legend()
plt.savefig('SIR_figure')
plt.show()
plt.clf()



