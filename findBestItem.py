def findBestItem(items):
    bestItem = None
    bestValue = 0
    itemIndex = 0
    while itemIndex < len(items):
        item = items[itemIndex]
        if valueOverDistance(item) > bestValue:
            bestItem = item
            bestValue = valueOverDistance(item)
        itemIndex += 1     
    return bestItem
