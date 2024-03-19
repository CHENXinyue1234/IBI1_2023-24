# city_sizes={'Edinburgh':0.56,'Glasgow':0.62,'Stirling':0.04,'London':9.7,'Haining':0.58,'Hangzhou':8.4,'Shanghai':29.9,'Beijing':22.2}
uk_cities=[0.56,0.62,0.04,9.7] # A list for populations of uk cities
China_cities=[0.58,8.4,29.9,22.2] # A list for populations of China cities
uk_cities.sort() #sort the data of uk cities
print('uk_cities',uk_cities)
China_cities.sort()#sort the data for China cities
print('China_cities',China_cities)

#Draw a bar graph for uk cities
import matplotlib.pyplot as plt #import matplotlib
city_names=['Stirling','Edinburgh','Glasgow','London'] #list the cities to which the population corresponds
width = 0.8 #set the width
plt.figure() #create a new figure
plt.bar(city_names,uk_cities, width,color='g')#create a bar graph and set the color green
for i in range(len(city_names)):
    plt.text(i,uk_cities[i],str(uk_cities[i]),ha='center',va='bottom')#display the value of each column
plt.ylabel("Population(millions)")#set y labels
plt.title("UK cities",fontsize=20)#set a title
plt.xticks(city_names, ('Stirling','Edinburgh','Glasgow','London'))#set x labels
plt.show()#show the figure
plt.clf() #close the figure

#Draw a bar graph for China cities
city_names=['Haining','Hangzhou','Beijing','Shanghai']
width = 0.8
plt.figure()
plt.bar(city_names,China_cities, width,color='b')#create a bar graph and set the color blue
for i in range(len(city_names)):
    plt.text(i,China_cities[i],str(China_cities[i]),ha='center',va='bottom')
plt.ylabel("Population(millions)")
plt.title("China cities",fontsize=20)
plt.xticks(city_names, ('Haining','Hangzhou','Beijing','Shanghai'))
plt.show()
plt.clf() 
