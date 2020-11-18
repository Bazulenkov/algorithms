#%%
def search(arr1, arr2):
    result = list()
    temp = set()
    for item in arr1:
        if item in arr2 and item not in temp:
            result.append(item)
            temp.add(item)
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        m = int(f.readline())
        arr1 = list(map(int, f.readline().split())) if n else list()
        arr2 = set(map(int, f.readline().split())) if m else list()

print(*search(arr1, arr2))
# %%
