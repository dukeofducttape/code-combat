# Practice using modulo to loop over an array

# Choose the mix and order of units you want to summon by populating this array:
summonTypes = ["soldier", "soldier", "archer", "archer"]
solDefendPoints = [{"x":40, "y":42}, {"x":40, "y":36}, {"x":40, "y":28}]
arcDefendPoints = [{"x":36, "y":40}, {"x":36, "y":40}]

def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold >= hero.costOf(type):
        hero.summon(type)

def commandTroops():
    friends = hero.findFriends()
    for i in range(len(friends)):
        friend = friends[i]
        # Use % to wrap around defendPoints based on friendIndex
        solDefendPoint = solDefendPoints[i % 3]
        arcDefendPoint = arcDefendPoints[i % 2]
        
        # Command your minion to defend the defendPoint
        if friend.type == "archer":
            hero.command(friend, "defend", arcDefendPoint)
        elif friend.type == "soldier":
            hero.command(friend, "defend", solDefendPoint)

def findBestItem(items):
    bestItem = None
    bestValue = 0
    for item in items:
        if item.value / hero.distanceTo(item) > bestValue:
            bestItem = item
            bestValue = item.value / hero.distanceTo(item)   
    return bestItem
    
def collectGold():
    coins = hero.findItems()
    coin = findBestItem(coins)
    if coin:
        hero.move(coin.pos)
        

while True:
    summonTroops()
    commandTroops()
    collectGold()
