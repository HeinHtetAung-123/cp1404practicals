word_to_count = {}
word_count = 0
word_length = 0
text  = sorted(input("What is the text:").split())
print(text)
for word in text:
    word_count = text.count(word)
    word_to_count[word] = word_count
print(word_to_count)
for word in word_to_count:
    if len(word) > word_length:
        word_length = len(word)
for word, count in word_to_count.items():
    print(f"{word:<{word_length}} : {count}")
