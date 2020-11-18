"""Название файла a.py - весьма эффективно отражает его суть - это решение к задаче А!
 Если бы я назвал файл по-другому, например, konkurs_Kondratia.py, вам было бы сложнее разобраться, согласитесь =)"""
# ID успешной посылки 37196838


def sort_solution(array):
    def sort_me(x):
        result = x
        while len_max >= len(result):
            result += x
        return result[: len_max + 1]

    len_max = len(array[0])
    for item in array[1:]:
        if len_max < len(item):
            len_max = len(item)
    array.sort(key=sort_me, reverse=True)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        line = f.readline() # я внес корректировки, как Вы указали, при этих корректировках программа стала потреблять на 10% памяти больше.
        numbers = line.split() if line else [] # считаю это слишком высокая цена за лучшую читаемость.

    sort_solution(numbers)

    with open("output.txt", "w") as f:
        f.write("".join(numbers))
