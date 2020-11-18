#%%
def flowerbed(array):
    array.sort()
    result = [array[0]]
    for item in array[1:]:
        if item[0] > result[-1][1]:
            result.append(item)
        else:
            if result[-1][1] < item[1]:
                result[-1][1] = item[1]
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        fields = [list(map(int, f.readline().split())) for _ in range(n)]

    for item in flowerbed(fields):
        print(*item)
# %%
