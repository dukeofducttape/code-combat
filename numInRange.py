def numInRange(units, range):
    inRange = 0
    index = 0
    while index < len(units):
        unit = units[index]
        if hero.distanceTo(unit) < range:
            inRange += 1
        index += 1
    return inRange
