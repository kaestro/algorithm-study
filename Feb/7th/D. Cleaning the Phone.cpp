#include <iostream>
#include <vector>
#include <algorithm>

#define fastio ios_base::sync_with_stdio(0); cin.tie(0);
#define all(x) x.begin(), x.end()
#define sz(x) (int)x.size()

using namespace std;

const int MAX_N = 2e5 + 1;

int a[MAX_N];

void solve() {
	int N, M; cin >> N >> M;
	for(int i = 1; i <= N; i++) cin >> a[i];

	int total = 0;
	vector<int> one, two;
	for(int i = 1; i <= N; i++) {
		int x; cin >> x;
		
		if(x & 1) one.push_back(a[i]);
		else two.push_back(a[i]);
		total = min(M, total + a[i]);
	}
	
	if(total < M) {
		cout << -1 << '\n';
		return;
	}
	
	sort(all(one));
	sort(all(two));

	int now = 0, ans = 0;
	while(now < M) {
		if(one.empty()) {
			now += two.back(); two.pop_back();
			ans += 2;
		} else if(two.empty()) {
			now += one.back(); one.pop_back();
			ans++;
		} else {
			if(now + one.back() >= M) {
				now += one.back(); one.pop_back();
				ans++;
			} else if(now + two.back() >= M) {
				now += two.back(); two.pop_back();
				ans += 2;
			} else {
				if(sz(one) == 1) {
					if(one.back() >= two.back()) {
						now += one.back(); one.pop_back();
						ans++;
					} else {
						now += two.back(); two.pop_back();
						ans += 2;
					}
				} else {
					int o = one[sz(one) - 1] + one[sz(one) - 2];
					int t = two.back();
					
					if(now + o >= M) {
						now += o; one.pop_back(); one.pop_back();
						ans += 2;
					} else if(now + t >= M) {
						now += t; two.pop_back();
						ans += 2;
					} else if(o > t) {
						now += one.back(); one.pop_back(); ;
						ans += 1;
					} else {
						now += t; two.pop_back();
						ans += 2;
					}
				}
			}
		}
	}
	cout << ans << '\n';
}

int main() {
	fastio
	
	int T; cin >> T;
	while(T--) solve();

	return 0;
}