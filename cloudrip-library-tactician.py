# Hushbaum has been ambushed by ogres!
# She is busy healing her soldiers, you should command them to fight!
# The ogres will send more troops if they think they can get to Hushbaum or your archers, so keep them inside the circle!

# Soldiers spread out in a circle and defend.
def commandSoldier(soldier, soldierIndex, numSoldiers):
    angle = Math.PI * 2 * soldierIndex / numSoldiers
    defendPos = {"x": 41, "y": 40}
    defendPos.x += 10 * Math.cos(angle)
    defendPos.y += 10 * Math.sin(angle)
    hero.command(soldier, "defend", defendPos);

# Find the strongest target (most health)
# This function returns something! When you call the function, you will get some value back.
def findStrongestTarget():
    mostHealth = 0
    bestTarget = None
    enemies = hero.findEnemies()
    # Figure out which enemy has the most health, and set bestTarget to be that enemy.
    for enemy in enemies:
        if enemy.health > mostHealth:
            bestTarget = enemy
            mostHealth = enemy.health
    # Only focus archers' fire if there is a big ogre.
    if bestTarget and bestTarget.health > 15:
        return bestTarget
    else:
        return None


# If the strongestTarget has more than 15 health, attack that target. Otherwise, attack the nearest target.
def commandArcher(archer):
    nearest = archer.findNearestEnemy()
    if archerTarget:
        hero.command(archer, "attack", archerTarget)
    elif nearest:
        hero.command(archer, "attack", nearest)

archerTarget = None

while True:
    # If archerTarget is defeated or doesn't exist, find a new one.
    if not archerTarget or archerTarget.health <= 0:
        # Set archerTarget to be the target that is returned by findStrongestTarget()
        archerTarget = findStrongestTarget()
    
    friends = hero.findFriends()
    soldiers = hero.findByType("soldier")
    # Create a variable containing your archers.
    archers = hero.findByType("archer")
    for i in range(len(soldiers)):
        soldier = soldiers[i]
        commandSoldier(soldier, i, len(soldiers));
    # use commandArcher() to command your archers
    for archer in archers:
        commandArcher(archer)
