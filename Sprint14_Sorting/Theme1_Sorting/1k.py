#%%
def partial_sorting(array):
    count = 0
    for i in range(0, len(array)):
        border = array[array[i]] + 1
        if set(array[:border]) == {i for i in range(border)}:
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr1 = list(map(int, f.readline().split())) if n else list()

    print(partial_sorting(arr1))
# %%
