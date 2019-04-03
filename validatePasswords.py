# Enter your code here. Read input from STDIN. Print output to STDOUT

k=int(input())
#print(k)
for i in range(1,k+1):
    j=input()
    #convert into a set and then a list
    testSetList=list(set(j))
    #Split j into a list
    testList = list(j)
    upperCt=0 
    numCt=0
    testFlag="Valid"
    #Length Check
    if(len(testList) != 10 or len(testSetList) < len(testList)):
        testFlag = "Invalid"
    

    for i in testList:
        asciiValue=ord(i)
        if(asciiValue >= 65 and asciiValue <=90):
            upperCt +=1
        if(asciiValue >= 48 and asciiValue <=57):
            numCt +=1
        if(asciiValue > 122 or asciiValue < 48 or (asciiValue >= 58 and asciiValue <= 64) or  (asciiValue >= 91 and asciiValue <= 96)):
         testFlag ="Invalid"
         continue   

    #Uppercase Check    
    if(upperCt < 2):
        testFlag ="Invalid"
    
    #Number Check
    if(numCt < 3):
        testFlag ="Invalid"

    
    print(testFlag)
