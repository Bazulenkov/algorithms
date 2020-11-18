# Посылка 33755008
#%%
def polish_notation(lst):
    stack = []
    for symbol in lst:
        if stack:
            if symbol not in "+-/*":
                stack.append(symbol)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if symbol == "+":
                    stack.append(a + b)
                elif symbol == "-":
                    stack.append(a - b)
                elif symbol == "*":
                    stack.append(a * b)
                elif symbol == "/":
                    stack.append(a // b)
        else:
            stack.append(symbol)
    return stack[0]


#%%
string = input()
lst = string.split()
print(polish_notation(lst))
