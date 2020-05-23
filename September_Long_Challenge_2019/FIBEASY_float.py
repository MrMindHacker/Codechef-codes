import math

t = int(input())
ans = []
ques = []


def find_fib(n):
    fibo = 2.078087 * math.log(n) + 1.672276
    # phi = (1 + 5**0.5) / 2.0
    return fibo  # int(round(((phi**n - (1 - phi)**n) / 5**0.5) % 10))


for testcase in range(t):
    n = float(input())
    j = 1
    while j < n:
        j = j << 1
    ans.append(j)

for i in ans:
    print(find_fib(i))
