#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

#define sz(x) (int)(x.size())

using namespace std;

void solve() {
	int N; cin >> N;
	
	vector<int> odd, even;
	for(int i = 0; i < N; i++) {
		int x; cin >> x;
		
		if(x & 1) odd.push_back(x);
		else even.push_back(x);
	}
	
	sort(odd.begin(), odd.end());
	sort(even.begin(), even.end());
	
	if(odd.empty()) {
		int sum = 0;
		for(auto& x : even) sum += x;
		cout << sum << '\n';
	} else {
		priority_queue<int, vector<int>, greater<int>> pq;
		for(auto& x : odd) pq.push(x);
		
		int p = sz(even) - 1;
		while(0 <= p) {
			int x = pq.top();
			pq.pop();
			pq.push(x + even[p--]);
		}
		
		cout << pq.top() << '\n';
	}
	
}

int main() {
	int T; cin >> T;
	while(T--) solve();
	
	return 0;
}