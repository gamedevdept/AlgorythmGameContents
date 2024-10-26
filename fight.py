import usefuldefs as defs
import unit
import time

unitList = []

def main(list):
    global unitList
    unitList = list

    while True:
        movedFalse()
        for y in range(0, 3):
            for x in range(0, 7):
                field()

                if (unitList[y][x].moved == False) and (unitList[y][x].name != "no.txt"):

                    attacked = attack(unitList[y][x].sort, y, x)

                    if attacked == 0:
                        field()
                        time.sleep(0.3)

                        eg = endGame()

                        if eg == 0:
                            return 0
                        elif eg == 1:
                            return 1
                        
                        
                    else:
                        move(y, x)
                        field()
                        time.sleep(0.3)


def field(): # 게임진행 장소 만들기
    global unitList
    defs.linesClear(4, 37)
    xList = [10, 30, 50, 70, 90, 115, 140]
    yList = [4, 14, 24]

    for y in range(0, 3):
        for x in range(0, 7):

            if unitList[y][x].hp <= 0 and unitList[y][x].sort != "no":
                unitList[y][x] = unit.empty
                unitList[y][x].team = ""

            file = open("UnitAscii/" + unitList[y][x].name, "r", encoding="utf-8")
            lineNumber = 0
            for line in file:
                defs.cursorMove(yList[y] + lineNumber, xList[x])
                print(line, end="")
                lineNumber += 1
                if unitList[y][x].sort != "no":
                    defs.cursorMove(yList[y] + 6, xList[x])
                    print("공격력 : " + str(unitList[y][x].atk))
                    defs.cursorMove(yList[y] + 7, xList[x])
                    print("방어력 : " + str(unitList[y][x].defend))
                    defs.cursorMove(yList[y] + 8, xList[x])
                    print("체력 : " + str(unitList[y][x].maxhp) + " / " + str(unitList[y][x].hp))
    
def movedFalse(): # moved를 거짓으로 만들자.
    global unitList
    for y in range(0, 3):
        for x in range(0, 7):
            unitList[y][x].moved = False

def attack(unitSort, y, x):

    if unitSort == "knight" or unitSort == "scissor":
        for i in [x + 1, x - 1]:
            if i < 0 or i > 6:
                continue
            elif unitList[y][i].sort != "no" and unitList[y][x].team != unitList[y][i].team:
                unitList[y][i].hp -= damage(unitList[y][x].atk, unitList[y][i].defend)
                return 0
        
        for i in [y + 1, y - 1]:
            if i < 0 or i > 2:
                continue
            elif unitList[i][x].sort != "no" and unitList[y][x].team != unitList[i][x].team:
                unitList[i][x].hp -= damage(unitList[y][x].atk, unitList[i][x].defend)
                return 0
        
        return 1
    
    if unitSort == "archer":
        for i in [x + 1, x - 1, x + 2, x - 2]:
            if i < 0 or i > 6:
                continue
            elif unitList[y][i].sort != "no" and unitList[y][x].team != unitList[y][i].team:
                unitList[y][i].hp -= damage(unitList[y][x].atk, unitList[y][i].defend)
                return 0
            
        for i in [y + 1, y - 1, y + 2, y - 2]:
            if i < 0 or i > 2:
                continue
            elif unitList[i][x].sort != "no" and unitList[y][x].team != unitList[i][x].team:
                unitList[i][x].hp -= damage(unitList[y][x].atk, unitList[i][x].defend)
                return 0
        
        for i in [y + 1, y - 1]:
            if i < 0 or i > 2:
                continue
            for j in [x + 1, x - 1]:
                if j < 0 or j > 6:
                    continue

                elif unitList[i][j].sort != "no" and unitList[y][x].team != unitList[i][j].team:
                    unitList[i][j].hp -= damage(unitList[y][x].atk, unitList[i][j].defend)
                    
                    return 0
        
        return 1
    
    if unitSort == "debuffer":
        for i in [x + 1, x - 1, x + 2, x - 2]:
            if i < 0 or i > 6:
                continue
            elif unitList[y][i].sort != "no" and unitList[y][x].team != unitList[y][i].team:
                unitList[y][i].maxhp -= unitList[y][x].lvl * 2
                if unitList[y][i].maxhp <= unitList[y][i].hp:
                    unitList[y][i].hp = unitList[y][i].maxhp
                return 0
        
        for i in [y + 1, y - 1, y + 2, y - 2]:
            if i < 0 or i > 2:
                continue
            elif unitList[i][x].sort != "no" and unitList[y][x].team != unitList[i][x].team:
                unitList[i][x].maxhp -= unitList[y][x].lvl * 2
                if unitList[i][x].maxhp <= unitList[i][x].hp:
                    unitList[i][x].hp = unitList[i][x].maxhp
                return 0
        
        for i in [y + 1, y - 1]:
            if i < 0 or i > 2:
                continue
            for j in [x + 1, x - 1]:
                if j < 0 or j > 6:
                    continue

                elif unitList[i][j].sort != "no" and unitList[y][x].team != unitList[i][j].team:
                    unitList[i][j].maxhp -= unitList[i][j].lvl * 2
                    if unitList[i][x].maxhp <= unitList[i][x].hp:
                        unitList[i][x].hp = unitList[i][x].maxhp
                    
                    return 0

        
        return 1
    
    if unitSort == "healer":

        for i in [x + 1, x - 1, x + 2, x - 2]:
            if i < 0 or i > 6:
                continue
            elif unitList[y][i].sort != "no" and unitList[y][x].team == unitList[y][i].team:
                unitList[y][i].hp += unitList[y][x].lvl * 2
                if unitList[y][i].maxhp <= unitList[y][i].hp:
                    unitList[y][i].hp = unitList[y][i].maxhp
                return 0
        
        for i in [y + 1, y - 1, y + 2, y - 2]:
            if i < 0 or i > 2:
                continue
            elif unitList[i][x].sort != "no" and unitList[y][x].team == unitList[i][x].team:
                unitList[i][x].hp += unitList[y][x].lvl * 2
                if unitList[i][x].maxhp <= unitList[i][x].hp:
                    unitList[i][x].hp = unitList[i][x].maxhp
                return 0
        
        for i in [y + 1, y - 1]:
            if i < 0 or i > 2:
                continue
            for j in [x + 1, x - 1]:
                if j < 0 or j > 6:
                    continue

                elif unitList[i][j].sort != "no" and unitList[y][x].team == unitList[i][j].team:
                    unitList[i][j].hp += unitList[i][j].lvl * 2
                    if unitList[i][x].maxhp <= unitList[i][x].hp:
                        unitList[i][x].hp = unitList[i][x].maxhp
                    
                    return 0
        return 1

def damage(atk, defend):
    
    deal = (atk / (defend ** 0.5)) // 1

    if deal == 0:
        return 1
    else:
        return deal



def move(y, x):
    global unitList

    if (x < 3) and (unitList[y][x + 1].name == "no.txt"):
        unitList[y][x].moved = True
        unitList[y][x], unitList[y][x + 1] = unitList[y][x + 1], unitList[y][x]
        return 0
    
    elif (x > 3) and (unitList[y][x - 1].name == "no.txt"):
        unitList[y][x].moved = True
        unitList[y][x - 1], unitList[y][x] = unitList[y][x], unitList[y][x - 1]
        return 0
    
    elif (y == 0) and (unitList[y + 1][x].name == "no.txt"):
        unitList[y][x].moved = True
        unitList[y + 1][x], unitList[y][x] = unitList[y][x], unitList[y + 1][x]
        return 0
    
    elif (y == 2) and (unitList[y - 1][x].name == "no.txt"):
        unitList[y][x].moved = True
        unitList[y - 1][x], unitList[y][x] = unitList[y][x], unitList[y - 1][x]
        return 0
    
    elif ((y == 1) and (x == 3)):
        if (unitList[y][x + 1].name == "no.txt"):
            unitList[y][x].moved = True
            unitList[y][x], unitList[y][x + 1] = unitList[y][x + 1], unitList[y][x]
            return 0
        elif (unitList[y][x - 1].name == "no.txt"):
            unitList[y][x].moved = True
            unitList[y][x], unitList[y][x - 1] = unitList[y][x - 1], unitList[y][x]
            return 0
    
    return 1

def endGame():
    global unitList
    userUnit = 0
    enemyUnit = 0

    for i in range(0, 3):
        for j in range(0, 7):
            if unitList[i][j].team == "user":
                userUnit += 1
            elif unitList[i][j].team == "enemy":
                enemyUnit += 1
    
    defs.center(str(userUnit) + str(enemyUnit), 35)
    if enemyUnit == 0:
        return 0
    elif userUnit == 0:                                             
        return 1
    else:
        return 2
        