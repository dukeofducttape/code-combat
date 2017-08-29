# This is a really sloppy solution, but it gets the job done.

# This level is intended to be for advanced players. The solution should be pretty complex with a lot of moving parts. It might also be a bit of a gear check unless you use "creative" methods.
# You need to make your way to the first trial (Oasis of Marr) defeating enemies along the way. When you reach it, pick all the mushrooms to trigger the trial to begin. If you survive the onslaught, make your way to the next Oasis for the second trial, then the Temple. When all trials are complete you will have to face the final boss. Good luck!
# HINT: Glasses with a high visual range help tremendously on this level so buy the best you can get.
# HINT: the unit 'type' for the oasis guardians is 'oasis-guardian'
enemyTypes = [{'door':{"danger": 1000, "focus": 200}},
            {'knight':{"danger": 100, "focus": 100}},
            {'potion-master':{"danger": 100, "focus": 100}},
            {'ranger':{"danger": 100, "focus": 100}},
            {'samurai':{"danger": 100, "focus": 100}},
            {'librarian':{"danger": 100, "focus": 100}},
            {'sorcerer':{"danger": 100, "focus": 100}},
            {'necromancer':{"danger": 100, "focus": 100}},
            {'captain': {"danger": 100, "focus": 100}}, 
            {'oasis-guardian':{"danger": 99, "focus": 100}},
            {'hero-placeholder-2':{"danger": 99, "focus": 100}},
            {'burl': {"danger": 10, "focus": 20}}, 
            {'shaman': {"danger": 10, "focus": 50}}, 
            {'warlock': {"danger": 10, "focus": 30}},
            {'arrow-tower': {"danger": 10, "focus": 20}}, 
            {'catapult': {"danger": 10, "focus": 100}},
            {'artillery': {"danger": 10, "focus": 100}},
            {'witch': {"danger": 8, "focus": 50}}, 
            {'brawler': {"danger": 7, "focus": 55}}, 
            {'ogre': {"danger": 5, "focus": 40}}, 
            {'chieftain': {"danger": 6, "focus": 35}}, 
            {'thrower': {"danger": 3, "focus": 22}}, 
            {'fangrider': {"danger": 4, "focus": 22}}, 
            {'munchkin': {"danger": 2, "focus": 15}},
            {'ice-yak': {"danger": -1, "focus": 0}},
            {'yak': {"danger": -1, "focus": 0}}]

summonTypes = ['soldier', 'soldier', 'soldier', 'archer']

trial = 1

def findTarget():
    danger = 0;
    enemyReturn = None
    for type in enemyTypes:
        if enemyTypes[type] and enemyTypes[type].danger > danger:
            enemy = hero.findNearest(hero.findByType(type))
            if enemy and hero.distanceTo(enemy) < enemyTypes[type].focus:
                enemyReturn = enemy
                danger = enemyTypes[type].danger
    if not enemyReturn:
        enemyReturn = hero.findNearest(hero.findEnemies())
    return enemyReturn

def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items);
    if nearestItem:
        moveTo(nearestItem.pos)

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
        elif hero.isReady("attack"):
            hero.attack(target)
        else:
            hero.shield()

def summonTroops():
    type = summonTypes[hero.built.length % summonTypes.length]
    if hero.gold > hero.costOf(type):
        hero.summon(type)

def commandTroops():
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == 'archer':
            commandArcher(friend)
        elif friend.type == 'soldier':
            commandSoldier(friend)

def commandSoldier(soldier):
    target = soldier.findNearest(soldier.findEnemies())
    if target:
        hero.command(soldier, "attack", target)
    else:
        loc = {"x":hero.pos.x, "y":hero.pos.y + 3}
        hero.command(soldier, "move", loc)
        
def commandArcher(archer):
    target = findTarget()
    if target:
        hero.command(archer, "attack", target)
    else:
        loc = {"x":hero.pos.x, "y":hero.pos.y - 3}
        hero.command(archer, "move", loc)

def lowestHealthFriend():
    lowestHealth = 99999
    weakestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            weakestFriend = friend
    return weakestFriend

while True:
    if trial == 2:
        hero.moveXY(10, 74)
        trial = 3
    if trial == 4:
        hero.moveXY(90, 130)
        trial = 5
    if trial == 6:
        hero.moveXY(60, 72)
        trial = 7
    
    enemy = findTarget()
    commandTroops()
    summonTroops()
    if enemy and enemy.type == 'oasis-guardian':
        trial += 1
        while enemy.health > 0:
            attack(enemy)
    elif enemy and enemy.type != 'oasis-guardian':
        while enemy.health > 0:
            attack(enemy)
    else:
        pickUpNearestItem(hero.findItems())
