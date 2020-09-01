# problem 2 - https://projecteuler.net/problem=3

def checkPrime(l):
    j=l
    #print(f'Inside Checkprime. Checking: ',j)
    for c in range(1,j):
        if j%c == 0:
            print(f'Is not a prime',j)
            break
    
    return(j)

if __name__ == "__main__":
    k=0
    for i in range(1,100):
        k=checkPrime(i)
        #if k != 0:
         #   print(k)
