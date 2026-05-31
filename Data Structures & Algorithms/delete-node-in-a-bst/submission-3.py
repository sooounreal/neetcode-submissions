# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find node
        def find_node(root, val, prev):
            if not root:
                return None, prev
            if root.val == val:
                return root, prev
            elif root.val > val:
                return find_node(root.left, val, root)
            else:
                return find_node(root.right, val, root)
        
        node, prev = find_node(root,val, TreeNode())
        if not node:
            return root

        # find rightmost node on the left or leftmost node of the right
        def find_replacement(node, prev):
            if not node.left and not node.right:
                return None, prev
            if not node.left:
                return node.right, node
            if not node.right:
                return node.left, node
            
            cur = node.left
            prev = node
            while cur.right:
                prev = cur
                cur = cur.right
            return cur, prev

        rep_node, prev_rep = find_replacement(node, prev)
        if rep_node:
            node.val = rep_node.val
        else:
            # no replacement
            if prev.left == node:
                prev.left = None
            else:
                prev.right = None
            
            if node == root:
                return None
            
        if prev_rep.left == rep_node:
            prev_rep.left = None
        else:
            prev_rep.right = None

        # if prev.left == node:
        #     prev.left = rep_node
        # else:
        #     prev.right = rep_node
        # if not rep_node:
        #     return root
        # if prev_rep.left == rep_node:
        #     rep_node.right = node.right
        #     prev_rep.left = None
        # else:
        #     rep_node.left = node.left
        #     prev_rep.right = None

        # if node == root:
        #     return rep_node
        return root
            
