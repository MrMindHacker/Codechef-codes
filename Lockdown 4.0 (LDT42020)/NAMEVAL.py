# vowels = ['a', 'e', 'i', 'o', 'u']
# t = int(input())

# while(t>0):
#     t-=1

#     string_array = list(input())

#     ans = 0

#     for s in string_array:
#         if s in vowels:
#             ans *= 2
#         else:
#             ans *= 2 
#             ans += 1

#     print(ans%1000000007)


#
# 
# solution

from sys import stdin,stdout
import bisect
from collections import defaultdict
def main():
    for _ in range(int(stdin.readline())):
        st=stdin.readline().strip()
        res=0
        for i in range(len(st)):
            if st[i]=="a" or st[i]=="e" or st[i]=="i" or st[i]=="o" or st[i]=="u":
                continue
            else:
                shift=(len(st)-i-1)
                res+=(1<<shift)
        print(res)
                   
                
        
                
            
if __name__=="__main__":
    main()