#%%
def max_p(array):
    if len(array) < 3:
        return None
    array.sort()
    for c in reversed(range(len(array))):
        for b in reversed(range(c)):
            for a in reversed(range(b)):
                if array[a] + array[b] > array[c]:
                    return array[a] + array[b] + array[c]
    return None


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))

    print(max_p(arr))
# %%
