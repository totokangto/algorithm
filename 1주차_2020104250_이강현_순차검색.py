def seqsearch(s,x):
    t = 0
    while(t < len(s)):
        if(s[t]==x):
            return t
        t = t + 1
    return -1
s = [3,5,2,1,7,9]
loc = seqsearch(s,4)
print(loc)