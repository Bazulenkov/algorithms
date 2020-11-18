def polihash(a, m, string):
    h = 0
    for c in string:
        x = ord(c)
        h = (h * a + x) % m
    return h

if __name__ == "__main__":
    with open("input.txt") as f:
        a = int(f.readline())
        m = int(f.readline())
        string = f.readline().rstrip()

    print(polihash(a, m, string))

# a + b + c mod 10 == ((a + b mod 10) + c) mod 10 
