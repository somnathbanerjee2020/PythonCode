# 4. https://projecteuler.net/problem=4

def checkPalindrome(num):
    rev=0
    temp=num
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        return(1)
    else:
        return(0)

if __name__ == "__main__":
    first_num=999
    second_num=999
    for i in range(1,999):
        first_num -= i
        second_num -= (i-1)
        product=first_num*second_num
        #checkFirst
        w=checkPalindrome(product)
        if w == 1:
            print(f'{product} is a palindrome')
        else:
            #check again

