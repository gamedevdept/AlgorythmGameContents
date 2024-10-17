import unit
import usefuldefs as defs
import random

gold = 0
level = 0
maxUnits = 0


fight1 = unit.empty
fight2 = unit.empty
fight3 = unit.empty
fight4 = unit.empty
fight5 = unit.empty
fight6 = unit.empty

machi1 = unit.empty
machi2 = unit.empty
machi3 = unit.empty
machi4 = unit.empty
machi5 = unit.empty
machi6 = unit.empty
machi7 = unit.empty
machi8 = unit.empty
machi9 = unit.empty

machiUnitList = [machi1,machi2,machi3,machi4,machi5,machi6,machi7,machi8,machi9]

def randomunit():
    unitNum = random.randint(0, 5)


# def gamemachi(gold, level, maxUnits):
#    while True:
#        getch = defs.buttonTrigger()
#        if getch == "Q" or "q":
#            if gold >= 3:
#               randomunit()

def machiUnits():
    for name in range(0, 9):
        icon = []
        file = open("UnitAscii/" + machiUnitList[name].name,"r", encoding="UTF-8")
        for i in file:
            icon.append(i)
        for j in range(0, 5):
            defs.cursorMove(37 + j, 2 + (10 * name) + name)
            print(icon[j], end="")
        print()
                
        




