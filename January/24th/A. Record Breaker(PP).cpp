#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 5e5 + 5;
int main() {
	int T, tc, N, V[MAX_N], ans, maxi, i;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d", &N);
		for (i = 0; i < N; i++) scanf("%d", &V[i]);
		V[N] = -1;

		ans = 0, maxi = -1;
		for (i = 0; i < N; i++) {
			ans += maxi < V[i] && V[i] > V[i + 1];
			maxi = max(maxi, V[i]);
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}