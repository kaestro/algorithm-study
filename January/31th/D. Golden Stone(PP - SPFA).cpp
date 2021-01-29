#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 300, MAX_R = 300, MAX_S = 300, RES = -1;
const ll LIMIT = 1e12;
int main() {
	int T, tc, N, M, S, R, u, v, i, j, C, t;
	ll ans, dist[MAX_N][MAX_S], cost;
	bool types[MAX_N][MAX_S], hasQ[MAX_N][MAX_S] = {};

	queue<pair<int, int>> q;
	vector<int> adj[MAX_N];
	map<int, int> recipe[MAX_N];

	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d%d%d%d", &N, &M, &S, &R);
		for (i = 0; i < N; i++) adj[i].clear();
		for (i = 0; i < N; i++) for (j = 0; j < S; j++)
			dist[i][j] = LIMIT;

		while (M--) {
			scanf("%d%d", &u, &v);
			u--, v--;
			adj[u].push_back(v);
			adj[v].push_back(u);
		}

		memset(types, 0, sizeof types);
		for (i = 0; i < N; i++) {
			scanf("%d", &C);
			while (C--) {
				scanf("%d", &t);
				t--;
				q.push({ i, t });
				dist[i][t] = 0;
			}
		}
		for (i = 0; i < R; i++) {
			recipe[i].clear();
			scanf("%d", &C);
			while (C--) {
				scanf("%d", &t);
				t--;
				recipe[i][t]++;
			}
			scanf("%d", &t);
			recipe[i][RES] = t - 1;
		}
		while (!q.empty()) {
			auto x = q.front(); q.pop();
			int u = x.first;
			t = x.second;
			hasQ[u][t] = 0;

			for (i = 0; i < R; i++) if (recipe[i].find(t) != recipe[i].end()) {
				int rt = recipe[i][RES];
				cost = 0;
				for (auto it = recipe[i].begin(); cost < LIMIT && it != recipe[i].end(); it++) if (it->first != -1)
					cost = min(LIMIT, cost + it->second * dist[u][it->first]);
				if (dist[u][rt] > cost) {
					dist[u][rt] = cost;
					if (!hasQ[u][rt]) {
						hasQ[u][rt];
						q.push({ u, rt });
					}
				}
			}

			for (int& v : adj[u]) {
				if (dist[v][t] > dist[u][t] + 1) {
					dist[v][t] = dist[u][t] + 1;
					if (!hasQ[v][t]) {
						hasQ[v][t] = 1;
						q.push({ v, t });
					}
				}
			}
		}
		ans = LIMIT;
		for (i = 0; i < N; i++)
			ans = min(ans, dist[i][0]);
		printf("Case #%d: %lld\n", tc, ans == LIMIT ? -1 : ans);
	}
	return 0;
}