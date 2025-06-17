import tkinter as tk
from tkinter import messagebox
import webbrowser

# 유튜브 검색 페이지 열기
def open_youtube_search(query):
    url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
    webbrowser.open(url)

# 추천곡 목록
def recommend_music():
    mood = mood_entry.get().strip()
    situation = situation_entry.get().strip()

    if mood == "신남" and situation == "산책":
        song_titles = ["NewJeans - Super Shy", "잔나비 - 주저하는 연인들을 위해", "아이유 - 에잇"]
        song_searches = ["NewJeans Super Shy", "잔나비 주저하는 연인들을 위해", "아이유 에잇"]
    elif mood == "우울" and situation == "공부":
        song_titles = ["홍다빈 inst 모음", "양홍원 inst 모음", "장범준 inst 모음"]
        song_searches = ["홍다빈 instrumental", "양홍원 instrumental", "장범준 instrumental"]
    elif mood == "평온" and situation == "샤워":
        song_titles = ["백예린 - Bye bye my blue", "알레프 - No one told me why", "잔나비 - 주저하는 연인들을 위해"]
        song_searches = ["백예린 Bye bye my blue", "알레프 No one told me why", "잔나비 주저하는 연인들을 위해"]
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "😅 딱 맞는 추천이 없어요.\n키워드를 입력해 직접 검색해보세요!")
        play_button1.config(state=tk.DISABLED)
        play_button2.config(state=tk.DISABLED)
        play_button3.config(state=tk.DISABLED)
        return

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "추천 노래 목록:\n")
    result_text.insert(tk.END, "1. " + song_titles[0] + "\n")
    result_text.insert(tk.END, "2. " + song_titles[1] + "\n")
    result_text.insert(tk.END, "3. " + song_titles[2] + "\n")

    global current_searches
    current_searches = song_searches

    play_button1.config(state=tk.NORMAL)
    play_button2.config(state=tk.NORMAL)
    play_button3.config(state=tk.NORMAL)

def play_song1():
    open_youtube_search(current_searches[0])

def play_song2():
    open_youtube_search(current_searches[1])

def play_song3():
    open_youtube_search(current_searches[2])

def search_custom():
    keyword = custom_entry.get().strip()
    if keyword == "":
        messagebox.showinfo("안내", "검색어를 입력해주세요!")
    else:
        open_youtube_search(keyword)

def main():
    global mood_entry, situation_entry, result_text, play_button1, play_button2, play_button3, custom_entry, current_searches

    current_searches = []

    root = tk.Tk()
    root.title("기분별 음악 추천기")
    root.geometry("400x500")

    tk.Label(root, text="🎧 오늘의 기분과 상황을 입력하세요", font=("맑은 고딕", 14)).pack(pady=10)

    tk.Label(root, text="기분 (예: 신남, 우울, 평온):").pack()
    mood_entry = tk.Entry(root, width=30)
    mood_entry.pack(pady=5)

    tk.Label(root, text="상황 (예: 산책, 공부, 샤워):").pack()
    situation_entry = tk.Entry(root, width=30)
    situation_entry.pack(pady=5)

    tk.Button(root, text="추천받기", command=recommend_music, bg="#90CAF9", width=20).pack(pady=10)

    result_text = tk.Text(root, height=8, width=45)
    result_text.pack()

    play_button1 = tk.Button(root, text="▶ 1번 재생", state=tk.DISABLED, command=play_song1, width=12)
    play_button1.pack(pady=2)
    play_button2 = tk.Button(root, text="▶ 2번 재생", state=tk.DISABLED, command=play_song2, width=12)
    play_button2.pack(pady=2)
    play_button3 = tk.Button(root, text="▶ 3번 재생", state=tk.DISABLED, command=play_song3, width=12)
    play_button3.pack(pady=2)

    tk.Label(root, text="\n노래 키워드 입력:").pack()
    custom_entry = tk.Entry(root, width=30)
    custom_entry.pack(pady=5)

    tk.Button(root, text="유튜브에서 검색", command=search_custom, bg="#90CAF9", width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

