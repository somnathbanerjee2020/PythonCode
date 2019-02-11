# import pySpark as ps
# pandas is a dataframe library

import numpy as np
import pandas as pd
import os

#convert list to DF
#l1={1,2,3,4,5,6}
#df1=pd.DataFrame([l1])
#print(df1)

# creating a pandas dataframe using a test csv
os.chdir("c:/Users/banerso/Documents/GitHub/PythonCode/pySpark/")
f=open("fifa18.csv","r")
data=pd.read_csv("fifa18.csv")
# First x rows
sample=data.head(30)

#Filtering based on a column
print(sample[sample["Age"] > 30])

# Metadata of the frame
#print(data.shape)




