# Collect all the coins!
# The peasants are unable to get the coins from other areas
# However, each area only spawns a certain value of coin!
# Filter through all the items and command the peasants accordingly.

def commandPeasant(peasant, coins):
    # Command the peasant to the nearest of their array
    coin = peasant.findNearest(coins)
    if coin:
        hero.command(peasant, "move", coin.pos)

friends = hero.findFriends()
peasants = {
    "Aurum": friends[0],
    "Argentum": friends[1],
    "Cuprum": friends[2]
}

while True:
    items = hero.findItems()
    goldCoins = []
    silverCoins = []
    copperCoins = []
    for item in items:
        if item.value == 3:
            goldCoins.append(item)
        # Put bronze and silver coins in their approriate array:
        elif item.value == 2:
            silverCoins.append(item)
        else:
            copperCoins.append(item)
    
    commandPeasant(peasants.Aurum, goldCoins)
    commandPeasant(peasants.Argentum, silverCoins)
    commandPeasant(peasants.Cuprum, copperCoins)
