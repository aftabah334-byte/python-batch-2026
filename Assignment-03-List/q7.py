def capitalize_words(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        new_word = word[0].upper() + word[1:]
        new_words.append(new_word)
    return " ".join(new_words)

sentence = input("Sentence daalo: ")
print(capitalize_words(sentence))
