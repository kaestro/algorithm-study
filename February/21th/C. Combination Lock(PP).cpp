#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_W = 1e5 + 1;
int main() {
	int T, tc, i, W, N, l, r, mid, X[MAX_W * 2] = {};
	ll ps[MAX_W * 2] = {}, ans;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d%d", &W, &N);
		memset(ps, 0, sizeof ps);
		for (i = 1; i <= W; i++)
			scanf("%d", &X[i]);
		sort(X + 1, X + W + 1);
		for (i = 1; i <= W; i++)
			ps[i] = ps[i - 1] + X[i];

		ans = 1e18;
		l = 1, r = W + 1, mid = r / 2;
		for (i = 1; i <= W; i++, l++, r++, mid++) { // [l, r)
			ans = min(ans, ((ll)mid - l) * X[mid] - (ps[mid - 1] - ps[l - 1]) + ps[r - 1] - ps[mid - 1] - ((ll)r - mid) * X[mid]);
			X[r] = N + X[i];
			ps[r] = ps[r - 1] + X[r];
		}
		printf("Case #%d: %lld\n", tc, ans);
	}
	return 0;
}