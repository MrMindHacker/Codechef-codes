t = int(input())
ans = []


"""
def find_fib(index):
    if index == 1:
        return 0
    else:
        #index += 1
        print(index)
        a = (round(((1.618**index)-(-0.618**index))/2.236)) % 10
        return a
        """


def find_fib(n):
    # fibo = 2.078087 * math.log(n) + 1.672276
    """phi = (1 + 5**0.5)/2.0
    return int(round((phi**n - (1-phi)**n) / 5**0.5))"""
    return 0  # fibo


fiblist = [0, 1]
last = 0
next = 1
max = 0


for testcase in range(t):
    n = int(input())
    j = 1
    while j < n:
        j = j << 1

    if max < j:
        for i in range(max, j):
            if i == 0 or i == 1:
                continue
            temp = next
            next = last + next
            last = temp

            if (i + 1) and (not ((i + 1) & (i))):
                fiblist.append(next)
        max = j

    ans.append(find_fib(2**j))

print(fiblist)
for i in ans:
    print(i)


# code to find n in 2 rais to #
que = []
for testcase in range(t):
    n = int(input())
    j = 1
    temp = 0
    while j < n:
        temp += 1
        j = j << 1
    que.append(temp)
    if max < temp:
        max = temp
