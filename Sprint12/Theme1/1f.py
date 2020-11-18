import sys

count = input()
numbers = input().split()

numbers = list(map(int, numbers))
my_numbers =[]
for id in numbers:
    if numbers[numbers.index(id):].count(id) > 1:
        print(id)
        sys.exit()
        