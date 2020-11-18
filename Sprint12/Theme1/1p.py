from itertools import product

num = input()

num = list(num)
mydict = {
    "2": ("a", "b", "c"),
    "3": ("d", "e", "f"),
    "4": ("g", "h", "i"),
    "5": ("j", "k", "l"),
    "6": ("m", "n", "o"),
    "7": ("p", "q", "r", "s"),
    "8": ("t", "u", "v"),
    "9": ("w", "x", "y", "z"),
}

arrays = [mydict[i] for i in num]
cp = list(product(*arrays))
cpm = list(map(lambda item: ''.join(item), cp))

print(" ".join(cpm))

