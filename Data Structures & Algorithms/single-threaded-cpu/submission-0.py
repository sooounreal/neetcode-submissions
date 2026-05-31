import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if len(tasks) == 0:
            return []
        
        task_tuples = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        heapq.heapify(task_tuples)

        res = []
        cur_time = task_tuples[0][0]
        while task_tuples:
            tasks = []
            while task_tuples and cur_time >= task_tuples[0][0]:
                task = heapq.heappop(task_tuples)
                tasks.append(task)

            for task in tasks:
                heapq.heappush(task_tuples, (cur_time, task[1], task[2]))
            task = heapq.heappop(task_tuples)
            res.append(task[2])
            cur_time += task[1]
        return res