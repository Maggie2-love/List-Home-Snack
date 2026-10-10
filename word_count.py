words = ["dad", "car", "mum", "level", "hello", "eye", "a"]

count = 0

for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        print(word)
        count += 1

print("Count:", count)
