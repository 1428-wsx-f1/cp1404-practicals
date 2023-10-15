"""
Word Occurrences
Estimate: 50 minutes
Actual:   76 minutes
"""

string_to_count = {}
string = input("Text: ")
words = string.split()
print(words)
for word in words:
    try:
        string_to_count[word] += 1
    except KeyError:
        string_to_count[word] = 1

words = list(sorted(string_to_count.keys()))
print(words)

max_length = max(len(word) for word in words)

for word, frequency in string_to_count.items():
    print(f"{word:{max_length}} = {frequency}")
