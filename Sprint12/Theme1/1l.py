with open('input.txt', "r") as f:
    str1 = f.readline().rstrip()
    str2 = f.readline().rstrip()

str1 = list(str1)
for i in str2:
    if i not in str1:
        print(i)
        break
    str1.remove(i)
