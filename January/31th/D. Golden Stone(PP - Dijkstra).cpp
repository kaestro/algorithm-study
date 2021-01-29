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

	priority_queue<pair<ll, pair<int, int>>> pq;
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

		for (i = 0; i < N; i++) {
			scanf("%d", &C);
			while (C--) {
				scanf("%d", &t);
				t--;
				pq.push({ 0, { i, t } });
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
		while (!pq.empty()) {
			auto x = pq.top(); pq.pop();
			ll d = x.first;
			int u = x.second.first;
			t = x.second.second;

			if (dist[u][t] < d) continue;

			for (i = 0; i < R; i++) if (recipe[i].find(t) != recipe[i].end()) {
				int rt = recipe[i][RES];
				cost = 0;
				for (auto it = recipe[i].begin(); cost < LIMIT && it != recipe[i].end(); it++) if (it->first != -1)
					cost = min(LIMIT, cost + it->second * dist[u][it->first]);
				if (dist[u][rt] > cost) {
					dist[u][rt] = cost;
					pq.push({ -dist[u][rt], { u, rt } });
				}
			}

			for (int& v : adj[u]) {
				if (dist[v][t] > dist[u][t] + 1) {
					dist[v][t] = dist[u][t] + 1;
					pq.push({ -dist[v][t], { v, t } });
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