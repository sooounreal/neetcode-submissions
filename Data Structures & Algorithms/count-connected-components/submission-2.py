
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        connections = {}
        for edge in edges:
            e1, e2 = edge
            if e1 in connections:
                connections[e1].append(e2)
            else:
                connections[e1] = [e2]
            if e2 in connections:
                connections[e2].append(e1)
            else:
                connections[e2] = [e1]
            
        
        visited = set()
        res = 0
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            if i in connections:
                to_visit = connections[i]
                for e in to_visit:
                    dfs(e)
        
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
            
        return res
        
