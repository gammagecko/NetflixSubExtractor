import re
japanese_pattern = re.compile(r'[\u3040-\u30FF\u4E00-\u9FFF\u3000-\u303F]')

def find_first_japanese_char(text):
    # Search for the first Japanese character
    match = japanese_pattern.search(text)
    if match:
        return match.start()

with open("GraveOfTheFireFiles.txt", "r", encoding="utf-8") as file:
    beginTimeStamp = []
    endTimeStamp = []
    subArray = []
    for line in file:
        line = line.strip()
        if line.startswith('<p xml:id=\"subtitle'):
            startIndex = line.find("begin=") + 7
            endIndex = startIndex + line[startIndex:].find("t")
            beginTimeStamp.append(line[startIndex:endIndex])

            startIndex = line.find("end=") + 5
            endIndex = startIndex + line[startIndex:].find("t")
            endTimeStamp.append(line[startIndex:endIndex])

            japaneseChar = japanese_pattern.search(line)
            startIndex = japaneseChar.start()
            if line[startIndex - 1] == '(':
                startIndex -= 1
            #japaneseChar = japanese_pattern.search(line[::-1])
            #endIndex = japaneseChar.start()
            #print(endIndex)
            #subArray.append(line[startIndex:endIndex])

   # for i in range(len(subArray)):
   #     print(subArray[i])