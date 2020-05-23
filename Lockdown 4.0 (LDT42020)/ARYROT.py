#
# 
# solution

t = int(input())

while(t>0):
    n, d = list(map(int, input().split()))
    array = list(map(int, input().split()))
    t-=1

    if n == d:
        for i in range(n):
            print(array[i], end=' ')
        print('\n')
        continue

    for i in range(n-d, n):
        print(array[i], end=' ')

    for i in range(n-d):
        print(array[i], end=' ')

    print('\n')
    