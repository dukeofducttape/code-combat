# Ogre Witches have some unpleasant surprises ready for you.

# Define a chooseTarget function which takes a friend argument
# Returns the a target to attack, depending on the type of friend.
# Soldiers should attack the witches, archers should attack nearest enemy.
def chooseTarget(friend):
    if friend.type == "soldier":
        target = friend.findNearest(hero.findByType("witch"))
    elif friend.type == "archer":
        target = friend.findNearestEnemy()
    return target

while True:
    friends = hero.findFriends()
    for friend in friends:
        # Use your chooseTarget function to decide what to attack.
        chosenTarget = chooseTarget(friend)
        
        if chosenTarget:
            hero.command(friend, "attack", chosenTarget)
