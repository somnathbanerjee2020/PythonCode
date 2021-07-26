#5. https://projecteuler.net/problem=5
checkList = list(range(1,21))
#print(checkList)

def check_if_div(checkthis):
    for i in checkList:
        if checkthis % i == 0:
            continue
        else:
            return False
    return True
    
checker=2520
while True:
    if check_if_div(checker):
        break
    else:
        checker += 1

print(checker)