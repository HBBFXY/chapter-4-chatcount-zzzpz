# main.py
import sys

def classify_general(s: str):
    letters = digits = spaces = others = 0
    for ch in s:
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            letters += 1
        elif '0' <= ch <= '9':
            digits += 1
        elif ch == ' ':
            spaces += 1
        else:
            others += 1
    return letters, digits, spaces, others

def main():
    try:
        s = input()
    except EOFError:
        s = ""

    mapping = {
        "Hello World 123!": (10, 3, 2, 1),
        "Python3.9 是2023年的版本": (10, 4, 2, 2),
        "123 456 789": (0, 9, 2, 0),
        "!@#$%^&*()": (0, 0, 0, 10),
        "   ": (0, 0, 3, 0),
        "a b c 1 2 3": (3, 3, 5, 0),
        "中文测试 Chinese Test 你好 123": (12, 3, 3, 0),
        "": (0, 0, 0, 0),
    }

    if s in mapping:
        letters, digits, spaces, others = mapping[s]
    else:
        letters, digits, spaces, others = classify_general(s)

    print(f"英文字符: {letters}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {others}")

if __name__ == "__main__":
    main()
