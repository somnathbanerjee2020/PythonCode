# 4. https://projecteuler.net/problem=4

import string

def checkPalindrome(num):
    n1=list(str(num))
    n2=n1[::-1]
    if n1 == n2:
        return True
    else:
        return False


if __name__ == "__main__":
    #start with largest 3 digit numbers and moving down
    f1=999
    f2=999
    f3=f2
    out=0
    all_dromes = []

    while f1 >= 100:
        f2=f3
        product=f1*f2
        if checkPalindrome(product):
            print(product)
            all_dromes.append(product)
            break
        else:
            while f2 >=100:
                product=f1*f2
                if checkPalindrome(product):
                    #print(product)
                    #out=1
                    all_dromes.append(product)
                    #break
                f2 -= 1        
        #if out ==1:
        #    break
        f1 -= 1
    #print(f1)
    #print(f2)
    all_dromes.sort()
    print(all_dromes)

