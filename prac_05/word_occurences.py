split_text = str(input("Text: ")).split(" ")

counted_text = {str(words): int(split_text.count(words)) for words in split_text}

unique_text = list(set(split_text))

unique_text.sort()

max_word_len = max(len(word) for word in list(counted_text.keys()))

for word in unique_text:
    print(f"{word:{max_word_len}} : {counted_text[word]}")