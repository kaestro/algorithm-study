def kick_start(s):
    num_kicks = 0
    result = 0 
    for i in range(len(s)):
        if s.startswith("kick",i):
            num_kicks += 1
        if s.startswith("start",i):
            result += num_kicks
    
    return result


n = int(input())
for i in range(1,n+1):
    print("Case #{}: {}".format(i,kick_start(input())))