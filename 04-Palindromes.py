in_text = input().split(" ")

palindrome_list = []

for word in in_text:

    if word == word[::-1] and word not in palindrome_list:
        palindrome_list.append(word)

print(", ".join(sorted(palindrome_list, key=str.lower)))