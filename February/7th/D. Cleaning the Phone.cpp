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
const int MAX_N = 2e5, LIMIT = 1e7 + 1;
int main() {
    int t, n, m, a[MAX_N], b, i, j, k, ans, N, M, tmp[2], tm;
    vector<int> reg, imp;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &n, &m);
        reg.clear(), imp.clear();
        for (i = 0; i < n; i++) scanf("%d", &a[i]);
        for (i = 0; i < n; i++) {
            scanf("%d", &b);
            (b % 2 ? reg : imp).push_back(a[i]);
        }
        sort(reg.begin(), reg.end(), greater<int>());
        sort(imp.begin(), imp.end(), greater<int>());

        N = reg.size(), M = imp.size();

        ans = 0;        
        i = 0, j = 0;
        while (m > 0 && (i < N || j < M)) {
            if (i < N && j < M) {
                if (i + 1 < N) {
                    if(reg[i] + reg[i+1] >= imp[j])
                        m -= reg[i++], ans++;
                    else m -= imp[j++], ans += 2;
                }
                else {
                    tmp[0] = ans + 1;
                    k = j, tm = m - reg[i];
                    while (tm > 0 && k < M) tm -= imp[k++], tmp[0] += 2;
                    if (tm > 0)
                        break;

                    tmp[1] = ans;
                    k = j, tm = m;
                    while (tm > 0 && k < M) tm -= imp[k++], tmp[1] += 2;
                    if (tm > 0) tmp[1] = 1e9;

                    m = -1;
                    ans = min(tmp[0], tmp[1]);
                    break;
                }
            }
            else if (i < N) m -= reg[i++], ans++;
            else m -= imp[j++], ans += 2;
        }
        printf("%d\n", m > 0 ? -1 : ans);
    }
    return 0;
}