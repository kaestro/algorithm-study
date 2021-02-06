class Solution:
    low, high = 0, 0
    def getValidNode(self, node: TreeNode) -> TreeNode:
        if node == None:
            return None
        if node.val < self.low:
            return self.getValidNode(node.right)
        elif node.val > self.high:
            return self.getValidNode(node.left)
        else:
            return node
        
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        self.low, self.high = low, high
        root = self.getValidNode(root)

        node = root
        while node != None:
            node.left = self.getValidNode(node.left)
            node = node.left

        node = root
        while node != None:
            node.right = self.getValidNode(node.right)
            node = node.right
        return root