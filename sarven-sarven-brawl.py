# Stay alive for two minutes.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

arcDefendPoints = [{"x":75, "y":77}, {"x":75, "y":74}, {"x":75, "y":67}, {"x":75, "y":63}]
heroDefendPoint = {"x":73, "y":70}

enemyTypes = [{"unittype": "shaman", "danger": 10, "focus": 30}, 
            {"unittype": "warlock", "danger": 10, "focus": 30},
            {"unittype": "witch", "danger": 8, "focus": 30}, 
            {"unittype": "brawler", "danger": 7, "focus": 30}, 
            {"unittype": "ogre", "danger": 5, "focus": 30}, 
            {"unittype": "chieftain", "danger": 6, "focus": 30}, 
            {"unittype": "thrower", "danger": 3, "focus": 30}, 
            {"unittype": "fangrider", "danger": 4, "focus": 30},
            {"unittype": "scout", "danger": 3, "focus": 30},
            {"unittype": "munchkin", "danger": 2, "focus": 30},
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
        elif hero.isReady("bash") and target.health > 42:
            hero.bash(target)
        elif hero.isReady("power-up") and target.health > 63:
            hero.powerUp()
        elif hero.isReady("attack"):
            hero.attack(target)
        else:
            hero.shield()

def summonTroops():
    if hero.gold >= hero.costOf('archer') and hero.pos.x > 60:
        hero.summon('archer')

def commandTroops():
    friends = hero.findFriends()
    for i in range(len(friends)):
        friend = friends[i]
        arcDefendPoint = arcDefendPoints[i % 4]
        if friend.type == "archer":
            hero.command(friend, "defend", arcDefendPoint)

while True:
    summonTroops()
    commandTroops()
    target = findTarget()
    if target and target.pos.x >= 40:
        attack(target)
    else:
        moveTo(heroDefendPoint)
