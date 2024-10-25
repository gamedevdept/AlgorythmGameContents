import usefuldefs as defs

def fight(fightList, enemyFightList):
    board = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]
    for i in fightList:
        for j in range(0, 3):
            for k in range(1, -1, -1):
                board[j][k] = i