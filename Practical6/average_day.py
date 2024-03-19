#create a dictionary called average_day
average_day={'sleeping':8,'classes':6,'studying':3.5,'TV':2,'music':1}
# add an entry
average_day['other']=3.5
print(average_day)

# Draw a pie chart
import matplotlib.pyplot as plt
# create lables
activity_labels = ['sleeping','classes','studying','TV','music','other']
# time used for an activity
time_used = [8,6,3.5,2,1,3.5]
plt.figure()
plt.pie(time_used, labels = activity_labels)
# show the figure
plt.show()
# close the figure
plt.clf()

import random
# Randomly select an activity
random_key = random.choice(list(average_day))
print('given activity :',random_key)
# print the value of an given activity
print('time used :',average_day[random_key],'h')