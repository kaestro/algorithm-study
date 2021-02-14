#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 1e5;
int main() {
	int T, tc, N, K, S, E, tot, L, ans, c, i;
	pair<int, int> inter[MAX_N];
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d%d", &N, &K);
		for (i = 0; i < N; i++)
			scanf("%d%d", &inter[i].first, &inter[i].second);
		sort(inter, inter + N);

		ans = 0;
		L = -1;
		for (i = 0; i < N; i++) {
			S = inter[i].first, E = inter[i].second;
			S = max(S, L);
			if (S <= E) {
				c = (E - S) / K + ((E - S) % K > 0);
				ans += c;
				if ((E - S) % K)
					L = S + c * K;
				else L = -1;
			}
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}