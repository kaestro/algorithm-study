#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

using vi = vector<int>;
using vvi = vector<vi>;

class Solution {
    int n, a, b;
    vvi adj;
    vi pa, pb, ac, bc;
    void dfs(int u, vi& path) {
        int l = path.size();
        if (l >= a)
            pa[u] = path[l-a];
        if (l >= b)
            pb[u] = path[l-b];
        path.push_back(u);
        ac[u] = 1, bc[u] = 1;
        for (int v : adj[u])
            dfs(v, path);
        path.pop_back();
        if (pa[u] > 0)
            ac[pa[u]] += ac[u];
        if (pb[u] > 0)
            bc[pb[u]] += bc[u];
    }

public:
    void solve(int case_num) {
        cin >> n >> a >> b;
        adj = vvi(n+1);
        int v;
        for (int i = 2; i <= n; ++i) {
            cin >> v;
            adj[v].push_back(i);
        }

        pa = vi(n+1);
        pb = vi(n+1);
        ac = vi(n+1);
        bc = vi(n+1);

        vi path;
        dfs(1, path);
        double ans = 0;
        for (int i = 1; i <= n; ++i) {
            ans += (double)(ac[i] + bc[i]) * n;
            ans -= (double)ac[i] * bc[i];
        }
        printf("Case #%d: %.12f\n", case_num, ans / n / n);
    }
};

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        Solution solution = Solution();
        solution.solve(i);
    }
    return 0;
}
