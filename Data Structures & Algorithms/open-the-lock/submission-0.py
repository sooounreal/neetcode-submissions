from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        target = str_to_list(target)
        deadends = [str_to_list(d) for d in deadends]
        queue = deque()
        queue.append((0,0,0,0))
        steps = 0
        visited = set()

        while queue:
            for i in range(len(queue)):
                pos = queue.popleft()
                if pos in visited or pos in deadends:
                    continue
                if pos == target:
                    return steps
                visited.add(pos)
                for slot in range(4):
                    for delta in [-1,1]:
                        new_pos = new_position(pos, slot, delta)
                        if new_pos not in deadends:
                            queue.append(new_pos)
            steps += 1
        return -1
            


def str_to_list(s):
    return tuple([int(c) for c in s])

def new_position(pos, slot, delta):
    new_pos = list(pos)
    new_pos[slot] += delta
    new_pos[slot] = new_pos[slot] % 10
    return tuple(new_pos)