t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))

    if m == 0 or n == 0:
        ans = -1
    elif m < n-1:
        ans = -1
    elif m == n-1:
        ans = 1
    else:
        m = m-n-1
        ans = 1 + int(m/n) + 1
    print(ans)
