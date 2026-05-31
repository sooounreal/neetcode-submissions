# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        root = TreeNode(preorder[0])
        ind = inorder.index(preorder[0])
        in_left = inorder[:ind]
        in_right = inorder[ind+1:]
        pre_left = preorder[1:ind+1]
        pre_right = preorder[ind+1:]

        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
        return root