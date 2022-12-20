
import day1 as d1
import day2 as d2
import day3 as d3
import day4 as d4

def main():
    print("Day 1")
    sumList = d1.listSum('Data/data.txt')
    highestCal = max(sumList)
    print(f"Elf with highest caloric count is {highestCal}")

    sumList.remove(highestCal)
    highest2 = max(sumList)
    print(f"Elf with 2nd highest caloric count is {highest2}")

    sumList.remove(highest2)
    highest3 = max(sumList)
    print(f"Elf with 3rd highest caloric count is {highest3}")

    print(f"The total caloric count for all three elves is {highestCal + highest2 + highest3}")


    print("Day 2")
    rpsList = d2.parseData("Data/rpsData.txt")
    print(f"Total is: {sum(rpsList)}")

    rpsListNew = d2.parseDataNewStrat("Data/rpsData.txt")
    print(f"Total with new strategy is: {sum(rpsListNew)}")

    print("Day 3")
    s = d3.rucksack("Data/bagData.txt")
    print(s)
    s2 = d3.rucksack_badges("Data/bagData.txt")
    print(s2)

    print("Day 4")
    assignments_overlap = d4.assignments('Data/assignmentData.txt')
    print(assignments_overlap)
    assignments_overlap_any = d4.assignments2('Data/assignmentData.txt')
    print(assignments_overlap_any)

if __name__ == "__main__":
    main()

