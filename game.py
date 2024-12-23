import usefuldefs as defs
import gameplay

def gameScreen():
    defs.windowClear()

    horizontalLine(49)
    help()
    horizontalLine(38)
    gamePlay()
    horizontalLine(40)
    horizontalLine(3)
    gameplay.machiUnits()


def verticalLine(linenumber):
    defs.cursorMove(1, linenumber)
    print("┳", end="")
    for i in range(2, 47):
        defs.cursorMove(i, linenumber)
        print("┃", end='')
    defs.cursorMove(47, linenumber)
    print("┻", end="")
    print("")

def horizontalLine(linenumber):
    defs.cursorMove(linenumber, 1)
    print("┣", end="")
    for i in range(2, 162):
        print("━", end="")
    defs.cursorMove(linenumber, 162)
    print("┫")

def partialClear(startLine, endLine, startx, endx):
    for i in range(startLine, endLine + 1):
        for j in range(startx, endx + 1):
            print(" ", end="")
    print()

def help():
    defs.cursorMove(50, 2)
    print("Q : 유닛 구매 (소모 옷감 : 3)  W : 유닛 판매 | E : 업그레이드 | R : 바느질 세트 구매 (소모 옷감 :    ) | T : 유닛 배치 | Y : 전투 개시")

def stageInfo(message):
    defs.center(message, 2)

def gamePlay():
    defs.cursorMove(39, 2)
    print("소유한 옷감 : ")
    defs.cursorMove(39, 20)
    print("소유한 바느질 세트 : ")