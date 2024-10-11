import usefuldefs as defs

def story1(storyName):
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

                defs.lineClear(5 + count)
                defs.center(quote[i], 5 + count)
                i += 1
                count += 1
        while True:
            getchar = defs.buttonTrigger()
            if getchar == "a" or "A":
                if read == True:
                    return 0
                count = 0
                break
