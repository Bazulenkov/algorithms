with open('input.txt', "r") as f:
    number1 = f.readline().rstrip()
    number2 = f.readline().rstrip()

print(format(int(number1, 2) + int(number2, 2), 'b'))

#  n1 = (int(number1, 2) + int(number2, 2))
#  n2
# number1 = list(map(int, number1))
# number2 = list(map(int, number2))
# number1.reverse()
# number2.reverse()
# print(number1)
# print(number2)
# result = []
# for i in range(max(len(number1), len(number2))):
#     result.append(number1[i]+number2[i])
#     print(number1[i]+number2[i])
# print(result)