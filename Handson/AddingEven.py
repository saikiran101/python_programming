import pandas as pd
import random
import numpy as np
n=int(input("enter number of student"))
data=pd.DataFrame(np.random.randint(40,100,size=(n,3)),columns=["marks1","marks2","marks3"])
df=data.describe()
print(df)
print(data)