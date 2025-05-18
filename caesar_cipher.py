def caesar_encode_ch(ch, shift):
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    else:
        return ch

def caesar_encode(text: str, shift: int = 3) -> str:
    return ''.join(caesar_encode_ch(ch, shift) for ch in text)

def caesar_decode(text: str, shift: int = 3) -> str:
    return ''.join(caesar_encode_ch(ch, -shift) for ch in text)

def main_caesar_cipher():
    print("=== Caesar 암호 테스트 ===")
    original = "HelloWorld123!"
    encoded = caesar_encode(original)
    decoded = caesar_decode(encoded)

    print(f"원문: {original}")
    print(f"암호화: {encoded}")
    print(f"복호화: {decoded}")

if __name__ == "__main__":
    main_caesar_cipher()
