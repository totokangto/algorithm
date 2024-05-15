import utility
#a=['A','A','C','A','G','T','T','A','C','C']
a=['A','C','G','A','C','T']
#b=['T','A','A','G','G','T','C','A']
b=['C','C','G','A','T','C','T']
m=len(a)
n=len(b)
table=[[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex = [[ (0,0) for j in range(0,n+1)] for i in range(0,m+1)]

# 틈 행 채우기
for j in range(n-1,-1,-1):
    table[m][j] =table[m][j+1]+2
# 틈 열 채우기
for i in range(m-1,-1,-1):
    table[i][n] =table[i+1][n]+2

# 테이블 생성 구현
for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            penalty = 0
            # 불일치할 경우 penalty = 1
            if a[i] != b[j]:
                penalty = 1
            # opt(i,j) = min(opt(i+1,j+1)+penalty, opt(i+1,j)+2, opt(i,j+1)+2)
            table[i][j] = min(table[i+1][j+1] + penalty, table[i+1][j] + 2, table[i][j+1] + 2)

            # min값이 어디로 부터 왔는지의 정보 저장
            if table[i][j] == table[i + 1][j + 1] + penalty:  
                minindex[i][j] = (i + 1, j + 1)
            elif table[i][j] == table[i + 1][j] + 2:  
                minindex[i][j] = (i + 1, j)
            else:
                minindex[i][j] = (i, j + 1)


utility.printMatrix(table)
x=0
y=0

while (x <m and y <n):
    tx, ty = x, y
    print(minindex[x][y])
    (x,y)= minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx]," ", b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")
