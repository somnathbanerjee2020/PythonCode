#10. https://projecteuler.net/problem=10

def check_prime(checkThis):
    for i in range(2,checkThis):
        if checkThis % i == 0:
            return False
        i+= 1
    return True

sum_primes=0
for i in range(1000000,1100000):
    if check_prime(i):
        #print(i)
        sum_primes += i

print(sum_primes)

#454396537
#9459839658
#8996050117
#18640115711


