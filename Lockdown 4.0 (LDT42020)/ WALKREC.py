#
# 
# solution

import math
for i in range(int(input())):
    n,k=map(int,input().split())
    k=k-1
    s=n*n
    if n==0:
        k+=1
        print((k*(k-1))%(10**9+7))
        continue
    if k==0:
        print(s%(10**9+7))
        continue
    if k%2==0:
        s+=(2*n)*(k/2)
        p=(k/2)*(2*2+(k/2-1)*2)
        p=p/2
        s+=p
    else:
        x=math.ceil(k/2)
        k=k-x
        s+=(2*n)*x
        p=k*(4+(k-1)*2)
        p=p/2
        s+=p
    print(int(s)%(10**9+7))


#
# 
# solution

import math
mod=1000000007
T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    if (n==0):
        print((m*(m-1))%mod)
        
    elif (m==1):
        print(((n*(n-1))+n)%mod)

    else:
        val=n-1+(math.ceil((m-1)/2))
        fv=(val*(val+1))%mod
        if ((m-1)%2==0):
            fv=(fv+(2*(val+1))-n)%mod
        else:
            fv=(fv+n)%mod

        print(fv%mod)