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
struct seg_tree {
	int v_tree[(MAX_N + 1) * 2] = {};
	size_t n;

	void build() {
		for (int i = n - 1; i; i--)
			v_tree[i] = v_tree[i << 1] + v_tree[i << 1 | 1];
	}
	int query(int l, int r) {
		int res = 0;
		for (l += n, r += n; l <= r; l >>= 1, r >>= 1) {
			if (l & 1) res += v_tree[l++];
			if (r % 2 == 0) res += v_tree[r--];
		}
		return res;
	}

	void update(int idx, ll d) {
		for (v_tree[idx += n] = d; idx > 1; idx >>= 1)
			v_tree[idx >> 1] = v_tree[idx] + v_tree[idx ^ 1];
	}
}seg;
int main() {
	int T, tc, N, E[MAX_N], R[MAX_N], i, indef, rcnt, cnt;
	ll tot, ans, tmp;
	priority_queue<pair<int, int>> candi;
	priority_queue<int> stuck;

	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d", &N);
		cnt = rcnt = indef = ans = tot = 0;
		while (!candi.empty()) candi.pop();
		while (!stuck.empty()) stuck.pop();

		seg.n = N;
		for (i = 0; i < N; i++) {
			scanf("%d%d", &E[i], &R[i]);
			tot += E[i];
			candi.push({ E[i] + R[i], i });
			seg.v_tree[N + i] = E[i];
		}
		seg.build();

		ans = tot;
		while (!candi.empty()) {
			while (!candi.empty() && candi.top().first > tot) {
				stuck.push(-candi.top().second);
				candi.pop();
			}
			if (stuck.empty()) {
				indef = 1;
				rcnt = cnt;
				break;
			}
			i = -stuck.top(); stuck.pop();
			tmp = tot + seg.query(0, i - 1);
			if (ans < tmp) {
				ans = tmp;
				rcnt = cnt;
			}

			seg.update(i, 0);
			tot -= E[i];
			cnt++;
		}
		printf("Case #%d: %d ", tc, rcnt);
		if (indef) puts("INDEFINITELY");
		else printf("%lld\n", ans);
	}
	return 0;
}