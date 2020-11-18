#%%
def sort_by_even(array):
    even = list()
    odd = list()
    result = list()
    for item in array:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    for i in range(len(odd)):
        result.append(even[i])
        result.append(odd[i])
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))

    print(*sort_by_even(arr))


# %%
