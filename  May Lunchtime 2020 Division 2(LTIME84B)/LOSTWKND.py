t = int(input())

while(t>0):
    t-=1
    arr = list(map(int, input().split()))
    n = arr[-1]
    arr.pop()
    sum_arr = sum(arr)*n
    if sum_arr <= 120:
        print("No")
    else:
        print("Yes")