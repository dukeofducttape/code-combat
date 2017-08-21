#while-loop version:
def findMostHealth(units):
    target = None
    targetHealth = 0
    unitIndex = 0
    while unitIndex < len(units):
        unit = units[unitIndex]
        if unit.health > targetHealth:
            target = unit
            targetHealth = unit.health
        unitIndex += 1
    return target

#for-loop version:
def findMostHealth(units):
    target = None
    targetHealth = 0
    for unit in units:
        if unit.health > targetHealth:
            target = unit
            targetHealth = unit.health
    return target
