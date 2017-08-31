# Stay alive for two minutes.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

arcDefendPoints = [{"x":75, "y":77}, {"x":75, "y":70}, {"x":75, "y":63}]
heroDefendPoint = {"x":70, "y":70}

enemyTypes = [{"unittype": "door", "danger": 1000, "focus": 200},
            {"unittype": "burl", "danger": 10, "focus": 20}, 
            {"unittype": "shaman", "danger": 10, "focus": 50}, 
            {"unittype": "warlock", "danger": 10, "focus": 30},
            {"unittype": "witch", "danger": 8, "focus": 50}, 
            {"unittype": "brawler", "danger": 7, "focus": 20}, 
            {"unittype": "ogre", "danger": 5, "focus": 20}, 
            {"unittype": "chieftain", "danger": 6, "focus": 35}, 
            {"unittype": "thrower", "danger": 3, "focus": 24}, 
            {"unittype": "fangrider", "danger": 4, "focus": 24},
            {"unittype": "scout", "danger": 3, "focus": 15},
            {"unittype": "munchkin", "danger": 2, "focus": 15},
            {"unittype": "sand-yak", "danger": -1, "focus": -1},
            {"unittype": "ice-yak", "danger": -1, "focus": -1},
            {"unittype": "yak", "danger": -1, "focus": -1}]

def findTarget():
    danger = 0;
    enemyReturn = None
    for i in range(len(enemyTypes)):
        utype = enemyTypes[i].unittype
        if enemyTypes[i].danger > danger:
            enemy = hero.findNearest(hero.findByType(utype))
            if enemy and hero.distanceTo(enemy) < enemyTypes[i].focus:
                enemyReturn = enemy
                danger = enemyTypes[i].danger
    #if not enemyReturn:
       #enemyReturn = hero.findNearest(hero.findEnemies())
    return enemyReturn

def moveTo(position):
    if hero.isReady("jump") and hero.distanceTo(position) > 10:
        hero.jumpTo(position)
    else:
        hero.move(position)

def attack(target):
    if target:
        if hero.distanceTo(target) > 10:
            moveTo(target.pos)
        elif hero.isReady("bash") and target.health > 21:
            hero.bash(target)
        elif hero.isReady("power-up") and target.health > 42:
            hero.powerUp()
        elif hero.isReady("attack"):
            hero.attack(target)
        else:
            hero.shield()

def summonTroops():
    if hero.gold >= hero.costOf('archer'):
        hero.summon('archer')

def commandTroops():
    friends = hero.findFriends()
    for i in range(len(friends)):
        friend = friends[i]
        arcDefendPoint = arcDefendPoints[i % 3]
        if friend.type == "archer":
            hero.command(friend, "defend", arcDefendPoint)

while True:
    summonTroops()
    commandTroops()
    target = findTarget()
    if target:
        attack(target)
    else:
        moveTo(heroDefendPoint)
