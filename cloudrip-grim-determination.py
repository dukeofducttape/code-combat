# Your goal is to protect Reynaldo

# Find the paladin with the lowest health.
def lowestHealthPaladin():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.type != "paladin":
            continue
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend

def commandPaladin(paladin):
    # Heal the paladin with the lowest health using lowestHealthPaladin()
    # You can use paladin.canCast("heal") and command(paladin, "cast", "heal", target)
    # Paladins can also shield: command(paladin, "shield")
    # And don't forget, they can attack, too!
    low = lowestHealthPaladin()
    enemy = paladin.findNearestEnemy()
    if low and low.health < low.maxHealth / 2:
        if paladin.canCast("heal"):
            hero.command(paladin, "cast", "heal", low)
    elif paladin.health < paladin.maxHealth * 0.3:
        hero.command(paladin, "shield")
    else:
        hero.command(paladin, "attack", enemy)

def commandPeasant(peasant):
    item = peasant.findNearest(peasant.findItems())
    if item:
        hero.command(peasant, "move", item.pos)
        
def commandGriffin(griffin):
    enemy = griffin.findNearestEnemy()
    if enemy:
        hero.command(griffin, "attack", enemy)

def commandFriends():
    # Command your friends.
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "peasant":
            commandPeasant(friend)
        elif friend.type == "griffin-rider":
            commandGriffin(friend)
        elif friend.type == "paladin":
            commandPaladin(friend)

while True:
    commandFriends()
    # Summon griffin riders!
    if hero.gold >= hero.costOf("griffin-rider"):
        hero.summon("griffin-rider")
