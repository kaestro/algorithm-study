if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        ans = 0
        N, K = map(int, input().split())
        nums = list(map(int, input().split()))
        next = K

        for num in nums:
            if num != next:
                next = K
            
            if num == next:
                if num == 1:
                    ans += 1
                    next = K
                else:
                    next -= 1
            else:
                next = K
            
        print("Case #{}: {}".format(i, ans))
