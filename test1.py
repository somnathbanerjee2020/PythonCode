def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

def merge_the_tools(string, k):
    result=""
    #creating t's
    for i in range(1,len(string)+1):
        if(i%k == 0):
            #sub=list(set(string[0:k]))
            w=string[0:k]
            s=unique(w)
            print(result.join(s))
            string=string[k:]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)