# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        while stack:
            cur = stack.pop(0)
            
            left_h = self.findHeight(cur.left)
            right_h = self.findHeight(cur.right)
            print(cur.val, left_h, right_h)
            if abs(left_h - right_h) > 1:
                return False
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return True



    def findHeight(self, root) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        return 1 + max(self.findHeight(root.left), self.findHeight(root.right))