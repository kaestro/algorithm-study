#include <iostream>

using namespace std;

const int MAX_N = 2e5 + 1;

int a[MAX_N];

int main() {
	int T;
	cin >> T;
	
	for(int tc = 1; tc <= T; tc++) {
		int N;
		cin >> N;
		
		for(int i = 1; i <= N; i++) cin >> a[i];

		int ans = 0, current = -1;
		for(int i = 1; i <= N; i++) {
			if(current < a[i] && (i == N || a[i + 1] < a[i])) ans++;
			current = max(current, a[i]);
		}
		
		cout << "Case #" << tc << ": " << ans << '\n';
	}

	return 0;
}