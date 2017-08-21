def findBestItem(items):
    bestItem = None
    bestValue = 0
    for item in items:
        if item.value / hero.distanceTo(item) > bestValue:
            bestItem = item
            bestValue = item.value / hero.distanceTo(item)   
    return bestItem

# Collect 80 gold
while hero.gold < 80:
    coins = hero.findItems()
    coin = findBestItem(coins)
    if coin:
        hero.move(coin.pos)

# Build 4 soldiers to use as bait
for i in range(4):
    hero.summon("soldier")
    
# Send your soldiers into position
points = []
points[0] = { "x": 13, "y": 73 }
points[1] = { "x": 51, "y": 73 }
points[2] = { "x": 51, "y": 53 }
points[3] = { "x": 90, "y": 52 }
friends = hero.findFriends()

# Use range to make an array to loop over.
# Match the friends to the points and command them to move
while True:
    friends = hero.findFriends()
    for j in range(len(friends)):
        point = points[j]
        friend = friends[j]
        hero.command(friend, "move", point)
