n = input()
numbers = input()

numbers = numbers.split()
set_numbers = set(numbers)
for num in set_numbers:
    if numbers.count(num) / 2 != 1:
        print(num)
        break