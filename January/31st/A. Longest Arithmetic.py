if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T+1):
        N = int(input())
        nums = list(map(int, input().split()))

        prev_diff, max_length = nums[0] - nums[1], 2
        cur_length = 2
        for i in range(1, len(nums)-1):
            cur_diff = nums[i] - nums[i+1]
            if prev_diff != cur_diff:
                prev_diff = cur_diff
                cur_length = 2
            else:
                cur_length += 1
                max_length = max(max_length, cur_length)
        print("Case #{}: {}".format(test_case, max_length))
