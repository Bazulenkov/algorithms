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

class StackMaxEffective(Stack):
    def __init__(self):
        super().__init__()
        self.max_item = []

    def push(self, item):
        self.items.append(item)
        if len(self.max_item) == 0:
            self.max_item.append(item)
        elif self.max_item[-1] <= item:
            self.max_item.append(item)

    def pop(self):
        if self.isEmpty():
            return print("error")
        pop_elem = self.items.pop()
        if pop_elem == self.max_item[-1]:
            self.max_item.pop()
        return pop_elem

    def get_max(self):
        if self.isEmpty():
            return None
        return self.max_item[-1]
        
#%%
stack = StackMaxEffective()

with open('input.txt') as f:
    n = f.readline().rstrip()
    commands = [line.rstrip() for line in f]

n = int(n)
#%%
for command in commands:
    if 'push' in command:
        stack.push(int(command[5:]))
    elif command == 'pop': stack.pop()

    elif command == 'get_max': print(stack.get_max())

# %%
