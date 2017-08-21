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
    # Move to the nearest coin.
    # Use move instead of moveXY so you can command constantly.
    coins = hero.findItems()
    coin = findBestItem(coins)
    hero.move(coin.pos)
    # If you have funds for a soldier, summon one.
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
        
    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        # Loop over all your soldiers and order them to attack.
        soldiers = hero.findFriends()
        soldierIndex = 0
        while soldierIndex < len(soldiers):
            soldier = soldiers[soldierIndex]
            hero.command(soldier, "attack", enemy)
            soldierIndex += 1
