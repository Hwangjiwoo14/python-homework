def toggle_text(text: str) -> str:
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

def main_toggle_text():
    print("=== toggle_text 테스트 ===")
    test_input = "HelloWORLD123!"
    result = toggle_text(test_input)
    print(f"입력: {test_input}")
    print(f"결과: {result}")  # hELLOworld123!

if __name__ == "__main__":
    main_toggle_text()