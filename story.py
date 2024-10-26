import usefuldefs as defs
import game

def asciiart(fileName):
    for i in range(2, 31):
        defs.lineClear(i)
    art = open(fileName, "r", encoding="utf-8") #아스키 아트 파일 오픈
    artList = []

    for line in art:
        artList.append(line) # 리스트 artList에 아스키 아트 한 줄씩 추가
    
    for i in range(0, len(artList)): # 아스키 아트 출력
        defs.cursorMove(i + 2, 66)
        print(artList[i], end="")
    
    print()
    return 0

def story(storyName):
    game.horizontalLine(38)
    prompt = open(storyName, "r", encoding="utf-8")
    quote = []
    printed = 0

    for line in prompt:
        quote.append(line)
    
    lineNumber = len(quote)

    for i in range(0, lineNumber):
        if quote[i][0:3] == "end":
            while True:
                cont = defs.buttonTrigger()
                if cont == "a":
                    for i in range(0, printed):
                        defs.lineClear(i + 39)
                    printed = 0
                    break
        elif quote[i][0:5] == "ascii":
            asciiart(quote[i][6:-1])
        else:
            defs.cursorMove(printed + 39, 2)
            print(quote[i], end="")
            printed += 1
            
def ending():
    defs.windowClear()
    defs.center("Thank You for Playing", 23)
    defs.center("24-2 알고리즘과 게임콘텐츠 : 하늘팀", 43)