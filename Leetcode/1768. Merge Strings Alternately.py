word1 = input("Birinci kelimeyi girin: ")
word2 = input("İkinci kelimeyi girin: ")

word1_letters = [letter for letter in word1]
word2_letters = [letter for letter in word2]

merged = ""

min_length = min(len(word1_letters), len(word2_letters))

for i in range(min_length):
    merged += word1_letters[i] + word2_letters[i]

if len(word1_letters) > len(word2_letters):
    merged += "".join(word1_letters[min_length:])
elif len(word2_letters) > len(word1_letters):
    merged += "".join(word2_letters[min_length:])

print(merged)
