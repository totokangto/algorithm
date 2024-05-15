import utility
class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data = data
def tree(key,r,i,j):
    k=r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
        return p
#key=[" ","A","B","C","D"]
key=[" ","A","B","C","D","E"]
# p1=3/16, p2=4/16, p3=2/16, p4=6/16, p5=1/16
p=[0,0.1875, 0.25, 0.125,0.375,0.0625]
#p=[0,0.375, 0.375, 0.125,0.125]
n=len(p)-1

a=[[0 for j in range(0,n+2)] for i in range(0,n+2)]
r=[[0 for j in range(0,n+2)] for i in range(0,n+2)]

for i in range (1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0

# 구현
for diag in range(1,n):
    for i in range(1,n-diag+1):
        j = i+diag
        temp_min = a[i][i-1] + a[i+1][j]
        sum_p = a[i][i]
        arg_k = i

        # 위에서 k = i일때의 값을 저장했기에 k = i+1부터 시작
        for k in range(i+1,j+1):
            sum_p += a[k][k]
            if temp_min > a[i][k-1] + a[k+1][j]:
                temp_min = a[i][k-1] + a[k+1][j]
                arg_k = k
        a[i][j] = temp_min + sum_p
        r[i][j] = arg_k


utility.printMatrixF(a)
print()
utility.printMatrix(r)
root=tree(key,r,1,n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)