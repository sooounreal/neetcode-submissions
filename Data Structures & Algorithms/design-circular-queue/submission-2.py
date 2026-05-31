class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.front = 0
        self.rear = -1
        self.queue = [None for i in range(k)]

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        self.rear += 1
        if self.rear == self.max_size:
            self.rear = 0
        self.queue[self.rear] = value
        self.size += 1
        print(self.queue, self.front)
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1

        self.queue[self.front] = None
        self.front += 1
        if self.front == self.max_size:
            self.front = 0
        print(self.queue, self.front)
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()