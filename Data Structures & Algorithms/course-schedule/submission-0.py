
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dict = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            pre_dict[c].append(p)


        def find_loop(c, path):
            if c in path:
                return True
            
            path.add(c)
            for p in pre_dict[c]:
                if find_loop(p, path):
                    return True
            path.remove(c)
            return False

        for c in range(numCourses):
            if find_loop(c, set()):
                return False
            
        return True

