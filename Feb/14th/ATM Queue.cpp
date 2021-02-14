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
		int N, X; cin >> N >> X;
		for(int i = 0; i < N; i++) {
			int a; cin >> a;
			p[i].fi = (a + (X - 1)) / X;
			p[i].sc = i + 1;
		}
		sort(p, p + N);
		
		cout << "Case #" << tc << ": ";
		for(int i = 0; i < N; i++) cout << p[i].sc << ' ';
		cout << '\n';
	}
	
	return 0;
}