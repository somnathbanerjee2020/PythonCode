#7. https://projecteuler.net/problem=7

def check_prime(checkThis):
    for i in range(2,checkThis):
        if checkThis % i == 0:
            return False
        i+= 1
    return True


start_from = 2
counter=0


while True:
    if check_prime(start_from):
        counter += 1

    if counter == 10001:
        break

    start_from += 1
print(start_from)
