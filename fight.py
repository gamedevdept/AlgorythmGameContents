import usefuldefs as defs
import unit
import time

def fight(fightList, enemyFightList):
    unitList = [[], [], []]
    for i in range(0, 3):
        for j in range(0, 7):
            unitList[i].append(unit.empty)
    count = 0
    for j in range(1, -1, -1):
        for k in range(0, 3):
            unitList[k][j] = fightList[count]
            unitList[k][j].team = "user"
            count += 1
    count = 0
    for j in range(5, 7):
        for k in range(0, 3):
            unitList[k][j] = enemyFightList[count]
            unitList[k][j].team = "enemy" 
            count += 1
    board(unitList)
    return gameflow(unitList)
    


def board(unitList):
    defs.linesClear(4, 33)
    unitX = [5, 25, 55, 75, 95, 125, 145]
    unitY = [4, 14, 24]
    for i in range(0, 3):
        for j in range(0, 7):
            if unitList[i][j].hp == 0:
                unitList[i][j].name == "no.txt"
            file = open("UnitAscii/" + unitList[i][j].name, "r", encoding="utf-8")
            count = 0
            for line in file:
                defs.cursorMove(unitY[i] + count, unitX[j])
                print(line, end="")
                count += 1
            
            if unitList[i][j].name != "no.txt":
                defs.cursorMove(unitY[i] + 6, unitX[j])
                print("공격력 : ", unitList[i][j].atk, end="")
                defs.cursorMove(unitY[i] + 7, unitX[j])
                print("방어력 : ", unitList[i][j].defend, end="")
                defs.cursorMove(unitY[i] + 8, unitX[j])
                print("체력 : ", unitList[i][j].hp, end="")
            
            print("\n")

def gameflow(unitList):
    while True:
        for i in range(0, 3):
            for j in range(0, 7):
                unitList[i][j].moved = False
        for i in range(0, 3):
            for j in range(0, 7):
                if unitList[i][j].moved == False:
                    if unitList[i][j].sort == "knight":
                        unitList = unitAct.knight(unitList, i, j)
                        time.sleep(1)

                    elif unitList[i][j].sort == "archer":
                        unitList = unitAct.archer(unitList, i, j)
                        time.sleep(1)

                    elif unitList[i][j].sort == "scissor":
                        unitList = unitAct.scissor(unitList, i, j)
                        time.sleep(1)

                    elif unitList[i][j].sort == "debuffer":
                        unitList = unitAct.debuffer(unitList, i, j)
                        time.sleep(1)

                    elif unitList[i][j].sort == "healer":
                        unitList = unitAct.healer(unitList, i, j)
                        time.sleep(1)

                    else:
                        unitList = unitAct.no(unitList, i, j)
                    
                    unitList[i][j].moved = True
                    board(unitList)

        if endgame(unitList)[0] == True:
            if endgame(unitList)[1] == True:
                return 0
            else:
                return 1

class unitAct:
    

    def knight(unitList, y, x):
        #공격 부분
        for i in range(x + 1, x - 2, -2):
            if i < 0 or i > 2:
                continue
            if unitList[y][i].name != "no.txt" and unitList[y][i].team != unitList[y][x]:
                unitList[y][i].hp -= unitAct.attack(unitList, [y, x], [y, i])
                return unitList
            
        for i in range(y + 1, y - 2, -2):
            if i < 0 or i > 2:
                continue
            if unitList[i][x].name != "no.txt" and unitList[i][x].team != unitList[y][x]:
                unitList[i][x].hp -= unitAct.attack(unitList, [y, x], [i, x])
                return unitList
        
        #공격 대상이 없을 때, 이동 부분
        if x < 3 and unitList[y][x + 1].sort == "no":
            unitList[y][x], unitList[y][x + 1] = unitList[y][x + 1], unitList[y][x]
            return unitList
        
        elif x > 3 and unitList[y][x - 1].sort == "no":
            unitList[y][x], unitList[y][x - 1] = unitList[y][x - 1], unitList[y][x]
            return unitList
        
        else:
            if y < 1 and unitList[y + 1][x].sort == "no":
                unitList[y + 1][x], unitList[y][x] = unitList[y][x], unitList[y + 1][x]
                return unitList
            
            elif y > 1 and unitList[y - 1][x].sort == "no":
                unitList[y - 1][x], unitList[y][x] = unitList[y][x], unitList[y - 1][x]
                return unitList
        
        return unitList
        


    
    
    def archer(unitList, y, x):
        return unitList
    
    def scissor(unitList, y, x):
        return unitList
    
    def debuffer(unitList, y, x):
        return unitList
    
    def healer(unitList, y, x):
        return unitList
    
    def no(unitList, y, x):
        return unitList
    
    def attack(unitList, attacker, defender):
        damage = (unitList[attacker[0]][attacker[1]].atk) / (unitList[defender[0]][defender[1]].defend ** 0.5) // 1
        if damage == 0:
            return 1
        return damage




def endgame(unitList): # 게임이 종료되었는지를 확인
    userTeam = 0
    enemyTeam = 0
    for i in range(0, 3):
        for j in range(0, 7):
            if unitList[i][j].hp != 0 and unitList[i][j].team == "user":
                userTeam += 1
            elif unitList[i][j].hp != 0 and unitList[i][j].team == "enemy":
                enemyTeam += 1
    
    if userTeam == 0:
        return [True, False]
    elif enemyTeam == 0:
        return [True, True]
    else:
        return [False, False]

        