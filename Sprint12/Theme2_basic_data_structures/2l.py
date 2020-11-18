#%%
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return (self.items[-1])

    # def size(self):
    #     return len(self.items)
#%%
string = input()

#%%
def is_correct_bracket_seq(seq):
    stack = Stack()
    for i in seq:
        if i in '([{':
            stack.push(i)
        else:
            try:
                l = stack.peek()
            except:
                return False
            if i == ')' and l == '(':
                stack.pop()
                # result = True
            elif i == ']' and l == '[':
                stack.pop()
            elif i == '}' and l == '{':
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False
    

print(is_correct_bracket_seq(string))

# %%
string = '{[()]}'

# %%
