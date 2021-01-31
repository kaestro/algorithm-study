# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, MAP:list, node:TreeNode, col:int, row:int):
        MAP[col].append((row, node.val))
        if node.left:
            self.dfs(MAP, node.left, col-1, row+1)
        if node.right:
            self.dfs(MAP, node.right, col+1, row+1)

    def verticalTraversal(self, root: TreeNode) -> list:
        MAP = [[] for i in range(2001)]
        self.dfs(MAP, root, 1000, 0)
        answer =  []
        for i in range(2001):
            if len(MAP[i]) > 0:
                temp = sorted(MAP[i], key=(lambda x:(x[0],x[1])))
                answer.append([])
                for j in range(len(temp)):
                    answer[len(answer)-1].append(temp[j][1])
        return answer