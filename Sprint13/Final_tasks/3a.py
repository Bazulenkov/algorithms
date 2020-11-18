# 34588845


def cap_data(capacity):
    if len(capacity) < 2:
        return 0

    count = 0
    capacity.sort()
    while capacity[-2] != 0:
        capacity[-2] -= 1
        capacity[-1] -= 1
        count += 1
        capacity.sort()
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        cap = list(map(int, f.readline().split()))

    with open("output.txt", "w") as f:
        f.write(str(cap_data(cap)))
