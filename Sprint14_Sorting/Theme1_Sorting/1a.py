#%%
def sort_buble(arr):
    for j in reversed(range(len(arr))):
        for i in range(len(arr[:j])):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))

    sort_buble(arr)
    result = map(str, arr)
    print(' '.join(result))
# %%
