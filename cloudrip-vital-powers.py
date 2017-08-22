# This level shows how to define your own functions.
# The code inside a function is not executed immediately. It's saved for later.
# This function has your hero collect the nearest coin.

# !!! This solution will not get the bonus with current gear (health 1963) !!!

def numInRange(units, range):
    inRange = 0
    for unit in units:
        if hero.distanceTo(unit) < range:
            inRange += 1
    return inRange

def useCleave(enemies, range, minEnemies):
    enemy = hero.findNearest(enemies)
    if enemy and hero.isReady("cleave") and numInRange(enemies, range) >= minEnemies:
        hero.cleave(enemy)

def findBestItem(items):
    bestItem = None
    bestValue = 0
    for item in items:
        if item.value / hero.distanceTo(item) > bestValue:
            bestItem = item
            bestValue = item.value / hero.distanceTo(item)   
    return bestItem

def pickUpCoin():
    items = hero.findItems()
    nearestCoin = findBestItem(items)
    if nearestCoin:
        hero.move(nearestCoin.pos)

# This function has your hero summon a soldier.
def summonSoldier():
    # Fill in code here to summon a soldier if you have enough gold.
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")


# This function commands your soldiers to attack their nearest enemy.
def commandSoldiers():
    for soldier in hero.findFriends():
        enemy = soldier.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)

while True:
    # In your loop, you can "call" the functions defined above.
    # The following line causes the code inside the "pickUpNearestCoin" function to be executed.
    pickUpCoin()
    # Call summonSoldier here
    summonSoldier()
    # Call commandSoldiers here
    commandSoldiers()
    #Cleave enemies if enough are in range
    enemies = hero.findEnemies()
    useCleave(enemies, 10, 3)
