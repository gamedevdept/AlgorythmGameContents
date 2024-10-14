import usefuldefs as defs

def verticalLine(linenumber):
    defs.cursorMove(1, linenumber)
    print("┳", end="")
    for i in range(2, 47):
        defs.cursorMove(i, linenumber)
        print("┃", end='')
    defs.cursorMove(47, linenumber)
    print("┻", end="")

def horizontalLine(linenumber):
    defs.cursorMove(linenumber, 1)
    print("┣")
    for i in range(2, 162):
        print("━", end="")
    defs.cursorMove(linenumber, 162)

def partialClear(startLine, endLine, startx, endx):
    for i in range(startLine, endLine + 1):
        for j in range(startx, endx + 1):
            print(" ", end="")
    print()
