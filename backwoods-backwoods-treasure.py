#Works for Backwoods Treasure up to level 3 with good gear. 
#Long Sword must be equipped to use cleave.
#I have not tested to see if a different sword would outperform
#the Long Sword when swarmed by many weak enemies.

# Collect 100 gold from two or three groves.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

def numInRange(units, range):
    inRange = 0
    index = 0
    while index < len(units):
        unit = units[index]
        if hero.distanceTo(unit) < range:
            inRange += 1
        index += 1
    return inRange

def findMostHealth(enemies):
    target = None
    targetHealth = 0
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        if enemy.health > targetHealth:
            target = enemy
            targetHealth = enemy.health
        enemyIndex += 1
    return target

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
    enemies = hero.findEnemies()
    enemy = findMostHealth(enemies)
    coins = hero.findItems()
    coin = None
    coin = findBestItem(coins)
    if enemy and coin and hero.distanceTo(enemy) < hero.distanceTo(coin):
        while enemy.health > 0:
            if hero.isReady("cleave") and numInRange(enemies, 10) > 3:
                hero.cleave(enemy)
            elif hero.isReady("bash") and enemy.health > 33:
                hero.bash(enemy)
            else:
                hero.attack(enemy)
    elif coin:
        hero.move(coin.pos)
    else:
        hero.moveXY(40, 32)
        
#-------------------------------------------
#-------------------------------------------
# With good enough gear, you can basically ignore the enemies and just run around grabbing coins...
# I had had my hero stop to cleave enemies if there were more than 5 in range to thin out the herd.

# Collect 100 gold from two or three groves.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

def numInRange(units, range):
    inRange = 0
    index = 0
    while index < len(units):
        unit = units[index]
        if hero.distanceTo(unit) < range:
            inRange += 1
        index += 1
    return inRange

def findMostHealth(enemies):
    target = None
    targetHealth = 0
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        if enemy.health > targetHealth:
            target = enemy
            targetHealth = enemy.health
        enemyIndex += 1
    return target

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
    enemies = hero.findEnemies()
    enemy = hero.findNearestEnemy()
    coins = hero.findItems()
    coin = None
    coin = findBestItem(coins)
    if enemy:
        if hero.isReady("cleave") and numInRange(enemies, 10) > 5:
            hero.cleave(enemy)
    if coin:
        hero.move(coin.pos)
    else:
        hero.moveXY(40, 32)
        
