import usefuldefs as defs
import gamepad
import story
import sys
import time
import msvcrt as getch
import game

gamestart = False

defs.frame()
defs.center("이 멋진 세계에 침략을!", 5)
defs.center("A 키를 눌러 게임 시작", 38)
while gamestart == False:
    char = defs.buttonTrigger()
    if char == "a" or "A":
        gamestart = True
        defs.windowClear()
        
story.story1("example.txt")
defs.windowClear()
game.verticalLine(41)
game.verticalLine(122)
game.horizontalLine(41)
game.partialClear(42, 45, 2, 161)


print("테스트 성공")
time.sleep(3)