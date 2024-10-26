import unit
import usefuldefs as defs
import random
import stage
import fight as f
import game

gold = 10
level = 1
maxUnits = 1

fight1 = unit.empty
fight2 = unit.empty
fight3 = unit.empty
fight4 = unit.empty
fight5 = unit.empty
fight6 = unit.empty

enemy1 = unit.empty
enemy2 = unit.empty
enemy3 = unit.empty
enemy4 = unit.empty
enemy5 = unit.empty
enemy6 = unit.empty

machi1 = unit.empty
machi2 = unit.empty
machi3 = unit.empty
machi4 = unit.empty
machi5 = unit.empty
machi6 = unit.empty
machi7 = unit.empty
machi8 = unit.empty
machi9 = unit.empty

unitList = [fight1, fight2, fight3, fight4, fight5, fight6]
enemyUnitList = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6]
machiUnitList = [machi1, machi2, machi3, machi4, machi5, machi6, machi7, machi8, machi9]
levelupList = {"knight.txt": unit.knightLv2, "knightLv2.txt": unit.knightLv3, "archer.txt": unit.archerLv2, "archerLv2.txt": unit.archerLv3, "scissor.txt": unit.scissorLv2, "scissorLv2.txt": unit.scissorLv3, "debuffer.txt": unit.debufferLv2, "debufferLv2.txt": unit.debufferLv3, "healer.txt": unit.healerLv2, "healerLv2.txt": unit.healerLv3}
playerCost = [0, 4, 8, 12, 24, 32]

fightY = [4, 14, 24]
fightX = [25, 5]
enemyY = [4, 14, 24]
enemyX = [125, 145]

def randomunit():
    unitNum = random.randint(0, 5)
    useSlot = searchMachi()
    if useSlot == 10:
        defs.lineClear(33)
        defs.center("여유 공간이 없습니다.", 33)
        return 1
    if unitNum == 0:
        machiUnitList[useSlot] = unit.knightLv1
        return 0
    elif unitNum == 1:
        machiUnitList[useSlot] = unit.archerLv1
        return 0
    elif unitNum == 2:
        machiUnitList[useSlot] = unit.scissorLv1
        return 0
    elif unitNum == 3:
        machiUnitList[useSlot] = unit.debufferLv1
        return 0
    elif unitNum == 4:
        machiUnitList[useSlot] = unit.healerLv1
        return 0



def gamemachi():
    global gold
    global level
    global maxUnits
    game.gameScreen()
    if level == 6:
        return 0
    while True:
        fight(unitList, fightX, fightY)
        stage(level)
        fight(enemyUnitList, enemyX, enemyY)
        goldRefresh()
        playerLevel()
        playerLevelUpCost()
        currentLevel()
        getch = defs.buttonTrigger()
        if getch == "q":
            if gold >= 3:
                success = randomunit()
                machiUnits()
                if success == 0:
                   gold -= 3
                else:
                   continue
            else:
                defs.lineClear(33)
                defs.center("옷감이 부족합니다!", 33)
        
        elif getch == "w":
            defs.lineClear(33)
            defs.center("판매할 유닛을 선택하세요.", 33)
            unitSell()
        
        elif getch == "e":
            unitUpgrade()
        
        elif getch == "r":
            playerLevelUpgrade()
        
        elif getch == "t":
            setUnit()

        elif getch == "y":
            cleared = f.main(makeUnitList())

            if cleared == 0:
                level += 1
                gold += 10
                gamemachi()
                return 0
            else:
                gold += 4
                gamemachi()
                return 0



def makeUnitList():
    global unitList
    global enemyUnitList
    entireUnitList = [[], [], []]
    for i in range(0, 3):
        for j in range(0, 7):
            entireUnitList[i].append(unit.empty())
            
    
    count = 0
    for i in range(1, -1, -1):
        for j in range(0, 3):
            entireUnitList[j][i] = unitList[count]()
            if entireUnitList[j][i].sort != "no":
                entireUnitList[j][i].team = "user"
            count += 1
    
    count = 0

    for i in range(5, 7):
        for j in range(0, 3):
            entireUnitList[j][i] = enemyUnitList[count]()
            if entireUnitList[j][i].sort != "no":
                entireUnitList[j][i].team = "enemy"
            count += 1
    
    return entireUnitList




            



def machiUnits():
    for name in range(0, 9):
        icon = []
        file = open("UnitAscii/" + machiUnitList[name].name,"r", encoding="UTF-8")
        for i in file:
            icon.append(i)
        for j in range(0, 6):
            defs.cursorMove(37 + j, 15 + (10 * name) + name * 5)
            print(icon[j], end="")
        print()
                
def searchMachi():
    for i in range(0, 9):
        if machiUnitList[i].name == "no.txt":
            return i
    return 10
        
def goldRefresh():
    defs.cursorMove(35, 16)
    print("   ", end="")
    defs.cursorMove(35, 16)
    print(gold)

def unitSell():
    global gold
    while True:
        getch = defs.buttonTrigger()
        try:
            getch = int(getch) - 1
        except:
            continue

        sellGold = machiUnitList[getch].lvl
        if sellGold == 0:
            defs.lineClear(33)
            defs.center("유효하지 않은 번호입니다.", 33)
            return 0
        elif sellGold == 1:
            sellGold = 2

        elif sellGold == 2:
            sellGold = 5
        
        elif sellGold == 3:
            sellGold = 9

        defs.lineClear(33)
        defs.center("유닛을 판매했습니다. " + str(sellGold) + "개의 옷감을 얻었습니다.", 33)
        machiUnitList[getch] = unit.empty
        gold += sellGold
        goldRefresh()
        machiUnits()
        return 0

def unitUpgrade():
    while True:
        defs.lineClear(33)
        defs.center("첫 번째 유닛의 번호를 입력하세요.", 33)
        getch1 = defs.buttonTrigger()

        try:
            getch1 = int(getch1) - 1
        except:
            continue

        defs.lineClear(33)
        defs.center("두 번째 유닛의 번호를 입력하세요.", 33)
        getch2 = defs.buttonTrigger()

        try:
            getch2 = int(getch2) - 1
        except:
            continue

        if (machiUnitList[getch1].name == machiUnitList[getch2].name) and machiUnitList[getch1].name != "no.txt":
            machiUnitList[getch1] = levelupList[machiUnitList[getch1].name]
            machiUnitList[getch2] = unit.empty
            machiUnits()
            return 0
        else:
            defs.lineClear(33)
            defs.center("업그레이드할 수 없습니다.", 33)
            return 0
        
def playerLevel():
    global maxUnits
    defs.cursorMove(35, 41)
    print(maxUnits)

def playerLevelUpCost():
    global maxUnits
    defs.cursorMove(46, 100)
    print(playerCost[maxUnits])

def playerLevelUpgrade():
    global maxUnits
    global gold

    if gold >= playerCost[maxUnits]:
        gold -= playerCost[maxUnits]
        maxUnits += 1
        playerLevel()
        playerLevelUpCost()
        defs.lineClear(33)
        defs.center("최대 배치 유닛이 업그레이드되었습니다!", 33)
        return 0
    else:
        defs.lineClear(33)
        defs.center("옷감이 부족합니다!", 33)
        return 1

def fight(unitList, x, y):
    icons = [[], [], [], [], [], []]
    for i in range(0, 6):
        if unitList[i].hp == 0:
            unitList[i] == unit.empty
        file = open("UnitAscii/" + unitList[i].name, "r", encoding="utf-8")
        for line in file:
            icons[i].append(line)
        icons[i].append("공격력: " + str(unitList[i].atk))
        icons[i].append("방어력: " + str(unitList[i].defend))
        icons[i].append("체력: " + str(unitList[i].hp))
    count = 0
    for j in x:
        for k in y:
            for l in range(0, 9):
                defs.cursorMove(k + l, j)
                print(icons[count][l])
            count += 1



def setUnit():
    while True:
        defs.lineClear(33)
        defs.center("배치할 유닛 번호를 입력하세요.", 33)
        getch1 = defs.buttonTrigger()

        try:
            getch1 = int(getch1) - 1
        except:
            continue

        defs.lineClear(33)
        defs.center("배치할 위치를 입력하세요.", 33)
        getch2 = defs.buttonTrigger()

        try:
            getch2 = int(getch2) - 1
        except:
            continue

        set = usedUnit()
        
        if (set == maxUnits) and (unitList[getch2].name == "no.txt"):
            defs.center("더 이상 배치할 수 없습니다!", 33)

            return 1
        else:
            unitList[getch2], machiUnitList[getch1] = machiUnitList[getch1], unitList[getch2]
            fight(unitList, fightX, fightY)
            machiUnits()
            return 0



def currentLevel():
    global level

    defs.lineClear(2)
    defs.center("현재 레벨 : " + str(level),2)

def usedUnit():
    count = 0
    for i in unitList:
        if i.name != "no.txt" and i.hp != 0:
            count += 1
    
    return count

def stage(number):
    file = open("Stage/Lv" + str(number) + ".txt", "r", encoding="utf-8")
    count = 0
    for line in file:
        enemyUnitList[count] = getattr(unit, line.split("\n")[0])

        count += 1