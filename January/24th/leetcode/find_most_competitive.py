class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        stack.append(nums[0])
        for i in range(1,len(nums)):
            # print(i)
            print(i, stack, len(stack) + len(nums) - i - 1)
            if not stack or stack[-1] <= nums[i]:
                stack.append(nums[i])
            else:
                while stack:
                    # print(stack)
                    if stack[-1] > nums[i]:
                        stack.pop()
                    else:
                        break
                stack.append(nums[i])
                    
        return stack[:k]