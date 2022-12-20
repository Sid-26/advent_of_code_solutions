def listSum(fileName: str) -> list:
    contents = []
    sumList = []

    with open(fileName, 'r') as file:
        for line in file:
            if line == "\n":
                sumList.append(sum(contents))
                contents = []
            else:
                contents.append(int(line))

    return sumList

