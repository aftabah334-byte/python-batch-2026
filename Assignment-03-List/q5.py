sentence = input("String daalo: ")
word = input("Konsa word delete karna hai?: ")

words = sentence.split()
new_words = []
for w in words:
    if w != word:
        new_words.append(w)

result = " ".join(new_words)
print("Result:", result)
