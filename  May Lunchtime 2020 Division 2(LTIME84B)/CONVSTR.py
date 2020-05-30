t = int(input())

while(t>0):
    t-=1
    n = int(input())
    a = input()
    b = input()

    l1 = []
    l2 = []

    a_cnt = a.find('a')
    b_cnt = a.find('b')

    if True:
        if a==b:
            print(0)
        elif a_cnt == -1 and a_cnt == -1:
            print(-1)
        elif a_cnt != -1 and a_cnt != -1:
            for i in range(n):
                if a[i] != 'b' and b[i] != 'a':
                    a[i] = 'b'
                    l1.append(i)
                elif a[i] == 'b' and b[i] == 'a':
                    l2.append(i)
                elif a[i] == 'a' and b[i] == 'b':
                    ans = -1
        
        print()


#
# 
# 
# solved
# cook your dish here
'''
from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    sa = set(a)
    sb = set(b)
    
    for i in range(n):
        if a[i]<b[i]:
            print(-1)
            break
        elif b[i] not in sa:
            print(-1)
            break
    else:
        d = dict()
        
        for i in range(n):
            if a[i]!=b[i]:
                if b[i] not in d:
                    d[b[i]]=[0]
                d[b[i]][0]+=1
                d[b[i]]+=[i]
        cov = sorted(d,reverse=True)
        ans = []
        opr = len(cov)
        for i in cov:
            t = [d[i][0]+1]+[a.index(i)]+d[i][1:]
            #print(i)
            #print(t)
            ans.append(t)
        print(opr)
        for i in ans:
            print(*i,sep=' ')
'''

#
# 
# 
# solved2
'''
for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())
    ase = set(a)
    bse = set(b)
    if a==b:
        print(0)
    
    elif bse.issubset(ase):
        d={}
        wr = {}
        f=0
        for i in range(n):
            if a[i]!=b[i]:
                if b[i] in d:
                    d[b[i]].append(i)
                    wr[b[i]].append(a[i])
                else:
                    d[b[i]]=[]
                    wr[b[i]]=[]
                    d[b[i]].append(i)
                    wr[b[i]].append(a[i])

        # print(wr,d)
        for k,v in sorted(wr.items(),reverse=True):
            # print(k,v)
            for i in v:
                # print(k,i)
                if ord(k)>ord(i):
                    f=1
                    break
            if f==1:
                break
        # print(flag)
        if f==1:
            print(-1)
        else:
            print(len(d))
            for k,v in sorted(d.items(),reverse=True):
                print(len(d[k])+1,end=" ")
                print(*d[k],a.index(k))
        
        
    else:
        print(-1)
'''
