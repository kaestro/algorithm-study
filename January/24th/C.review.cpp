#include <vector>
#include <iostream>

using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

class Solution {
private:
    int N, A, B;
    vi pa, pb, ca, cb; // parent a, b; count a, b;
    vvi Adj;

    void dfs(int u, vi& path) {
        int len = path.size();
        if (len >= A) 
            pa[u] = path[len - A];
        if (len >= B) 
            pb[u] = path[len - B];

        ca[u] = 1, cb[u] = 1;

        path.push_back(u);
        for (int v : Adj[u]) 
            dfs(v, path);
        path.pop_back();

        if (len >= A)
            ca[pa[u]] += ca[u];
        if (len >= B)
            cb[pb[u]] += cb[u];
    }

public:
    Solution(int N):
        N(N), A(0), B(0),
        pa(N+1), pb(N+1), ca(N+1), cb(N+1),
        Adj(N+1, vi())
        {}
    
    void solve() {
        cin >> A >> B;
        int parent;
        for (int i = 2; i <= N; ++i) {
            cin >> parent;
            Adj[parent].push_back(i);
        }

        vi path;
        dfs(1, path);
        double ans = 0;
        double prob_A, prob_B;
        for (int i = 1; i <= N; ++i) {
            prob_A = (double) ca[i] / N;
            prob_B = (double) cb[i] / N;
            ans += prob_A + prob_B - prob_A * prob_B;
        }
        cout << ans << "\n";
    }

};


int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T, N;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        cin >> N;
        Solution sol = Solution(N);

        cout << "Case #" << test_case << ": ";
        sol.solve();
    }
    return 0;
}
