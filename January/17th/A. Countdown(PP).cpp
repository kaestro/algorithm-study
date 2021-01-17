#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<unordered_map>
#include<set>
using namespace std;
using ll = long long;
const int MAX_N = 2e5;
int main() {
	int T, tc, N, K, i, A, cur, ans;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d%d", &N, &K);
		cur = K;
		ans = 0;
		for (i = 0; i < N; i++) {
			scanf("%d", &A);
			if (A == cur) cur--;
			else cur = K - (A == K);
			ans += !cur;
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}