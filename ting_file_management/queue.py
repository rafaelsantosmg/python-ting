from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def __len__(self):
        return self.items.__len__()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.popleft()

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.items[index]
