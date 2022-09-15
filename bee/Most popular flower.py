# Find out which type of flower the bees prefer, based on how often they visit each type of flower.
# Format of dictionary flowers:   "Key":{flower_name,Xcord,Ycord}
myflowers = {

    "f1": ("rose", 0, 4),
    "f5": ("rose", 4, 4),
    "f2": ("iris", 4, 0),
    "f3": ("iris", 0, 0),
    "f8": ("tulip", 2, 1)
}

# calculate flower distance


def dist_calc(d1, d2):
    return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])


def popular_busyb(flowers, visits, hive):
    closest = ["invalid"] * 2
    myflowers = flowers
    # loop through flowers
    for value in myflowers.keys():
        if(value in visits):
            # Initialise closest value
            if(closest == ["invalid"] * 2):
                closest[0] = myflowers[value][0]
                closest[1] = dist_calc(
                    (myflowers[value][1], myflowers[value][2]), hive)
            # Add if same flower
            elif(closest[0] == myflowers[value][0]):
                closest[1] = int(closest[1]) + dist_calc(
                    (myflowers[value][1], myflowers[value][2]), hive)
            else:
                newdiff = dist_calc(
                    (myflowers[value][1], myflowers[value][2]), hive)
                # Replace current dist with new values if value is greater then current
                if(newdiff > closest[1]):
                    closest[0] = myflowers[value][0]
                    closest[1] = dist_calc(
                        (myflowers[value][1], myflowers[value][2]), hive)
                # If the distances are the same then sort it
                elif(newdiff == closest[1]):
                    sorted = [myflowers[value]
                              [0], closest[0]]
                    sorted.sort()
                    closest[0] = sorted[0]
    return closest[0]


print(popular_busyb(myflowers, {"f1", "f2", "f3"}, (2, 2)))
