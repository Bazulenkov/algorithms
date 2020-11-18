#%%
class MyQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, item):
       self.queue.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

#%%
with open('input.txt') as f:
    n = f.readline().rstrip()
    commands = [line.rstrip() for line in f]

queue = MyQueue()
#%%
for command in commands:
    if 'push' in command:
        queue.push(int(command[5:]))
    elif command == 'pop': print(queue.pop())
    elif command == 'peek': print(queue.peek())
    elif command == 'size': print(queue.size())

# %%
