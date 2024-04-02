def bs(data,item,low,high):
    # 못 찾았을 경우
    if low > high :
        return -1
    else:
        mid = (low + high) // 2
        # 배열의 중간에 위치한 값이 item과 일치하면 그 때의 index값 반환
        if(data[mid]==item):
            return mid
        # 배열의 중간(mid)에 위치한 값이 item보다 작으면
        # item은 mid 보다 뒤에 있으므로 mid+1~high에서 재탐색
        elif(data[mid]<item):
            return bs(data,item,mid+1,high)
        # 배열의 중간(mid)에 위치한 값이 item보다 크면
        # item은 mid 보다 앞에 있으므로 low~mid-1에서 재탐색
        else:
            return bs(data,item,low,mid-1)
data=[1,3,5,6,7,9,10,14,17,19]
n = 10
location = bs(data,17,0,n-1)
print(location)
print("-----------------------------------")

def merge(h,m,u,v,s):
    i=j=k=0
    # u와 v는 이미 정렬된 상태이다
    # 각 배열의 첫 원소부터(가장 작은 원소 부터) 서로 비교한다
    # 그 중에 작은 숫자를 s[k]에 저장한다 
    # 작은 숫자가 있던 배열의 다음 인덱스의 숫자와 아까 비교했던 숫자와 다시 비교한다
    # 이 과정을 한 배열의 모든 숫자를 다 저장할 때까지 반복한다
    while(i < h and j < m):
        if(u[i]<v[j]):
            s[k] = u[i]
            i+=1
        else:
            s[k] = v[j]
            j+=1
        k+=1
    # s에 추가되지 않은 숫자들을 마지막으로 추가해준다
    if(i>=h):
        s[k:h+m]=v[j:m]
    else:
        s[k:h+m]=u[i:h]

def mergeSort(n,s):
    h = n//2
    m = n-h
    if(n>1):
        u = s[:h]
        v = s[h:]
        mergeSort(h,u)
        mergeSort(m,v)
        merge(h,m,u,v,s)

s = [3,5,2,9,10,14,4,8]
mergeSort(8,s)
print(s)
    



