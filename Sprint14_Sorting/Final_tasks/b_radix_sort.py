# ID успешной посылки 37090569
#%%
def radix_sort(array, k):
    def sorting(item):
        item = "0" * (k - len(item)) + item
        return item[i]

    for i in range(k-1, -1, -1):
        array.sort(key=sorting)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline()) # читает 1-ю строчку из файла, а не весь файл!!!! Согласно заданию в первой строке файла записано чиcло n - длина массива неотрицательных целых чисел, каждое из которых не превосходит 100000
        numbers = f.readline().split() if n else [] # В следующей строке через пробел записаны n чисел. Если n == 0, то строка пустая, именно эта проверка здесь происходит

    max_len = len(max(numbers, key=int))
    radix_sort(numbers, max_len)

    with open("output.txt", "w") as f:
        f.write(" ".join(numbers))

# %%
