def findBestItem(items):
    bestItem = None
    bestValue = 0
    for item in items:
        if item.value / hero.distanceTo(item) > bestValue:
            bestItem = item
            bestValue = item.value / hero.distanceTo(item)   
    return bestItem
    
# Protect the cage.
# Put a soldier at each X.
points = []
points[0] = {"x": 33, "y": 42}
points[1] = {"x": 47, "y": 42}
points[2] = {"x": 33, "y": 26}
points[3] = {"x": 47, "y": 26}

# 1. Collect 80 gold.
while True:
    if hero.gold < 80:
        coins = hero.findItems()
        coin = findBestItem(coins)
        if coin:
            hero.move(coin.pos)
    else:
        break
# 2. Build 4 soldiers.
for i in range(4):
    hero.summon("soldier")
    
# 3. Send your soldiers into position.
while True:
    friends = hero.findFriends()
    for j in range(len(friends)):
        point = points[j]
        friend = friends[j]
        enemy = friend.findNearestEnemy()
        if enemy and enemy.team == "ogres" and friend.distanceTo(enemy) < 5:
            # Command friend to attack.
            if enemy:
                hero.command(friend, "attack", enemy)
            
        else:
            # Command friend to move to point.
            hero.command(friend, "move", point)
