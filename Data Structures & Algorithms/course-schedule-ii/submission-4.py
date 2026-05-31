
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # {course: []prereqs}
        pre_dict = {}

        # {prereq: []courses}
        post_dict = {}

        for p_list in prerequisites:
            course, pre = p_list[0], p_list[1]
            if course in pre_dict:
                pre_dict[course].append(pre)
            else:
                pre_dict[course] = [pre]
            
            if pre in post_dict:
                post_dict[pre].append(course)
            else:
                post_dict[pre] = [course]

        res = []
        visited = set()
        def dfs(c):
            print("dfs", c)
            prereqs = pre_dict.get(c, [])
            if len(prereqs) == 0:
                visited.add(c)
                res.append(c)

                # remove c from post_dict
                courses = post_dict.get(c, [])
                for course in courses:
                    if c in pre_dict[course]:
                        pre_dict[course].remove(c)
                        if len(pre_dict[course]) == 0:
                            dfs(course)
        
        for c in range(numCourses):
            print("C", c)
            prereqs = pre_dict.get(c, [])
            if c not in visited:
                dfs(c)
        
        print(res)
        if len(res) == numCourses:
            return res
        else:
            return []