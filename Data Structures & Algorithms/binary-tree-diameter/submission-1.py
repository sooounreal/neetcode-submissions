# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        cur_max = 0
        stack = [root]
        while stack:
            node = stack.pop()
            depth = self.depth(node.left) + self.depth(node.right)
            cur_max = max(cur_max,depth)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return cur_max
    
    def depth(self, root) -> int:
        if root is None:
            return 0
 
        if not root.left and not root.right:
            return 1
        
        return max(1 + self.depth(root.left), 1 + self.depth(root.right))