def rucksack(input_file):
    prior_sum = 0
    with open(input_file, "r") as f:
        for line in f.readlines():
            inside = [el for el in line.rstrip()]
            # get unique items of each compartment
            comp1 = set(inside[:len(inside) // 2])
            comp2 = set(inside[len(inside) // 2:])
            # get the element that is common
            el = list(comp1.intersection(comp2))[0]
            if el == el.upper():
                p = ord(el) - 65 + 27
            else:
                p = ord(el) - 97 + 1
            # add the priority to the sum
            prior_sum += p
    return (prior_sum)


def rucksack_badges(input_file):
    common_carryon = set()
    elves = 0
    prior_sum = 0
    with open(input_file, "r+") as f:
        for line in f.readlines():
            carryon = set([el for el in line.rstrip()])

            elves += 1

            common_carryon = carryon if elves % 3 == 1 else common_carryon.intersection(carryon)

            if (elves % 3 == 0):

                badge = list(common_carryon)[0]
                common_carryon = set()

                if badge == badge.upper():
                    p = ord(badge) - 65 + 27

                else:
                    p = ord(badge) - 97 + 1

                # add the priority to the sum
                prior_sum += p

    return (prior_sum)
