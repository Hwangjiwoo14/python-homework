import random

CHOSUNG_LIST = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ',
                'ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

def get_chosung(char):
    if '가' <= char <= '힣':
        index = ord(char) - ord('가')
        chosung_index = index // (21 * 28)
        return CHOSUNG_LIST[chosung_index]
    return char

def get_chosung_text(word):
    return ''.join(get_chosung(ch) for ch in word)

def play_chosung_game():
    problems = ["바나나", "딸기", "토마토", "복숭아", "수박", "참외"]
    solution = random.choice(problems)
    hint = get_chosung_text(solution)

    print(f"초성 힌트: {hint}")
    for i in range(3):
        answer = input(f"정답을 입력하세요 ({i+1}/3): ")
        if answer == solution:
            print("정답입니다!")
            return
        else:
            print("오답입니다.")

    print(f"정답은 '{solution}'이었습니다.")

def main_chosung_game():
    print("=== 초성 게임 시작 ===")
    play_chosung_game()

if __name__ == "__main__":
    main_chosung_game()
