inf=1000
w = [
    [0,3,2,8,inf,inf],
    [inf,0,1,inf,5,inf],
    [inf,inf,0,5,3,inf],
    [inf,inf,inf,0,3,2],
    [inf,inf,inf,inf,0,1],
    [inf,inf,inf,inf,inf,0]
]
n=6
f=set()
touch=n*[0]
length=n*[0]
save_length = n*[0]

for i in range(1,n):
    length[i]=w[0][i]

for i in range(1,n):
    minima = inf
    for j in range(1,n):
        # V-Y에 속하면서 v1에서 Y에 속한 정점 만을 거쳐서
        # 최단 경로가 되는 가장 가까운 vi찾기
        if 0 <= length[j] < minima :
            minima = length[j]
            vnear = j 
    edge = (touch[vnear], vnear)
    f.add(edge)
    # 새로운 정점이 y에 추가된 후에 
    # y에 없는 정점들에 대해서
    # 새로운 정점을 마지막으로 거쳤을 때의 거리가 
    # 기존의 최단 거리보다 더 짧은지 확인 후 갱신
    for k in range(1,n):
        if length[vnear] + w[vnear][k] < length[k]:
            length[k] = length[vnear] + w[vnear][k] 
            touch[k] = vnear
    for m in range(1,n):
        if length[m] >=0:
            save_length[m] = length[m]
    length[vnear] = -1

# n개의 노드 이름 만들기
nodes=[]
j = 0
for i in range(ord('a'),ord('z')+1):
    if j < n:
        nodes.append(chr(i))
        j += 1
    else: break

print("각 노드로 가는 최단 경로 및 최단 거리")
print(f, save_length)
min_idx = save_length.index(min(save_length[1:])) # 시작 노드 제외
max_idx = save_length.index(max(save_length))
print(f"가장 짧은 길이 : {save_length[min_idx]}, 노드 : {nodes[min_idx]}")
print(f"가장 긴 길이 : {save_length[max_idx]}, 노드 : {nodes[max_idx]}")


            
