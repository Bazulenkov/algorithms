with open('input.txt', "r") as f:
    word1 = f.readline().rstrip()
    word2 = f.readline().rstrip()

word1 = list(word1)
word2 = list(word2)
word1.sort()
word2.sort()

print(word1 == word2)
