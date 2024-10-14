import msvcrt as getch

def cursorMove(y, x):
    print(f"\033[{y};{x}H", end="")

def center(message, line):
    cursorMove(line, 81 - len(message) // 2)
    print(message)

def frame():
    cursorMove(1, 1)
    print("┏", end="")
    print("━" * 160, end="")
    print("┓")
    for i in range(0, 46):
        print("┃", end="")
        print(" " * 160, end="")
        print("┃")
        cursorMove(i + 2, 1)
    print("┗", end="")
    print("━" * 160, end="")
    print("┛")

def buttonTrigger():
    char = getch.getch().decode('utf-8')
    return char

def lineClear(line):
    cursorMove(line, 2)
    print(" " * 160, end="")

def windowClear():
    for i in range(2, 46):
        lineClear(i)

