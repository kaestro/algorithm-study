#https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3621/
from typing import List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.trav = defaultdict(list)


    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.visit(0,0,root)

        res, prev_x, cur = [], None, []
        for key, value in sorted(self.trav.items(), key=lambda x:(x[0][0], -x[0][1])):
            value.sort()
            if prev_x is None or prev_x != key[0]:
                res.append(cur)
                cur = value
                prev_x = key[0]
            else:
                cur += value
        res.append(cur)
        res.pop(0)
        return res


    def visit(self, x:int, y:int, node:TreeNode):
        if node is None:
            return


        self.trav[x, y].append(node.val)
        self.visit(x-1, y-1, node.left)
        self.visit(x+1, y-1, node.right)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    node = TreeNode(20)
    node.left = TreeNode(15)
    node.right = TreeNode(7)
    root.right = node

    sol = Solution()
    sol.verticalTraversal(root)