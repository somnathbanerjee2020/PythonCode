import pickle

l1=[1,2,3,4,5]

f=open('datafile.txt','wb')

pickle.dump(l1,f)

f.close