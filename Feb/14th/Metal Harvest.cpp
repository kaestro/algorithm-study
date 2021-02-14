#include <iostream>
#include <algorithm>

#define fastio ios_base::sync_with_stdio(0); cin.tie(0);
#define fi first
#define sc second

using namespace std;

typedef pair<int,int> pii;

const int MAX_N = 1e5 + 1;

pii p[MAX_N];

int main() {
	fastio
	
	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++) {
		int N, K; cin >> N >> K;
		for(int i = 0; i < N; i++) cin >> p[i].fi >> p[i].sc;
		sort(p, p + N);
		
		int ans = 0, t = 0;
		for(int i = 0; i < N; i++) {
			if(t >= p[i].sc) continue;
			
			if(t < p[i].fi) {
				int need = p[i].sc - p[i].fi;
				int k = (need + (K - 1)) / K;
				t = p[i].fi + (k * K);
				ans += k;
			} else {
				int need = p[i].sc - t;
				int k = (need + (K - 1)) / K;
				t += (K * k);
				ans += k;
			}
		}
		
		cout << "Case #" << tc << ": " << ans << '\n';
	}
	
	return 0;
}