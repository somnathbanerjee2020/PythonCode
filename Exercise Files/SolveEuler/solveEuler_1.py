# problem 1 - https://projecteuler.net/problem=1
upper_limt=1000

sum_of_all=0

for i in range(1,upper_limt,1):
   if i%3 == 0 or i%5 == 0:
       sum_of_all = sum_of_all + i

print(sum_of_all)