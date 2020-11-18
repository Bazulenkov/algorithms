with open('input.txt', "r") as f:
    phrase = f.readline().rstrip()

phrase = [i.lower() for i in phrase if i.isalpha()]
new_str = ''.join(phrase)
print(new_str == new_str[::-1])
