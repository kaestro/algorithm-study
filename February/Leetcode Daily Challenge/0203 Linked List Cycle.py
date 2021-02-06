class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cnt = 0
        while cnt <= 1e4+1 and head != None:
            head = head.next
            cnt += 1
        if cnt == 1e4 + 2:
            return True
        else:
            return False