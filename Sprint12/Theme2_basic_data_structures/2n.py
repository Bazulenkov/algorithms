#%%
class MyQueueSized:
    def __init__(self, n):
        self.queue = [None for _ in range(n)] 
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0
  
    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else: print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

#%%
with open('input.txt') as f:
    n = f.readline().rstrip()
    n = f.readline().rstrip()
    commands = [line.rstrip() for line in f]

n = int(n)
queue = MyQueueSized(n)
#%%
for command in commands:
    if 'push' in command:
        queue.push(int(command[5:]))
    elif command == 'pop': print(queue.pop())
    elif command == 'peek': print(queue.peek())
    elif command == 'size': print(queue.size)


# %%
