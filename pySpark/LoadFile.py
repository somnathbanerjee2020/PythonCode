# import pySpark as ps
# pandas is a dataframe library

#import numpy
import pandas as pd
import os

# creating a pandas dataframe using a test csv
os.chdir("c:/Users/banerso/Documents/GitHub/PythonCode/pySpark/")

f=open("fifa18.csv","r")
data=pd.read_csv("fifa18.csv")
# First x rows
print(data.head(30))
# k=data.tail()
# print(k)

# Metadata of the frame
print(data.shape)
