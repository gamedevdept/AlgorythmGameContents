import usefuldefs as defs

def asciiart(fileName):
    art = open(fileName, "r", encoding="utf-8")
    artList = []

    for line in art:
        artList.append(line)
    
    for i in range(0, len(artList)):
        defs.cursorMove(i + 2, 2)
        print(artList[i], end="")
    
    print()
    return 0

def story(storyName):
    prompt = open(storyName, "r", encoding="utf-8")
    quote = []
    for line in prompt:
        quote.append(line)
    i = 0
    count = 0
    read = False

    while True:
        while count < 5:
            defs.center("A 키를 눌러 스토리 진행", 38)
            while count < 5:
                if i >= len(quote):
                    read = True
                    while count < 5:
                        defs.lineClear(5 + count)
                        print("")
                        count += 1
                    continue
                if quote[i][0:5] == "ascii":
                    asciiart(quote[i].split(":")[1].split("\n")[0])
                defs.lineClear(35 + count)
                defs.cursorMove(35 + count, 2)
                print(quote[i])
                i += 1
                count += 1
        while True:
            getchar = defs.buttonTrigger()
            if getchar == "a" or "A":
                if read == True:
                    return 0
                count = 0
                break
