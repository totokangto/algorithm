# 1. sum of subsets problem
print("============problem 1 ===============")
def promising_ss(i,weight, total):
    # 현재 무게와 남아있는 무게의 합이 W보다 크면서
    # 현재 무게가 W와 같거나 
    # 현재 무게와 그 다음 아이템의 무게를 더한 값이 W보다 작거나 같을 경우 promissing
    return (weight+total >= W) and (weight == W or weight+w[i+1] <= W)
def s_s(i, weight, total, include):
    global node_counter_ss
    node_counter_ss += 1
    if(promising_ss(i,weight,total)):
        if(weight==W):
            print(include)
        else:
            include[i+1] = 1 # 그 다음 아이템을 추가하는 경우
            s_s(i+1,weight+w[i+1],total-w[i+1],include)
            include[i+1] = 0 # 그 다음 아이템을 추가하지 않는 경우
            s_s(i+1,weight,total-w[i+1],include)

n=5
w=[2,3,5,7,8]
W=8
print("items =",w, "W =", W)
include = n*[0]
total=0
node_counter_ss = 0 # 총 노드 수를 세기 위한 변수
for k in w:
    total+=k
s_s(-1,0,total,include)
print(node_counter_ss)

# 2. graph coloring
print("============problem 2 ===============")
def color(i,vcolor,n):
    global node_counter_col
    node_counter_col += 1
    if(promising_col(i,vcolor)):
        if(i==n-1):
            print(vcolor)
        else:
            for c in range(1,m+1):
                vcolor[i+1] = c
                color(i+1,vcolor,n)

def promising_col(i,vcolor):
    switch = True
    j = 0
    # i번째 지역과 인접한 지역 중에 같은 색깔이 있으면 nonpromissing
    while(j<i and switch):
        if(W[i][j] and vcolor[i]==vcolor[j]):
            switch = False
        j += 1
    return switch

n=6 # n개의 지역
W = [[0,1,0,1,0,0],[1,0,1,0,1,0],[0,1,0,0,1,0],
     [1,0,0,0,1,1],[0,1,1,1,0,1],[0,0,0,1,1,0]]
vcolor=n*[0]
m=3 # m개의 색상
node_counter_col = 0
color(-1,vcolor,n)
print(node_counter_col)