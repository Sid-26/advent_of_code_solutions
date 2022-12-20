from DataParser import DataParser

def assignments(inputFile: str) -> int:
    parse = DataParser(inputFile)
    data = parse.parseDataAsList()
    pairs = []
    for elem in data:
        elf1, elf2 = elem.split(',')

        elf1 = [int(i) for i in elf1.split('-')]
        elf2 = [int(i) for i in elf2.split('-')]

        if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            pairs.append([elf1,elf2])
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            pairs.append([elf1,elf2])

    return len(pairs)

def assignments2(intputFile: str) -> int:
    parse = DataParser(intputFile)
    data = parse.parseDataAsList()
    pairs = []

    for elem in data:
        e1, e2 = elem.split(',')

        e1 = [int(i) for i in e1.split('-')]
        e2 = [int(i) for i in e2.split('-')]

        if e1[0] in range(e2[0], e2[1]+1) or e1[1] in range(e2[0],e2[1]+1):
            pairs.append([e1,e2])
        elif e2[0] in range(e1[0],e1[1]+1) or e2[1] in range(e1[0],e1[1]+1):
            pairs.append([e1,e2])

    return len(pairs)