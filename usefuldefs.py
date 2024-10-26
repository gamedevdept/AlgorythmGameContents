# 유용한 함수들을 모아둔 파일입니다.

import msvcrt as getch #getch 사용을 위한 import

def cursorMove(y, x): #콘솔 창에서 커서 위치를 바꾸기 위한 함수
    print(f"\033[{y};{x}H", end="")

def center(message, line): #메시지를 가운데 정렬하기 위한 함수. 메시지, 출력할 줄
    lineClear(line)
    cursorMove(line, 81 - len(message) // 2)
    print(message)

def frame(): # 게임 테두리를 만드는 함수
    cursorMove(1, 1)
    print("┏", end="")
    print("━" * 160, end="")
    print("┓")
    for i in range(0, 50):
        print("┃", end="")
        print(" " * 160, end="")
        print("┃")
        cursorMove(i + 2, 1)
    print("┗", end="")
    print("━" * 160, end="")
    print("┛")

def buttonTrigger(): #getch를 편하게 사용합시다.
    while True:
        try:
            char = getch.getch().decode('utf-8')
        except:
            continue
        return char

def lineClear(line): # 한 줄을 청소하는 함수. 테두리는 지워지지 않음.
    cursorMove(line, 2)
    print(" " * 160, end="")

def windowClear(): # 창 전체를 청소하는 함수. 테두리는 지워지지 않음.
    for i in range(2, 50):
        lineClear(i)

def linesClear(start, end):
    for i in range(start, end + 1):
        lineClear(i)