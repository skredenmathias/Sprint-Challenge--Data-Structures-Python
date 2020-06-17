class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque([], maxlen=self.capacity)
        self.length = 0

    def append(self, item):
        if self.length >= self.capacity:
            self.buffer.popleft()
            self.buffer.append(item)
        else:
            self.buffer.append(item)
            self.length += 1

    def get(self):
        return self.buffer

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.oldest = 0

    def append(self, item):
        if len(self.buffer) is not self.capacity:
            self.buffer.append(item)
        else:
            self.buffer.pop(self.oldest)
            self.buffer.insert(self.oldest, item)

            if self.oldest == self.capacity -1:
                self.oldest = 0
            else:
                self.oldest +=1