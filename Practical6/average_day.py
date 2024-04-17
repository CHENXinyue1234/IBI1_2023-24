#create a dictionary called average_day
average_day={'sleeping':8,'classes':6,'studying':3.5,'TV':2,'music':1}
# add an entry
average_day['other']=3.5
print(average_day)
time= list(average_day.values())
activity=list(average_day.keys())
# Draw a pie chart
import matplotlib.pyplot as plt


plt.figure()
plt.pie(time, labels = activity,autopct='%1.1f%%')
# show the figure
plt.show()
# close the figure
plt.clf()


#A given activity that can be modified
given_activity= 'studying'
print('given activity :',given_activity)
# print the value of an given activity
print('time used :',average_day[given_activity],'h')