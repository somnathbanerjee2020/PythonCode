
status="Valid"
numberOfCards=int(input())
for i in range(1,numberOfCards + 1):
    cardNum = input()
    firstDig=cardNum[:1]
    if(firstDig != "4"):
        status="Invalid" 
        print(status)

print(status)