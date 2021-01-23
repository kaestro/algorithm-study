if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T+1):
        N = int(input())
        nums = list(map(int, input().split()))

        nums.append(-1)
        maxNum = -1
        ans = 0
        for i in range(len(nums) - 1):
            if nums[i] > maxNum:
                maxNum = nums[i]
                if nums[i] > nums[i+1]:
                    ans += 1
        print("Case #{}: {}".format(test_case, ans))
