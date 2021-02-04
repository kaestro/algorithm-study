#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<functional>
#include<cmath>
#include<algorithm>
using namespace std;
using ll = long long;
const int MAX_N = 2e5+1, LIMIT = 1e7 + 1, MOD = 1e9 + 7;
vector<int> adj[MAX_N];
int main() {
    int t, a[MAX_N], n, i, j, sqrta, dp[MAX_N], ans, cnt[MAX_N];
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        memset(cnt, 0, sizeof cnt);
        for (i = 0; i < n; i++) {
            scanf("%d", &a[i]);
            cnt[a[i]]++;
        }
        sort(a, a + n);
        memset(dp, 0, sizeof dp);
        ans = cnt[1];
        for (i = 0; i < n; i++) {
            sqrta = sqrt(a[i]);
            int& dpa = dp[a[i]];
            if (dpa > 0) continue;
            if (a[i] == 1) continue;            

            dpa = cnt[1] + cnt[a[i]];
            for (j = 2; j <= sqrta; j++) if (a[i] % j == 0)
                dpa = max({ dpa, dp[j] + cnt[a[i]], dp[a[i] / j] + cnt[a[i]] });
            ans = max(ans, dpa);
        }
        printf("%d\n", n - ans);
    }
    return 0;
}