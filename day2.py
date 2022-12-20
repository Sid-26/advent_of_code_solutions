def parseData(fileName: str) -> list:
    rpsList = []
    with open(fileName,'r') as file:
        for line in file:
            line = line.replace("\n","")
            if line == "A X":
                rpsList.append(4)
            elif line == "A Y":
                rpsList.append(8)
            elif line == "A Z":
                rpsList.append(3)
            elif line == "B X":
                rpsList.append(1)
            elif line == "B Y":
                rpsList.append(5)
            elif line == "B Z":
                rpsList.append(9)
            elif line == "C X":
                rpsList.append(7)
            elif line == "C Y":
                rpsList.append(2)
            elif line == "C Z":
                rpsList.append(6)
    return  rpsList

def parseDataNewStrat(fileName: str) -> list:
    rpsList = []
    with open(fileName,'r') as file:
        for line in file:
            line = line.replace("\n","")
            if line == "A X":
                rpsList.append(3)
            elif line == "A Y":
                rpsList.append(4)
            elif line == "A Z":
                rpsList.append(8)
            elif line == "B X":
                rpsList.append(1)
            elif line == "B Y":
                rpsList.append(5)
            elif line == "B Z":
                rpsList.append(9)
            elif line == "C X":
                rpsList.append(2)
            elif line == "C Y":
                rpsList.append(6)
            elif line == "C Z":
                rpsList.append(7)
    return  rpsList

