with open("GraveOfTheFireFiles.txt", "r", encoding="utf-8") as file:
    beginTimeStamp = []
    for line in file:
        line = line.strip()
        if line.startswith("<p xml:id=\"subtitle\""):
            startIndex = line.find("begin=") + 7
            endIndex = line[startIndex:].find("t")
            beginTimeStamp.append(line[startIndex:endIndex])
            print(line[startIndex:endIndex])