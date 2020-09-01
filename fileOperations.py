myfile=open('fifa18.csv')
k=myfile.readlines()
print(k)
myfile.seek(0)
w=myfile.read()

print(f"w is {w}")