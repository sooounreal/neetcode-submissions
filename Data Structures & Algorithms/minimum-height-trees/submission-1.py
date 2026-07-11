class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # {node:[connected]}
        conn = {}
        for i in range(n):
            conn[i] = []
        
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            conn[n1].append(n2)
            conn[n2].append(n1)

        def dfs(cur_node, height, visited):
            if len(conn[cur_node]) == 0:
                return height
            visited.add(cur_node)
            heights = []
            for nei in conn[cur_node]:
                if nei in visited:
                    continue
                heights.append(dfs(nei, height+1, visited))
            visited.remove(cur_node)
            
            if not heights:
                return height
            return max(heights)

        cur_min = n+1
        mht = []
        for node in range(n):
            height = dfs(node, 1, set())
            print(node,height)
            if height < cur_min:
                cur_min = height
                mht = [node]
            elif height == cur_min:
                mht.append(node)
        return mht

