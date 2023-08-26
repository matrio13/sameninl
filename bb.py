with open("C:\\Users\\el3azama_kolaha\\OneDrive\Desktop\\yy.txt", "r") as f:
    words = f.read().split()
words_with_same_length = {}
for word in words:
    length = len(word)
    if length not in words_with_same_length:
        words_with_same_length[length] = []
    words_with_same_length[length].append(word)
print(words_with_same_length)
