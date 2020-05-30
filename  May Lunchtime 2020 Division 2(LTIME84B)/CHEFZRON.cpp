//
//
//
//
// solved
/*
#ifndef Local
#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops,fast-math,O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,sse4.2,popcnt,abm,mmx,avx")
#endif

#include <bits/stdc++.h>

#include <ext/numeric>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace __gnu_cxx;
using namespace std;

#define popCnt(x) (__builtin_popcountll(x))
#define sz(x) ((int)(x.size()))
#define all(v) begin(v), end(v)
typedef long long Long;

const int N = 2e6 + 5;
const int OO = 1e9;

vector<int> ones;
int memo[N][3];
int vis[N][3];
int vid;
int _end;

int solve(int ind, int prev) {
  if (ind == _end) {
    return 0;
  }
  if (prev < ind - 2) prev = ind - 2;
  int& res = memo[ind][ind - prev];
  if (vis[ind][ind - prev] == vid) return res;
  vis[ind][ind - prev] = vid;

  if (prev == ind) {
    res = solve(ind + 1, ind);
  } else {
    res = solve(ind + 1, ind + 1) + ones[ind + 1] - ones[ind];
    if (prev + 1 == ind) {
      res = min(res, solve(ind + 1, prev) + ones[ind] - ones[ind - 1]);
    }
  }
  return res;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int t;
  cin >> t;

  while (t--) {
    ones.clear();
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
      bool x;
      cin >> x;
      if (x) {
        ones.emplace_back(i);
      }
    }
    if (ones.size() == 1) {
      cout << -1 << endl;
      continue;
    }
    if (ones.empty()) {
      cout << 0 << endl;
      continue;
    }
    for (int i = 0; ones[i] < n; ++i) {
      ones.emplace_back(ones[i] + n);
    }
    ones.emplace_back(OO / 2);
    int res = OO;

    ++vid;
    _end = ones.size() / 2;
    res = min(res, solve(0, -2));

    ++vid;
    ++_end;
    res = min(res, solve(1, -2));

    ++vid;
    _end = ones.size() - 1;
    res = min(res, solve(ones.size() / 2 - 1, -2));

    cout << res << endl;
  }

  return 0;
}
*/