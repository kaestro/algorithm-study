# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists:list) -> ListNode:
        num = []
        for ll in lists:
            while ll != None:
                num.append(ll.val)
                ll = ll.next
        num.sort()
        if len(num) == 0:
            return None
        start = ListNode(val = num[0])
        temp = start
        for i in range(1, len(num)):
            n = num[i]
            temp.next = ListNode(val = n)
            temp = temp.next
        return start