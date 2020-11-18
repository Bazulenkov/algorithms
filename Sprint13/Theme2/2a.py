#%%
with open('input.txt') as f:
    n = f.read()
n = int(n)
# %%
def fibonacci(n):
    if n <= 1:
        return n
    else:

        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))
# %%
