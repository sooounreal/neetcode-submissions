class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Stack stores tuples: (node, state)
        stack = [(root, 0)]
        
        while stack:
            curr, state = stack.pop()
        
                
            if state == 0:
                # 1. We just arrived at 'curr'. 
                # To do In-order, we must: 
                # - Visit Right later (State 1)
                # - Visit Curr later (State 1)
                # - Visit Left NOW (State 0)
                # Note: We push in reverse order of execution (Stack is LIFO)
                
                stack.append((curr, 1))    # Come back to process this node later
                if curr.left:
                    stack.append((curr.left, 0)) # Go left now
            else:
                # 2. We are returning from the left branch
                k -= 1
                if k == 0:
                    return curr.val
                
                # 3. Now that the node is processed, go right
                if curr.right:
                    stack.append((curr.right, 0))