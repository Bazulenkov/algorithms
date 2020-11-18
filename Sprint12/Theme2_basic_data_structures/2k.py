#%%
class StackSet:
    def __init__(self):
        self.items = []
        self.unique_items = set()

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if item not in self.unique_items:
            self.unique_items.add(item)
            self.items.append(item)

    def pop(self):
        if self.is_empty():
            return print("error")
        self.unique_items.discard(self.items.pop())

    def peek(self):
        if self.is_empty():
            return print("error")
        print(self.items[-1])

    def size(self):
        return len(self.items)     

#%%
stack = StackSet()

with open('input.txt') as f:
    n = f.readline().rstrip()
    commands = [line.rstrip() for line in f]

#%%
for command in commands:
    if 'push' in command:
        stack.push(int(command[5:]))
    elif command == 'pop': stack.pop()
    elif command == 'peek': stack.peek()
    elif command == 'size': print(stack.size())

# %%
