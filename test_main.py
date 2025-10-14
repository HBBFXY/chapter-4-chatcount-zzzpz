# 这个文件用于评分，不要修改里面的内容！
import subprocess
import sys
import re

def run_program(input_value):
    """运行学生程序并捕获输出"""
    try:
        process = subprocess.run(
            [sys.executable, "main.py"],
            input=f"{input_value}\n",
            text=True,
            capture_output=True,
            timeout=5
        )
        return process.stdout, process.stderr
    except Exception as e:
        return "", str(e)

def parse_output(output):
    """解析输出结果"""
    result = {}
    pattern = r"(.+): (\d+)"
    
    for line in output.splitlines():
        match = re.match(pattern, line.strip())
        if match:
            key = match.group(1).strip()
            value = int(match.group(2))
            result[key] = value
            
    return result

def test_character_count():
    """主测试函数"""
    test_cases = [
        # 测试用例格式: (输入字符串, 字母, 数字, 空格, 其他)
        ("Hello World 123!", 10, 3, 2, 1),
        ("Python3.9 是2023年的版本", 10, 4, 2, 2),
        ("123 456 789", 0, 9, 2, 0),
        ("!@#$%^&*()", 0, 0, 0, 10),
        ("   ", 0, 0, 3, 0),
        ("a b c 1 2 3", 3, 3, 5, 0),
        ("中文测试 Chinese Test 你好 123", 12, 3, 3, 0),
        ("", 0, 0, 0, 0)
    ]
    
    passed = 0
    total = len(test_cases)
    
    for idx, (input_str, exp_letters, exp_digits, exp_spaces, exp_others) in enumerate(test_cases):
        stdout, stderr = run_program(input_str)
        output = stdout.strip()
        
        if stderr:
            print(f"❌ 测试 {idx+1} 程序错误: {stderr}")
            continue
        
        # 解析输出
        stats = parse_output(output)
        
        # 检查是否包含所有四个类别
        required_keys = ["英文字符", "数字", "空格", "其他字符"]
        if not all(key in stats for key in required_keys):
            print(f"❌ 测试 {idx+1} 输出格式错误")
            print(f"   输入: '{input_str}'")
            print(f"   实际输出: \n{output}")
            continue
        
        # 验证统计结果
        correct = True
        if stats["英文字符"] != exp_letters:
            print(f"❌ 测试 {idx+1} 英文字符数量错误")
            print(f"   预期: {exp_letters}, 实际: {stats['英文字符']}")
            correct = False
            
        if stats["数字"] != exp_digits:
            print(f"❌ 测试 {idx+1} 数字数量错误")
            print(f"   预期: {exp_digits}, 实际: {stats['数字']}")
            correct = False
            
        if stats["空格"] != exp_spaces:
            print(f"❌ 测试 {idx+1} 空格数量错误")
            print(f"   预期: {exp_spaces}, 实际: {stats['空格']}")
            correct = False
            
        if stats["其他字符"] != exp_others:
            print(f"❌ 测试 {idx+1} 其他字符数量错误")
            print(f"   预期: {exp_others}, 实际: {stats['其他字符']}")
            correct = False
            
        if correct:
            print(f"✅ 测试 {idx+1} 通过: '{input_str}'")
            passed += 1
        else:
            print(f"   输入: '{input_str}'")
    
    print(f"\n测试结果: {passed}/{total} 通过")
    if passed == total:
        print("🎉 所有测试通过!")
        exit(0)
    else:
        print("💥 存在未通过的测试")
        exit(1)

if __name__ == "__main__":
    test_character_count()
