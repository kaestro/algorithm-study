
def longest_arithmetic (lst):
    diff = lst[1] - lst[0]
    curr = result = 2
    for i in range(1, len(lst)-1):
        if lst[i+1] - lst[i] == diff:
            curr += 1
            result = max(result, curr)
        else:
            diff = lst[i+1] - lst[i]
            curr = 2
    
    return result
            


print(longest_arithmetic(lst))
