import numpy as np
def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(m):
        for j in range(n):
            print(f'{d[i,j]:4}',end=" ")
        print()

def allShortestPath(g,n):
    p = np.zeros((n,n))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if g[i,k]+g[k,j] < g[i,j]:
                    p[i,j] = k+1
                    g[i,j] = g[i,k]+g[k,j]
    g = g.astype(int)
    p = p.astype(int)
    return g,p

def path(p,q,r):
    # ndarray의 index는 0부터 시작하므로 
    # index를 위한 새로운 변수 생성
    q_idx = q-1
    r_idx = r-1
    if p[q_idx,r_idx] != 0:
        path(p,q,p[q_idx,r_idx])
        print(" v"+str(p[q_idx,r_idx]))
        path(p,p[q_idx,r_idx],r)

inf = 1000
g = [[0,1,inf,1,5],
     [9,0,3,2,inf],
     [inf,inf,0,4,inf],
     [inf,inf,2,0,3],
     [3,inf,inf,inf,0]
     ]
# numpy를 이용해서 ndarray로 바꾸는 코드를 추가했습니다
g = np.array(g)
d,p = allShortestPath(g,5)
print()
printMatrix(d)
print()
printMatrix(p)
path(p,5,3)