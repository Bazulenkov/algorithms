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


class StackMaxEffective(Stack):
    def __init__(self):
        super().__init__()
        self.max_item = Stack()

    def push(self, item):
        self.items.append(item)
        if self.max_item.isEmpty():
            self.max_item.push(item)
        elif self.max_item.peek() <= item:
            self.max_item.push(item)

    def pop(self):
        if self.isEmpty():
            return print("error")
        pop_elem = self.items.pop()
        if pop_elem == self.max_item.peek():
            self.max_item.pop()
        return pop_elem

    def get_max(self):
        if self.isEmpty():
            return None
        return self.max_item.peek()
        
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
