def merge_the_tools(string, k):
    result=""
    #creating t's
    for i in range(1,len(string)+1):
        if(i%k == 0):
            sub=list(set(string[0:k]))
            print(result.join(sub))
            string=string[k:]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)