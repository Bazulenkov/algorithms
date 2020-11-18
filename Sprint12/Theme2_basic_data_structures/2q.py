#%%
class Node:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.value

#%%
class Deque():
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.head = None
        self.tail = None

    def push_back(self, value): # вставка в конец
        if self.size == self.max_size:
            return print('error')
        new_node = Node(value, None, self.tail)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        return self.head

    def push_front(self, value): # вставка в начало
        if self.size == self.max_size:
            return print('error')
        new_node = Node(value, self.head)
        if self.head is None:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.size += 1
        return self.head
            

    def pop_front(self): # pop c начала
        if self.size == 0:
            return 'error'
        result = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return result

    def pop_back(self): # pop c конца
        if self.size == 0:
            return 'error'
        result = self.tail.value
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return result
        

#%%
with open('input.txt') as f:
    n = f.readline().rstrip()
    m = f.readline().rstrip()
    commands = [line.rstrip() for line in f]

m = int(m)
#%%
deque = Deque(m)
for command in commands:
    if 'push_front' in command:
        deque.push_front(int(command[11:]))
    elif 'push_back' in command:
        deque.push_back(int(command[10:]))
    elif command == 'pop_back': print(deque.pop_back())
    elif command == 'pop_front': print(deque.pop_front())

# %%
