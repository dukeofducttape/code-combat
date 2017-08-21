# Command your troops to move east and attack any ogres they see.
# Use for-loops and findFriends.
# You can use findNearestEnemy() on your soldiers to get their nearest enemy instead of yours.


# Use range to make an array to loop over.
# Match the friends to the points and command them to move
while True:
    friends = hero.findFriends()
    for j in range(len(friends)):
        friend = friends[j]
        enemy = friend.findNearestEnemy()
        if enemy:
            hero.command(friend, "attack", enemy)
        else:
            newX = friend.pos.x + 5
            newY = friend.pos.y
            hero.command(friend, "move", {"x":newX, "y":newY})
