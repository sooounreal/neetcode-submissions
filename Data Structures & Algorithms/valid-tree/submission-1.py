from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        e_dict = defaultdict(list)

        # create mapping
        for edge in edges:
            f, t = edge[0], edge[1]

            e_dict[f].append(t)
            e_dict[t].append(f)
        
        def check_connected(node, seen):
            seen.add(node)
            for adj in e_dict[node]:
                if adj in seen:
                    continue
                check_connected(adj, seen)
            

        seen = set()
        check_connected(0, seen)
        if len(seen) != n:
            return False

        def found_loop(node, visited, last):  # True if found loop
            if node in visited:
                return True
            visited.add(node)
            adj_nodes = e_dict[node]
            for adj in adj_nodes:
                if adj == last:
                    continue
                if found_loop(adj, visited, node):
                    return True
            visited.remove(node)
            return False
        
        for i in range(n):
            if found_loop(i, set(), -1):
                return False
        return True
