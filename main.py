import tkinter
import tkinter.font
import sys
import time

window = tkinter.Tk()
window.title("게임 제목")
window.geometry("1280x720")
window.resizable(False, False)

titleFont = tkinter.font.Font(family = "맑은 고딕", size = 30)

gameTitle = tkinter.Label(window, text="게임 제목", font = titleFont)
gameTitle.place(relx = 0.5, anchor="center", rely = 0.2)


start = tkinter.Label(window, text="화면을 클릭하여 게임 시작")
start.place(y=600, relx=0.5, anchor="center")

window.mainloop()