#
# 
# 
# solved
# cook your dish here
'''
from collections import deque

def readTree(n):
    adj = [set() for _ in range(n)]
    for _ in range(n-1):
        u,v = map(int, input().split())
        adj[u-1].add(v-1)
        adj[v-1].add(u-1)
    return adj



def main():
    def solve():
        n,q = map(int, input().split())
        aa = [int(a) for a in input().split()]
        adj = readTree(n)
        dq = deque()
        dq.append(0)
        parent = [-2] + [-1] * (n-1)
        depth = [0] * n
        while dq:
            nd = dq.popleft()
            for a in adj[nd]:
                if parent[a] < 0:
                    parent[a] = nd
                    depth[a] = depth[nd] + 1
                    dq.append(a)

        def solve1():

            a,b = map(int, input().split())
            a -= 1
            b -= 1
            values = set()
            if depth[b] > depth[a]:
                b,a = a,b
            while depth[a] > depth[b]:
                if aa[a] in values:
                    print(0)
                    return
                values.add(aa[a])
                a = parent[a]
            while a != b:
                if aa[a] in values:
                    print(0)
                    return
                values.add(aa[a])
                a = parent[a]
                if aa[b] in values:
                    print(0)
                    return
                values.add(aa[b])
                b = parent[b]
            if aa[a] in values:
                print(0)
                return
            values.add(aa[a])
            lv = list(values)
            lv.sort()
            mn = n
            for i in range(len(lv)-1):
                mn = min(lv[i+1] - lv[i], mn)
                if mn == 1:
                    break
            print(mn)


        for _ in range(q):
            solve1()

    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
'''

#
# 
# 
# solved
# cook your dish here
'''
#include <bits/stdc++.h>
using namespace std;
 
const int MAXN = 200005;
const int MAXM = 200005;
const int LN = 19;
const int mod=1000000007; 
int N, M, K, cur, LVL[MAXN], DP[LN][MAXN];
int BL[MAXN << 1], ID[MAXN << 1], VAL[MAXN], ANS[MAXM];
int d[MAXN], l[MAXN], r[MAXN],minv[20*MAXN],freq[105],a[MAXN];
bool VIS[MAXN];
vector < int > adjList[MAXN];
 
struct query{
	int id, l, r, lc;
	bool operator < (const query& rhs){
		return (BL[l] == BL[rhs.l]) ? (r < rhs.r) : (BL[l] < BL[rhs.l]);
	}
}Q[MAXM];

    
// Set up Stuff
void dfs(int u, int par){
	l[u] = ++cur; 
	ID[cur] = u;
	for (int i = 1; i < LN; i++) DP[i][u] = DP[i - 1][DP[i - 1][u]];
	for (int i = 0; i < adjList[u].size(); i++){
		int v = adjList[u][i];
		if (v == par) continue;
		LVL[v] = LVL[u] + 1;
		DP[0][v] = u;
		dfs(v, u);
	}
	r[u] = ++cur; ID[cur] = u;
}
 
// Function returns lca of (u) and (v)
inline int lca(int u, int v){
	if (LVL[u] > LVL[v]) swap(u, v);
	for (int i = LN - 1; i >= 0; i--)
		if (LVL[v] - (1 << i) >= LVL[u]) v = DP[i][v];
	if (u == v) return u;
	for (int i = LN - 1; i >= 0; i--){
		if (DP[i][u] != DP[i][v]){
			u = DP[i][u];
			v = DP[i][v];
		}
	}
	return DP[0][u];
}
 
inline void check(int x, long& res){
// 	If (x) occurs twice, then don't consider it's value 
	if(!VIS[x])
	    freq[a[x]]++;
	else
	    freq[a[x]]--;
	VIS[x] ^= 1;
}
 
void compute(){
	
	// Perform standard Mo's Algorithm
	int curL = Q[0].l, curR = Q[0].l - 1;
	long res = 1l;
	
	for (int i = 0; i < M; i++){
		
		while (curL < Q[i].l) check(ID[curL++], res);
		while (curL > Q[i].l) check(ID[--curL], res);
		while (curR < Q[i].r) check(ID[++curR], res);
		while (curR > Q[i].r) check(ID[curR--], res);
		
		int u = ID[curL], v = ID[curR];
		// Case 2
		if (Q[i].lc != u and Q[i].lc != v) check(Q[i].lc, res);
		int tmp = 0, ind = 0, ans = (int)(1e8);
		while(freq[ind] < 1)
		    ind++;
	    if(freq[ind] > 1)
	        ans = 0;
		tmp = ind;
		ind++;
		for(; ind < 102; ind++)
		{
		    if(freq[ind] > 1)
		    {
		        ans = 0;
		        break;
		    }
		    if(freq[ind] > 0)
		    {
		        ans = min(ans, ind - tmp);
		        tmp = ind;
		    }
		    
		}
		ANS[Q[i].id] = ans;
		
		if (Q[i].lc != u and Q[i].lc != v) check(Q[i].lc, res);
	}
 
	for (int i = 0; i < M; i++) printf("%d\n", ANS[i]);
}
 
int main(){
 
	int u, v, x, t;
	scanf("%d",&t);
	while (t--){
		scanf("%d", &N);
		scanf("%d", &M);
		// Cleanup
		cur = 0;
		memset(VIS, 0, sizeof(VIS));
		memset(VAL, 0, sizeof(VAL));
		memset(freq, 0, sizeof(freq));
		for (int i = 1; i <= N; i++)
		    adjList[i].clear();
		
		// Inputting Values
		for (int i = 1; i <= N; i++)
		    scanf("%d", &a[i]);
		    
		// Inputting Tree
		for (int i = 1; i < N; i++){
			scanf("%d %d", &u, &v);
			adjList[u].push_back(v);
			adjList[v].push_back(u);
		}
		
		// Preprocess
		DP[0][1] = 1;
		dfs(1, -1);
		int size = 1000;//sqrt(cur);
		for (int i = 1; i <= cur; i++) BL[i] = (i - 1) / size + 1;
		for (int i = 0; i < M; i++){
			scanf("%d %d", &u, &v);
			Q[i].lc = lca(u, v);
			if (l[u] > l[v]) swap(u, v);
			if (Q[i].lc == u) Q[i].l = l[u], Q[i].r = l[v];
			else Q[i].l = r[u], Q[i].r = l[v];
			Q[i].id = i;
		}
 
		sort(Q, Q + M);
		compute();
	}
}
'''