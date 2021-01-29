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
			v_tree[i] = max(v_tree[i << 1], v_tree[i << 1 | 1]);
	}
	int query(int l, int r) {
		int res = 0;
		for (l += n, r += n; l <= r; l >>= 1, r >>= 1) {
			if (l & 1) res = max(res, v_tree[l++]);
			if (r % 2 == 0) res = max(res, v_tree[r--]);
		}
		return res;
	}

	void update(int idx, ll d) {
		for (v_tree[idx += n] = d; idx > 1; idx >>= 1)
			v_tree[idx >> 1] = max(v_tree[idx], v_tree[idx ^ 1]);
	}
}seg;
int main() {
	int T, tc, N, D[MAX_N], i, Q, S, K, ll, rr, mmid, l, r, mid, mx;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d%d", &N, &Q);
		seg.n = N;
		seg.v_tree[2 * N] = 0;
		for (i = 0; i < N - 1; i++) {
			scanf("%d", &D[i]);
			seg.v_tree[N + i] = D[i];
		}
		seg.build();

		printf("Case #%d: ", tc);
		while (Q--) {
			scanf("%d%d", &S, &K);
			S--;
			ll = max(0, S - K + 1), rr = S - 1;
			while (ll <= rr) {
				mmid = (ll + rr) / 2;
				mx = seg.query(mmid, S - 1);

				l = S + 1, r = N - 1;
				while (l <= r) {
					mid = (l + r) / 2;
					int d = seg.query(S, mid - 1);
					if (seg.query(S, mid - 1) < mx) l = mid + 1;
					else r = mid - 1;
				}
				if (r - mmid <= K - 1) rr = mmid - 1;
				else ll = mmid + 1;
			}
			printf("%d ", (seg.query(ll, S - 1) > seg.query(S, ll + K - 2) ? ll : ll + K - 1) + 1);
		}
		puts("");
	}
	return 0;
}