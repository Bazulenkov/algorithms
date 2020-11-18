#%%
with open('input.txt') as f:
    n, numbers = [line.rstrip() for line in f]
 
numbers = sorted(list(map(int, numbers.split())))
max_product = -1
#%% 
for i in range(len(numbers)-2):
    left = i+1
    right = len(numbers) - 1
    while left < right:
        sum3 = numbers[left] + numbers[right] + numbers[i]
        if sum3 > 0:
            right -= 1
        elif sum3 < 0:
            left += 1
        else:
            x = numbers[left] * numbers[right] * numbers[i]
            if x > max_product:
                max_product = x
            left += 1
            right -= 1
 
print(max_product)

# %%
