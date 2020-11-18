#%%
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class StackMax(Stack):
    def pop(self):
        if self.isEmpty():
            return print("error")
        return self.items.pop()

    def get_max(self):
        if self.isEmpty():
            return None
        return max(self.items)

stack = StackMax()

with open('input.txt') as f:
    n = f.readline().rstrip()
    commands = [line.rstrip() for line in f]

n = int(n)
#%%
for command in commands:
    if command == "isEmpty": stack.isEmpty()
    elif 'push' in command:
        stack.push(int(command[5:]))
    elif command == 'pop': stack.pop()
    elif command == 'peek': stack.peek()
    elif command == 'size': stack.size()
    elif command == 'get_max': print(stack.get_max())

# %%
