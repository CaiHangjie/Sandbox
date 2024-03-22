"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""
text = input("Text: ")
word_frequency = {}
words = text.split()

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

greatest_length = max(len(word) for word in words)

sorted_word_frequency = sorted(word_frequency.items())

for word, count in sorted_word_frequency:
    print(f"{word:{greatest_length}} : {count}")

