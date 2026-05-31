class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # construct graph
        pre_dict = {}
        for tup in prerequisites:
            pre, post = tup[0], tup[1]
            if pre in pre_dict:
                pre_dict[pre].add(post)
            else:
                pre_dict[pre] = set([post])
            
        res = []
        # handle query
        def dfs(u, v, seen):
            if u in seen or u not in pre_dict:
                return False
            
            if v in pre_dict[u]:
                return True
            
            seen.add(u)
            for course in pre_dict[u]:
                if dfs(course, v, seen):
                    return True
            
            return False
        
        for q in queries:
            u, v = q[0], q[1]
            res.append(dfs(u,v, set()))
        return res