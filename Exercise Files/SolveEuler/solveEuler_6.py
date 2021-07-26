#6. https://projecteuler.net/problem=6

workList = range(1,101)

sum_of_squares = 0

square_of_sum = 0

sum_of_sum = 0

for i in workList:
    sum_of_sum += i
    sum_of_squares = sum_of_squares + i**2

square_of_sum = sum_of_sum ** 2

diff= square_of_sum -  sum_of_squares

print(diff)
