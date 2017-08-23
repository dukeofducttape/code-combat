# The goal is to survive for 30 seconds, and keep the mines intact for at least 30 seconds.

def findBestItem(items):
    bestItem = None
    bestValue = 0
    for item in items:
        if item.value / hero.distanceTo(item) > bestValue:
            bestItem = item
            bestValue = item.value / hero.distanceTo(item)   
    return bestItem

def chooseStrategy():
    enemies = hero.findEnemies()
    # If you can summon a griffin-rider, return "griffin-rider"
    if hero.gold >= hero.costOf("griffin-rider"):
        return "griffin-rider"
    # If there is a fangrider on your side of the mines, return "fight-back"
    for enemy in enemies:
        if enemy and enemy.type == "fangrider" and enemy.pos.x < 36:
            return "fight-back"
    # Otherwise, return "collect-coins"
    return "collect-coins"

def commandAttack():
    # Command your griffin riders to attack ogres.
    friends = hero.findFriends()
    if friends:
        for friend in friends:
            enemies = friend.findEnemies()
            enemy = friend.findNearest(enemies)
            if enemy:
                hero.command(friend, "attack", enemy)
    
def pickUpCoin():
    # Collect coins
    coins = hero.findItems()
    coin = findBestItem(coins)
    if coin:
        hero.move(coin.pos)
    
def heroAttack():
    # Your hero should attack fang riders that cross the minefield.
    enemies = hero.findEnemies()
    for enemy in enemies:
        if enemy and enemy.pos.x < 36:
            while enemy.health > 0:
                hero.attack(enemy)

def summonGriffinRider():
    hero.summon("griffin-rider")
    
while True:
    strategy = chooseStrategy()
    commandAttack()
    # Call a function, depending on what the current strategy is.
    if strategy == "griffin-rider":
        summonGriffinRider()
    elif strategy == "fight-back":
        heroAttack()
    else:
        pickUpCoin()
