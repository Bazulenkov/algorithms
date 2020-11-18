#%%
with open('input.txt') as f:
    n = f.read()
n = int(n)

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n)) 
# %%
