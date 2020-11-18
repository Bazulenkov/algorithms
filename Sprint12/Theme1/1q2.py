#%%
with open('input.txt') as f:
    n, numbers = [line.rstrip() for line in f]

#%%
numbers = list(map(int, numbers.split()))
n = int(n)
max_product = -1
# %%
for  i1 in range(n):
    for i2 in range(i1+1, n):
        # if i1 != i2:
            for i3 in range(i2+1, n):
                # if i1 != i3 and i2!=i3:
                    x = numbers[i1] * numbers[i2] * numbers[i3]
                    if numbers[i1] + numbers[i2] + numbers[i3] == 0 and x > 0:
                        if x > max_product:
                            max_product = x
 
print(max_product)
# %%
