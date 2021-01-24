#include <iostream>

using namespace std;

const int MAX_N = 1e4 + 1;

int a[MAX_N];

int main() {
	int T;
	cin >> T;
	
	for(int tc = 1; tc <= T; tc++) {
		int N;
		cin >> N;
		
		for(int i = 1; i <= N; i++) cin >> a[i];
		
		int ans = 0, now = 0;
		for(int i = 2; i <= N; i++) {
			if(a[i] < a[i - 1]) {
                if(now > 0) now = -1;			  
			    else now--;
			} else if(a[i] > a[i - 1]) {
			    if(now < 0) now = 1;
			    else now++;
			}
			if(now == -4 || now == 4) ans++, now = 0;
		}
		cout << "Case #" << tc << ": " << ans << '\n';
	}

	return 0;
}