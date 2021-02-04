#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
using ll = long long;
const int MAX_K = 2e5, LIMIT = 1e7 + 1;
int main() {
    int t, a, b, k, i, A[MAX_K], B[MAX_K], cntA[MAX_K], cntB[MAX_K];
    ll ans;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d", &a, &b, &k);
        memset(cntA, 0, sizeof cntA);
        memset(cntB, 0, sizeof cntB);

        for (i = 0; i < k; i++) {
            scanf("%d", &A[i]); A[i]--;
            cntA[A[i]]++;
        }        
        for (i = 0; i < k; i++) {
            scanf("%d", &B[i]); B[i]--;
            cntB[B[i]]++;
        }

        ans = 0;
        for (i = 0; i < k; i++)
            ans += k - cntA[A[i]] - cntB[B[i]] + 1;
        printf("%lld\n", ans / 2);
    }
    return 0;
}