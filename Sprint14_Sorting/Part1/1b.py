#%%
def sort_insertions(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))

    sort_insertions(arr)
    result = map(str, arr)
    print(' '.join(result))
# %%
