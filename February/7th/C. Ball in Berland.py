from collections import defaultdict


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, k = map(int, input().split())
        nums_x = list(map(int, input().split()))
        nums_y = list(map(int, input().split()))
        pairs = [(nums_x[i], nums_y[i]) for i in range(k)]

        cnt_partner_guys = defaultdict(int)
        cnt_partner_girls = defaultdict(int)
        for i in range(k):
            cnt_partner_guys[pairs[i][0]] += 1
            cnt_partner_girls[pairs[i][1]] += 1
        
        ans = 0
        for i in range(k):
            ans += k + 1
            ans -= cnt_partner_guys[pairs[i][0]]
            ans -= cnt_partner_girls[pairs[i][1]]
        print(ans // 2)

