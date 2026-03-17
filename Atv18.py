word = input("Write a word: ")
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count +=1
print(f"In the word exist {count} vowels.")