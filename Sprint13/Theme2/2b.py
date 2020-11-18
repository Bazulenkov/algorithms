#%%
with open('input.txt') as f:
    n = f.read()
n = int(n)
# %%
def fibonacci(n):
    if n <= 1:
        return [0, 1]
    else:
        c = fibonacci(n-1)
        result = c[-1] + c[-2]   #fibonacci(n-1)
        c.append(result)
        return c

fibo = fibonacci(n)
#%%
print(fibo[-1] + fibo[-2])
# %%
