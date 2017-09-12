# Survive the waves of ogres.
# If you win, the level gets harder, and gives more rewards.
# If you lose, you must wait a day to re-submit.
# Each time you submit gives a new random seed.
friDefendPoints = [{"x":40, "y":40}, {"x":40, "y":30}]
heroDefendPoint = {"x":40, "y":35}
summonTypes = ["soldier", "soldier", "soldier"]

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
    if not enemyReturn:
       enemyReturn = hero.findNearest(hero.findEnemies())
    return enemyReturn

def moveTo(position):
    if hero.isReady("jump") and hero.distanceTo(position) > 10:
        hero.jumpTo(position)
    else:
        hero.move(position)

def attack(target):
    if target:
        if hero.isReady("bash") and target.health > 42:
            hero.bash(target)
        elif hero.isReady("power-up") and target.health > 63:
            hero.powerUp()
        elif hero.isReady("attack"):
            hero.attack(target)
        else:
            hero.shield()

def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold >= hero.costOf(type):
        hero.summon(type)

def commandTroops():
    friends = hero.findFriends()
    for i in range(len(friends)):
        friend = friends[i]
        friDefendPoint = friDefendPoints[i % 2]
        hero.command(friend, "defend", friDefendPoint)
        

while True:
    summonTroops()
    commandTroops()
    target = findTarget()
    item = hero.findNearestItem()
    if item and hero.health < hero.maxHealth * 0.75:
        hero.move(item.pos)
    if target:
        attack(target)
    else:
        moveTo(heroDefendPoint)
