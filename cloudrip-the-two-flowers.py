# If the peasant is damaged, the flowers will shrink!

def summonSoldiers():
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")

# Define the function: commandSoldiers
def commandSoldiers():
    for friend in hero.findFriends():
        enemy = friend.findNearestEnemy()
        if enemy and friend.type == "soldier":
            hero.command(friend, "attack", enemy)

# Define the function: pickUpNearestCoin
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
        
peasant = hero.findByType("peasant")[0]

while True:
    summonSoldiers()
    commandSoldiers()
    pickUpCoin()
