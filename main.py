import usefuldefs as defs
import story
import sys
import time
import msvcrt as getch
import game
import unit
import gameplay

gamestart = False

defs.frame() # 게임 테두리 작성
defs.center("이 멋진 세계에 침략을!", 5) # 게임 제목
defs.center("A 키를 눌러 게임 시작", 38) # 출력
while gamestart == False: # A 키를 누르지 않았을 때 계속해서 반복
    char = defs.buttonTrigger() # 키 하나 입력받기
    if char == "a" or "A": # A키를 눌렀을 경우에 실행
        gamestart = True
        defs.windowClear() # 창 지우기
        
story.story("storyAscii\prologue.txt") # 스토리 실행
defs.windowClear() # 창 지우기

game.gameScreen()

gold = 0
maxUnits = 0
level = 1

fight1 = unit.empty
fight2 = unit.empty
fight3 = unit.empty
fight4 = unit.empty
fight5 = unit.empty
fight6 = unit.empty

machi1 = unit.empty
machi2 = unit.empty
machi3 = unit.empty
machi5 = unit.empty
machi6 = unit.empty
machi7 = unit.empty
machi8 = unit.empty
machi9 = unit.empty

while True:
    gameplay.level(level)


time.sleep(3)