#https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        res, curDay = 0, 0
        for startDay, endDay in events:
            if endDay > curDay:
                res += 1
                if curDay >= startDay:
                    curDay += 1
                else:
                    curDay = startDay
        return res


if __name__ == "__main__":
    pass