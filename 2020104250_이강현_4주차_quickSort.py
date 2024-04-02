def quickSort(s,low,high):
    
    if(high>low):
        p = partition(s,low,high)
        quickSort(s,low,p-1)
        quickSort(s,p+1,high)

def partition(s,low,high):
    pitem = s[low]
    j = low
    for i in range(low+1,high+1):
        if(s[i]<pitem):
            j +=1
            s[i],s[j] = s[j],s[i]
    s[low],s[j] = s[j],s[low]
    return j
s=[3,5,2,9,10,14,4,8]
quickSort(s,0,7)
print(s)