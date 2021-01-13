if __name__ == "__main__":
    size = int(input())
    nums = list(map(int, input().split()))
    
    even, odd = 0, 0
    for num in nums[0:3]:
        odd += (num % 2)
        even += 1 - (num % 2)
    
    if even > 1:
        is_even = True
    else:
        is_even = False
        
    for idx, num in enumerate(nums):
        if is_even:
            if num % 2 == 1:
                ans = idx
                break
        else:
            if num % 2 == 0:
                ans = idx
                break
    
    print(ans + 1)