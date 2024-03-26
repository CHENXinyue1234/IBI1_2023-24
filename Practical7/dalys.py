import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#这句话不行 os.chdir('\C\MyFiles\IBI\IBI_work\IBI1_2023-24\Practical7')
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")
#show the fourth column (the DALYs) from every 10th row
print(dalys_data.iloc[0:101:10,3])
#find every row where the Entity is Afghanistan
Afghanistan_rows = dalys_data.loc[dalys_data['Entity']=='Afghanistan','DALYs']
print(Afghanistan_rows)
China_rows = dalys_data.loc[dalys_data['Entity']=='China',[True, False, True, True]]
print(China_rows)
China_mean=np.mean(China_rows['DALYs'])
China_2019=China_rows.loc[China_rows['Year'] == 2019,'DALYs']
print('China_mean:',China_mean)
print('China_2019:',China_2019.iloc[0])
#whether the DALYs in China in 2019 was greater or less than the mean
if (China_mean >= China_2019.iloc[0]).any():
    print('2019 was below the mean')
else:
    print('2019 was above the mean')
plt.plot(China_rows.Year, China_rows.DALYs, 'g-')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('The DALYs in China from 1990 to 2019',fontsize=15)
plt.xticks(China_rows.Year,rotation=-45,fontsize=7)
plt.show()

#Are there places in the World where the DALYs in 2019 is less than 18,000? If so, where are they?
Year2019_rows = dalys_data.loc[dalys_data['Year']==2019]
Selected_Year2019_Dalys = Year2019_rows.loc[Year2019_rows['DALYs'] < 18000,'Entity']
print('Places in the World where the DALYs in 2019 is less than 18,000:')
print(Selected_Year2019_Dalys.to_string(index=False))