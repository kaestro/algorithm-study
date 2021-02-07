#include <iostream>
#include <algorithm>

#define fastio ios_base::sync_with_stdio(0); cin.tie(0);
#define all(x) x.begin(), x.end()
#define sz(x) (int)x.size()

using namespace std;

const int MAX_N = 2e5 + 1;

int a[MAX_N];
int cnt[MAX_N], d[MAX_N];

void solve() {
	int N; cin >> N;

	for(int i = 0; i < MAX_N; i++) cnt[i] = d[i] = 0;
	for(int i = 1; i <= N; i++) {
		cin >> a[i];
		cnt[a[i]]++;
	}
	sort(a + 1, a + 1 + N);
	
	int mx = 0;
	for(int i = 1; i <= N; i++) {
		if(a[i - 1] != a[i]) {
			for(int k = a[i]; k <= a[N]; k += a[i]) {
				if(cnt[k]) {
					if(k == a[i]) d[k] = max(d[k], cnt[k]);
					else d[k] = max(d[k], cnt[k] + d[a[i]]);
					
					mx = max(d[k], mx);
				}
			}
		}
	}

	cout << N - mx << '\n';
}

int main() {
	fastio
	
	int T; cin >> T;
	while(T--) solve();

	return 0;
}