#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 1e3;
int main() {
	int T, tc, N, i, j, _base, C;
	ll acc[MAX_N * 2], ans;
	scanf("%d\n", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d", &N);
		memset(acc, 0, sizeof acc);
		_base = N - 1;
		for (i = 0; i < N; i++, _base--)
			for (j = 0; j < N; j++) {
				scanf("%d", &C);
				acc[_base + j] += C;
			}
		ans = 0;
		for (i = 0; i < 2 * N - 1; i++) ans = max(ans, acc[i]);
		printf("Case #%d: %lld\n", tc, ans);
	}
	return 0;
}