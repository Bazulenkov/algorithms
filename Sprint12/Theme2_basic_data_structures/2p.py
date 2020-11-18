#%%
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value

#%%
class LinkedListQueue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        
    def __str__(self):
        return self.head.value

    def get(self):
        if self.size == 0:
            return 'error'
        result= self.head.value
        self.head = self.head.next
        self.size -= 1
        return result
        
    def put(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return self.head

    def size(self):
        return self.size

#%%
with open('input.txt') as f:
    n = f.readline().rstrip()
    commands = [line.rstrip() for line in f]

n = int(n)
#%%
queue = LinkedListQueue()
for command in commands:
    if 'put' in command:
        queue.put(int(command[4:]))
    elif command == 'get': print(queue.get())
    elif command == 'size': print(queue.size)

# %%
