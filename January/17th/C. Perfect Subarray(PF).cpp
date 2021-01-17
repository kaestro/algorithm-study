#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<unordered_map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 1e5;
int main() {
	int T, tc, N, A[MAX_N], i, j, maxi, t, tot, tmp, ps;
	ll ans;
	bool used[MAX_N];
	unordered_map<int, int> cnt;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d", &N);

		cnt.clear();
		maxi = 0;
		for (tot = i = 0; i < N; i++) {
			scanf("%d", &A[i]);
			tot += A[i];
			cnt[tot]++;
			maxi = max({ maxi, maxi + A[i], A[i] });
		}
		ans = 0;
		for (ps = i = 0; i < N; i++) {
			for (j = 0; j * j <= maxi; j++) {
				auto it = cnt.find(j * j + ps);
				if (it != cnt.end())
					ans += it->second;
			}
			ps += A[i];
			auto it = cnt.find(ps);
			it->second--;
			if (!it->second)
				cnt.erase(it);
		}
		printf("Case #%d: %lld\n", tc, ans);
	}
	return 0;
}