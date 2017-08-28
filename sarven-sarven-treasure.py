# Works for through level 4 with good equipment.

# Collect 150 gold while evading ogres with teleporters.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

teleports = [{"x": 5, "y": 49},{"x": 5, "y": 19},{"x": 76, "y": 51},{"x": 76, "y": 19}]

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

while True:
    coins = hero.findItems()
    coin = None
    coin = findBestItem(coins)
    enemy = hero.findNearestEnemy()
    if enemy and coin:
        if hero.distanceTo(coin) > hero.distanceTo(enemy):
            teleport = hero.findNearest(teleports)
            hero.move(teleport)
        else:
            hero.move(coin.pos)
