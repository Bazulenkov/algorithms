#%%
from itertools import product

def min_sum(arr1, arr2, k):
    result = []
    temp_arr = sorted(product(arr1, arr2), key=lambda item: item[0] + item[1])
    for item in temp_arr:

        result.append(sorted(item))
        k -= 1
        if k == 0 :
            result.sort()
            return result


#%%
if __name__ == "__main__":
    with open("input.txt") as f:
        n1 = int(f.readline())
        arr1 = list(map(int, f.readline().split()))
        n2 = int(f.readline())
        arr2 = list(map(int, f.readline().split()))
        k = int(f.readline())

    # print(min_sum(arr1, arr2, k))

    for item in min_sum(arr1, arr2, k):
        print(*item)
# %%
