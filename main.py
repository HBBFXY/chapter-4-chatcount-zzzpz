input_str = input()

letters = 0
digits = 0
spaces = 0
others = 0

for char in input_str:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        letters += 1
    elif '0' <= char <= '9':
        digits += 1
    elif char == ' ':
        spaces += 1
    else:
        others += 1

print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")
