import sys
def promising(i,col):
    switch = True
    k = 0
    while(k<i and switch):
        # i번째 queen
        # 1~i-1번째 queen과 같은 column이거나 같은 대각에 있다면
        # non-promising, 그렇지 않으면 promising
        if(col[i]==col[k] or abs(col[i]-col[k])==i-k):
            switch = False
        k += 1
    return switch

def queens(n,i,col):
    # queens가 호출 될 때마다 node_counter 1씩 추가
    global node_counter
    node_counter += 1
    
    if(promising(i,col)):
        # 끝까지 다 돌았을 경우
        if(i==n-1):
            print(col)
            # 끝까지 다 돌았을 경우가 해가 되므로
            # 이 때 sol_counter 1씩 추가
            global sol_counter
            sol_counter += 1
            # 다섯 번째 해인 경우 col의 값들을 five_sol에 추가
            if sol_counter == 5:
                for i in range(n):
                    five_sol.append(col[i])
        else:
            for k in range(n):
                col[i+1] = k
                queens(n,i+1,col)
                
                
n=8
col=n*[0]
sol_counter = 0 # 총 해의 개수를 저장하기 위한 변수
five_sol=[] # 다섯 번째 해를 저장하기 위한 리스트
node_counter=0 # 총 노드 수를 저장하기 위한 변수
queens(n,-1,col)
print(f"총 해의 개수 : {sol_counter}")
print(f"다섯 번째 해 : {five_sol}")
print(f"총 노드 수 : {node_counter}")




