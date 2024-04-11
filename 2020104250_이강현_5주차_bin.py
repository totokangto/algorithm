import numpy as np
def bin(n,k):
    if k==0 or n ==k:
        return 1
    else:
        return bin(n-1,k-1) + bin(n-1,k)

def bin2(n,k):
    b = np.zeros((n+1,k+1))
    for i in range(n+1):
        for j in range(min(i,k)+1):
                if j==0 or j==i:
                    b[i,j]=1
                else: b[i,j] = b[i-1,j-1] + b[i-1,j]
    return int(b[n,k])

print(bin(10,5),bin2(10,5))