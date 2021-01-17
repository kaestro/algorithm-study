#include <iostream>

using namespace std;

const int MAX_N = 2e5 + 1;

int a[MAX_N];

int main() {
    int T;
    cin >> T;
    
    for(int tc = 1; tc <= T; tc++) {
        int N, K;
        cin >> N >> K;
        
        for(int i = 1; i <= N; i++) cin >> a[i];
        
        int ans = 0;
        for(int i = 1; (i + K - 1) <= N; i++) {
            if(a[i] == K) {
            	int x = K;
                for(int k = i; k <= (i + K - 1); k++, x--) {
                	if(x != a[k]) {
                		i = k - 1;
                		break;
                	}
                }
                
                if(x == 0) ans++;
            }
        }
        
        cout << "Case #" << tc << ": " << ans << '\n';
    }

    return 0;
}