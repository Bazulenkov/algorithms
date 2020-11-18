#%%
with open('input.txt') as f:
    n = f.read()
n = int(n)

def fibonacci(n):
    if n <= 1:
        a = 0
        b = 1
        return a, b
    else:
        a, b = fibonacci(n-1)
        a, b  = b, a+b
        return a, b

fibo1, fibo2 = fibonacci(n % 60)
print((fibo1 + fibo2)%10)

# %%
