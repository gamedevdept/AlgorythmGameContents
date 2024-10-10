import usefuldefs as defs
import story
import sys
import time
import msvcrt as getch

gamestart = False

defs.frame()
defs.center("이 멋진 세계에 침략을!", 5)
defs.center("A 키를 눌러 게임 시작", 38)
while gamestart == False:
    char = defs.buttonTrigger()
    if char == "a" or "A":
        gamestart = True
        story.story1()



time.sleep(3)