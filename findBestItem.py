
#while-loop version
def findBestItem(items):
    bestItem = None
    bestValue = 0
    itemIndex = 0
    while itemIndex < len(items):
        item = items[itemIndex]
        if item.value / hero.distanceTo(item) > bestValue:
            bestItem = item
            bestValue = item.value / hero.distanceTo(item)
        itemIndex += 1     
    return bestItem

#for-loop version
def findBestItem(items):
    bestItem = None
    bestValue = 0
    for item in items:
        if item.value / hero.distanceTo(item) > bestValue:
            bestItem = item
            bestValue = item.value / hero.distanceTo(item)   
    return bestItem
