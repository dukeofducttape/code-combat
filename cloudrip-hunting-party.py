# Command your troops to move east and attack any ogres they see.
# Use for-loops and findFriends.
# You can use findNearestEnemy() on your soldiers to get their nearest enemy instead of yours.


while True:
    friends = hero.findFriends()
    for j in range(len(friends)):
        friend = friends[j]
        enemy = friend.findNearestEnemy()
        if enemy:
            hero.command(friend, "attack", enemy)
        elif friend.health < friend.maxHealth * 0.5:
            newX = friend.pos.x - 5
            newY = friend.pos.y
            hero.command(friend, "move", {"x":newX, "y":newY})
        else:
            newX = friend.pos.x + 5
            newY = friend.pos.y
            hero.command(friend, "move", {"x":newX, "y":newY})

while True:
    heroEnemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    else:
        heroX = hero.pos.x + 5
        heroY = hero.pos.y
        hero.moveXY(heroX, heroY)
