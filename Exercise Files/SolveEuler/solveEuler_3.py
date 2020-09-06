# problem 3 - https://projecteuler.net/problem=3

def findPrimeFactors(w):
    for a in range(2,w):
        if w%a == 0:
            #print(f"{a} is a factor of {w}. Lets check if {a} is a prime")
            k=checkPrime(a)
            if k==1:
                print(f'{a} is a prime factor of {w}')



def checkPrime(l):
    for c in range(2,l):
        if l%c == 0:
            return(0)
    return(1)
    
    
if __name__ == "__main__":
    #k=checkPrime(24)
    #print(k)
    findPrimeFactors(600851475143)
