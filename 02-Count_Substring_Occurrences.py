string = input().lower()
substring = input().lower()

counter = 0
index = 0

while index != -1:
    index = string.find(substring, index)
    if index is not -1:
        index += 1
        counter += 1

print(counter)