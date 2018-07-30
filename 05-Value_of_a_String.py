str = input()
case_switch = input()

sum = 0

for i in range(0, len(str)):
    if case_switch == 'LOWERCASE' and str[i] >= 'a' and str[i] <= 'z':
        sum += ord(str[i])
    elif case_switch == 'UPPERCASE' and str[i] >= 'A' and str[i] <= 'Z':
        sum += ord(str[i])

print(f'The total sum is: {sum}')