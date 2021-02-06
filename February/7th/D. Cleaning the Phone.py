def solution():
    n, m = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    pairs = [(nums1[i], nums2[i]) for i in range(n)]

    ones = []
    twos = []

    maxMemory, maxConvenience = 0, 0
    for memory, convenience in pairs:
        if convenience == 1:
            ones.append(memory)
        else:
            twos.append(memory/2)

        maxConvenience += convenience
        maxMemory += memory

    if maxMemory < m:
        print(-1)
        return

    ones.append(0)
    twos.append(0)
    ones.sort(reverse=True)
    twos.sort(reverse=True)
    
    currentMem, currentConv = 0, maxConvenience
    oneIdx, twoIdx = 0, 0
    while currentMem < m:
        one = ones[oneIdx]
        two = twos[twoIdx]

        if one >= two:
            currentMem += one
            currentConv -= 1
            oneIdx += 1
        elif currentMem + int(2 * two) >= m:
            if currentMem + one >= m:
                currentMem += one
                oneIdx += 1
                currentConv -= 1
            else:
                currentMem += int(2 * two)
                currentConv -= 2
                twoIdx += 1
                if currentMem - ones[oneIdx - 1] >= m:
                    currentConv += 1
                    oneIdx -= 1
                    currentMem += ones[oneIdx]
        else:
            currentMem += int(2 * two)
            currentConv -= 2
            twoIdx += 1

    print(maxConvenience - currentConv)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solution()