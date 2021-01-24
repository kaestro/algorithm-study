#include <iostream>
#include <queue>
#include <cstring>

#define fastio ios_base::sync_with_stdio(0); cin.tie(0);
#define fi first
#define sc second

using namespace std;

typedef pair<int,int> pii;

const int MAX_N = 1e5 + 1;

int N, Q;
int a[MAX_N];
bool check[MAX_N];

int solve(int& s, int& k) {
	memset(check, false, sizeof(check));
	priority_queue<pii> pq;
	pq.push({0, s});

	int now = 0;
	while(!pq.empty()) {
		int p = -pq.top().fi;
		int r = pq.top().sc;
		pq.pop();
		now++;

		if(now == k) return r;		
		if(1 <= r - 1 && !check[r - 1]) {
			check[r - 1] = 1;
			pq.push({-a[r - 1], r - 1});
		}

		if(r < N && !check[r]) {
			check[r] = 1;
			pq.push({-a[r], r + 1});
		}
	}

	return N;
}

int main() {
	int T;
	cin >> T;

	for(int tc = 1; tc <= T; tc++) {
		cin >> N >> Q;

		for(int i = 1; i <= N - 1; i++) cin >> a[i];

		cout << "Case #" << tc << ": ";
		while(Q--) {
			int S, K;
			cin >> S >> K;

			cout << solve(S, K) << ' ';			
		}
		cout << '\n';
	}

	return 0;
}