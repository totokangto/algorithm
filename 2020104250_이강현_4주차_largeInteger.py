import math

def prod2(a,b):
    # a와 b중 자릿수가 작은 것의 자릿수를 n에 저장
    # int를 str로 변환한 뒤 len()을 통해 자릿수 구함
    n = max(len(str(a)),len(str(b)))
    if(a==0 or b==0):
        return 0
    elif(n<3):
        return a*b
    else:
        m = math.floor(n/2)
        # a = x*10^m + y
        x = a // (10**m)
        y = a % (10**m)
        # b = w*10^m + z
        w = b // (10**m)
        z = b % (10**m)
        # r = (x+y)*(w+z)
        r = prod2(x+y,w+z)
        p = prod2(x,w)
        q = prod2(y,z)
        # a*b = (x*w)*10^2m + (xz+wy)*10^m + yz
        # xz+wy = r-p-q
        return p*(10**(2*m)) + (r-p-q)*(10**m) + q
a=1234567812345678
b=2345678923456789
print(prod2(a,b))
print(a*b)
    