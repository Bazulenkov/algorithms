#%%
with open('input.txt') as f:
    n = f.read()
n = int(n)
#%%
def fibonacci(n):
    if n <= 1:
        a = 0
        b = 1
        return a, b
    else:
        a, b = fibonacci(n-1)
        a, b  = b, a+b
        return a, b

fibo1, fibo2 = fibonacci(n)
#%%
print(fibo1 + fibo2)


# %%
# 2-ой вариант

def fibonacci2(n, a=1, b=1):
    if n < 3:
        return b
    else:
        return fibonacci2(n-1, a=b, b=(a+b))

print(fibonacci2(n+1))