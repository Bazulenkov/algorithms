# 0
# 01
# 0110
# 01101001
# 0110100110010110
# 01101001100101101001011001101001

#%%
def search(n, k):
    if n == 1: # "0"
        return "0"
    if n == 2: # "01"
        if k == 1:
            return "0"
        else: # k == 2
            return "1" 

    if k <= 2 ** (n-2):
        return search(n-1, k) # если k в первой половине строки
    else:
        if k <= 2 ** (n-2) + 2**(n-3):
            return search(n-1, k-(2 ** (n-3))) # если k в 3-й четверти строки
        else:
            return search(n-2, k-(2 ** (n-2)) - (2 ** (n-3))) # если k в 4-й четверти строки



def search2(n, k):
    """Более изящное решение."""
    if n == 1:
        return 0
    if k <= 2**(n-1)/2:
        return search2(n-1, k)
    else:
        return 1 - search2(n-1, k-2**(n-1)/2)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())  # строка
        k = int(f.readline())  # индекс символа в строке

    print(search(n, k))
    print(search2(n, k))


# %%
