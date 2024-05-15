import utility

inf = 1000
w=[[0, 1, 3,inf, inf],
[1, 0, 3,6, inf],
[3, 3, 0,4, 2],
[inf,6, 4,0, 5],
[inf,inf,2,5, 0]]

F=set()
utility.printMatrix(w)
n=len(w)
nearest=n*[0] 
distance=n*[0] 

for i in range(1,n):
    nearest[i]=0 # y에 속한 정점 중 vi와 가장 가까운 정점
    distance[i]=w[0][i] # vi와 nearest[i]를 잇는 edge의 weight

# prim’s 알고리즘 구현
for i in range(1,n):
    min = 1000
    for j in range(1,n):
        # y와 가장 가까운 정점 찾기
        if 0 <= distance[j] < min :
            min = distance[j]
            vnear = j 
    # 위에서 찾은 정점과 y에 속해있는 정점 사이의 edge F에 추가
    edge = (vnear,nearest[vnear])
    F.add(edge)
    distance[vnear] = -1
    # 새로운 정점이 y에 추가된 후에
    # y에 없는 정점들에 대해서
    # 기존의 최단 거리보다 새로운 정점과의 거리가 더 짧은지 확인 후 갱신
    for k in range(1,n):
        if w[k][vnear] < distance[k]:
            distance[k] = w[k][vnear] 
            nearest[k] = vnear

print()
print(F)

