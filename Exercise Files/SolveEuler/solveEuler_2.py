# problem 2 - https://projecteuler.net/problem=2
upper_limt=4000000

first=1
second=2
carry=0
sum=2

for i in range(1,upper_limt,1):
   if first < upper_limt:
       first = first + second
       #print(f'First=',first)
       carry = second
       second = first
       if first %2 == 0:
           sum=sum+first
       first = carry
       #print(f'sum=',sum)

print(f'sum=',sum)



