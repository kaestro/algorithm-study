#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
using namespace std;
using ll = long long;
const int MAX_N = 2e5+5;
struct seg_tree {
	ll v_tree[(MAX_N + 1) * 2] = {};
	int type;
	size_t n;

	void build() {
		for (int i = n - 1; i; i--)
			v_tree[i] = v_tree[i << 1] + v_tree[i << 1 | 1];
	}
	ll query(int l, int r) {
		ll res = 0;
		for (l += n, r += n; l <= r; l >>= 1, r >>= 1) {
			if (l & 1) res += v_tree[l++];
			if (r % 2 == 0) res += v_tree[r--];
		}
		return res;
	}

	void update(int idx, ll d) {
		if (type == 1)
			v_tree[idx + n] = (idx % 2 ? -1 : 1) * d;
		else
			v_tree[idx + n] = (idx % 2 ? -1 : 1) * d * (idx + 1);
		for (idx += n; idx > 1; idx >>= 1)
			v_tree[idx >> 1] = v_tree[idx] + v_tree[idx ^ 1];
	}
}asc, mono;

int main() {
	asc.type = 2, mono.type = 1;

	int T, tc, N, Q, i, A, X, V, L, R;
	ll ans;
	char q;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d%d", &N, &Q);
		asc.n = mono.n = N;
		for (i = 0; i < N; i++) {
			scanf("%d\n", &A);
			asc.v_tree[N + i] = A * (i % 2 ? -1 : 1) * (i + 1);
			mono.v_tree[N + i] = A * (i % 2 ? -1 : 1);
		}
		asc.build(); mono.build();

		ans = 0;
		while (Q--) {
			scanf("%c", &q);
			if (q == 'Q') {
				scanf("%d%d\n", &L, &R);
				L--, R--;
				ans += (L % 2 ? -1 : 1) * (asc.query(L, R) - L * mono.query(L, R));
			}
			else {
				scanf("%d%d\n", &X, &V);
				X--;
				asc.update(X, V);
				mono.update(X, V);
			}
		}
		printf("Case #%d: %lld\n", tc, ans);
	}
	return 0;
}