# t = int(input())

# while(t>0):
#     string = input()
#     l = len(string)
#     ans = ((l*(l+1))/2)-l-1
#     ans = ans%1000000007
#     print(int(ans))


#
#
# solution by aert [33263655]

from math import factorial
import sys
mod = 10**9 + 7

t = int(sys.stdin.readline().strip())
for _ in range(t):
	s = sys.stdin.readline().strip()
	n = len(s)-1
	print(factorial(2*n)//(factorial(n)*factorial(n+1))%mod)


#
#
# solution by arora_kshitiz [33266798]

# cook your dish here
import sys
msg = sys.stdin.read()

l=list(msg.split())

from math import factorial as fact

def paren(n):
    if n==1:
        return 1
    n-=1
    n1 = fact(2*n)/(fact(n)*fact(n))
    n2 = fact(2*n)/(fact(n+1)*fact(n-1))
    return int(n1-n2)%1000000007
    
for i in l[1:]:
    n = len(i)
    print(paren(n))