import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#这句话不行 os.chdir('\C\MyFiles\IBI\IBI_work\IBI1_2023-24\Practical7')
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")
print(dalys_data.head(5))
dalys_data.info()
print(dalys_data.describe())
print(dalys_data.iloc[0,3]) 
print(dalys_data.iloc[2,0:5])
print(dalys_data.iloc[0:10:2,0:5])
print(dalys_data.iloc[0:3,[0,1,3]])
my_columns = [True, True, False,True]
print(dalys_data.iloc[1:3,my_columns])
print(dalys_data.loc[2:4,"Year"])
print(dalys_data.loc[0:29,"DALYs"])
#会报错 print(dalys_data.iloc[0:29,"DALYs"])
#find every row where the Entity is Afghanistan
Afghanistan_rows = dalys_data.loc[dalys_data['Entity']=='Afghanistan','DALYs']
print(Afghanistan_rows)