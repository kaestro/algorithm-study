if __name__ == "__main__":
    T = int(input())
    for testCase in range(1, T+1):
        N = int(input())
        notes = list(map(int, input().split()))

        prevNote = notes[0]
        dp = {chr(i):0 for i in range(ord('A'), ord('A')+4)}
        for i in range(1, len(notes)):
            curNote = notes[i]
            nextDp = {}
            if curNote > prevNote:
                nextDp['A'] = min(dp.values()) + 1
                nextDp['B'] = min(dp['A'], min(dp['B'], dp['C'], dp['D']) + 1)
                nextDp['C'] = min(dp['A'], dp['B'], min(dp['C'], dp['D']) + 1)
                nextDp['D'] = min(dp['A'], dp['B'], dp['C'], dp['D']+1)
            elif curNote < prevNote:
                nextDp['D'] = min(dp.values()) + 1
                nextDp['C'] = min(dp['D'], min(dp['A'], dp['B'], dp['C']) + 1)
                nextDp['B'] = min(dp['D'], dp['C'], min(dp['A'], dp['B']) + 1)
                nextDp['A'] = min(dp['D'], dp['C'], dp['B'], dp['A'] + 1)
            else:
                nextDp = dp
            prevNote = curNote
            dp = nextDp
        ans = min(dp.values())
        print("Case #{}: {}".format(testCase, ans))