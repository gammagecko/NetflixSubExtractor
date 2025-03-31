import re

import TimeSearch

japanese_pattern = re.compile(r'[\u3040-\u30FF\u4E00-\u9FFF\u3000-\u303F]+')
from TimeSearch import Binary_Search

def find_first_japanese_char(text):
    # Search for the first Japanese character
    match = japanese_pattern.search(text)
    if match:
        return match.start()

with open("GraveOfTheFireFiles.txt", "r", encoding="utf-8") as file:
    beginTimeStamp = []
    endTimeStamp = []
    subArray = []
    subsAndStampsArray = []
    parenthesis = False

    for line in file:
        line = line.strip()
        if line.startswith('<p xml:id=\"subtitle'):
            startIndex = line.find("begin=") + 7
            endIndex = startIndex + line[startIndex:].find("t")
            beginTimeStamp = int(line[startIndex:endIndex])

            startIndex = line.find("end=") + 5
            endIndex = startIndex + line[startIndex:].find("t")
            endTimeStamp = int(line[startIndex:endIndex])

            japaneseChars = japanese_pattern.findall(line)
            subArray.append([beginTimeStamp, endTimeStamp, japaneseChars])

for i in range(len(subArray)):
    print(subArray[i])

inp = True
while inp == True:
    user_input = input("Enter a time in the format HH:MM:SS: (e.g. 01:05:59 or \"Q\" to quit): ")
    if user_input == "Q":
        inp = False
        break
    try:
        parsed_data = user_input.split(":")
        time_stamp = int(parsed_data[0]) * 3600 + int(parsed_data[1]) * 60 + int(parsed_data[2])
        time_stamp *= 10000000
        print(time_stamp)
        print(TimeSearch.Binary_Search(subArray, time_stamp))
    except:
        print("Invalid input. Please try again.")


