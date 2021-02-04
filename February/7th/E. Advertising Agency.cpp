#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<functional>
#include<algorithm>
using namespace std;
using ll = long long;
const int MAX_N = 1001, LIMIT = 1e7 + 1, MOD = 1e9 + 7;
int main() {
    map<int, int> p;
    int t, k, n, a, i, j, ans, nCr[MAX_N][MAX_N] = { 1 };
    for (i = 1; i < MAX_N; i++) {
        nCr[i][0] = 1;
        for (j = 1; j <= i; j++)
            nCr[i][j] = (nCr[i - 1][j - 1] + nCr[i - 1][j]) % MOD;
    }
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &n, &k);
        p.clear();
        for (i = 0; i < n; i++) {
            scanf("%d", &a);
            p[a]++;
        }
        ans = 1;
        for (auto it = p.rbegin(); it != p.rend(); it++) {
            if (k >= it->second)
                k -= it->second;
            else {
                ans = nCr[it->second][k];
                break;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}