parent = dict()
rank = dict()
def make_singleton_set(v):
    parent[v] = v
    rank[v] = 1

# tree의 root찾기
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]
def union(r1, r2):
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
            rank[r1] += rank[r2]
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]: rank[r2] += rank[r1]
def kruskal(graph):
    #Kruskal algorithm 구현
    # make_singleton_set을 이용하여
    # 정점의 개수만큼 disjoint set 초기화
    for i in range(len(graph['vertices'])):
        make_singleton_set(graph['vertices'][i])
    # edge를 가중치의 비내림차순으로 정렬
    sorted_e = sorted(list(graph['edges']))
    F = set()
    # F에 (정점의 개수 - 1)개의 이음선이 추가될 때까지
    # = 모든 정점이 연결될 때까지
    while len(F) < len(graph['vertices'])-1:
        
        e = sorted_e[0] # 아직 점검하지 않은 최소의 가중치를 가진 edge
        i, j = e[1], e[2] # e로 이어진 양 끝의 정점
        p = find(i) # i의 root(i가 속한 set) 찾기
        q = find(j) # j의 root(j가 속한 set) 찾기
        
        # root가 다른 경우에만 set을 union 
        # = 이미 같은 set 안에 있다면 pass
        # = 두 정점 i,j가 이미 같은 set 안에 있다면 pass
        if p != q:    
            union(p,q)
            F.add(e)
        sorted_e.pop(0) # 정렬된 정점 제거
    return F
    

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E'],
    'edges': set([
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (3, 'B', 'C'),
    (6, 'B', 'D'),
    (4, 'C', 'D'),
    (2, 'C', 'E'),
    (5, 'D', 'E'),
    ])
}
mst=kruskal(graph)
print(mst)
