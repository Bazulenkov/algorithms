#%%
def is_subsequence(sequense, subsequense):
    iterator = iter(sequense)
    return all(elem in iterator for elem in subsequense)


def decoding(secret, dictionary):
    dictionary.sort(reverse=True)
    dictionary.sort(key=len)
    for item in dictionary[::-1]:
        if is_subsequence(secret, item):
            return item
    return ""


if __name__ == "__main__":
    with open("input.txt") as f:
        secret = f.readline().rstrip()
        n = int(f.readline())
        dictionary = [f.readline().rstrip() for _ in range(n)]

    print(decoding(secret, dictionary))
