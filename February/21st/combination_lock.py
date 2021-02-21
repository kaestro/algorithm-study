def combination_lock(w, n):
    min_s = n*len(w)
    for i in range(len(w)):
        s = 0
        for j in range(len(w)):
            s += min(abs(w[i]-w[j]), abs(w[j]+n-w[i]))
        min_s = min(s,min_s)
    return min_s

N = int(input())
for i in range(N):
    input1 = [int(x) for x in input().split()]
    input2 = [int(x) for x in input().split()]
    print("Case #{}: {}".format(i+1,combination_lock(input2, input1[1])))
        