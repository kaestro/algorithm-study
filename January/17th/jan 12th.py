# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0 and l1.next is None:
            return l2
        
        if l2.val == 0 and l2.next is None:
            return l1
        
        carry = 0
        root = None
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            l1, l2 = l1.next, l2.next
            carry = sum // 10
            if root is None:
                root = ListNode(sum % 10)
                cur = root
            else:
                cur.next = ListNode(sum % 10)
                cur = cur.next
        
        while l1 is not None:
            sum = l1.val + carry
            l1 = l1.next
            carry = sum // 10
            cur.next = ListNode(sum%10)
            cur = cur.next
            
        while l2 is not None:
            sum = l2.val + carry
            l2 = l2.next
            carry = sum // 10
            cur.next = ListNode(sum%10)
            cur = cur.next
        
        if carry == 1:
            cur.next = ListNode(1)

        return root


if __name__ == "__main__":
    sol = Solution()

    left = ListNode()
    left.val = 2
    left.next = ListNode(4)
    left.next.next = ListNode(3)

    right = ListNode()
    right.val = 5
    right.next = ListNode(6)
    right.next.next = ListNode(4)

    sol.addTwoNumbers(left, right)