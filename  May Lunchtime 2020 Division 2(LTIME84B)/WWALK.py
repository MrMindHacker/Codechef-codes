t = int(input())

while(t>0):
    t-=1
    n = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))

    alice_dist = 0
    bob_dist = 0
    ans = 0
    last = True

    for i in range(n):
        alice_dist += alice[i]
        bob_dist += bob[i]

        if alice_dist == bob_dist:
            if last == True:
                ans += bob[i]
            else:
                last = True
        else:
            last = False
    
    print(ans)