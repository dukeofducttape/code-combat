# --------------------------------------------------------------------------
# I got this solution from https://gist.github.com/a1ip/b948e20a7f5f37c39aae
# The original code was in JavaScript so I did the work of "translating" the code to Python and made some minor changes.
# --------------------------------------------------------------------------
# Your goal is to collect coins / gems.
# This level is repeatable. If you win, the difficulty and rewards will increase.
# If you fail, you have to wait a day to resubmit.
# This level is an optional challenge level. You don't need to beat it to continue the campaign!
enemyTypes = [{'door':{"danger": 1000, "focus": 200}},
            {'knight':{"danger": 100, "focus": 100}},
            {'potion-master':{"danger": 100, "focus": 100}},
            {'ranger':{"danger": 100, "focus": 100}},
            {'samurai':{"danger": 100, "focus": 100}},
            {'librarian':{"danger": 100, "focus": 100}},
            {'sorcerer':{"danger": 100, "focus": 100}},
            {'necromancer':{"danger": 100, "focus": 100}},
            {'captain': {"danger": 100, "focus": 100}}, 
            {'hero-placeholder-1':{"danger": 99, "focus": 100}},
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
        elif hero.isReady("bash"):
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
        elif friend.type == 'peasant':
            commandPeasant(friend)

def commandSoldier(soldier):
    target = hero.findNearest(self.findEnemies())
    if target:
        hero.command(soldier, "attack", target)

def commandPeasant(peasant):
    item = peasant.findNearest(peasant.findItems())
    if item:
        hero.command(peasant, "move", item.pos)

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
    items = hero.findItems()
    enimies = hero.findEnemies()
    if hero.health < hero.maxHealth * 0.2:
        summonTroops()
    commandTroops()
    if items.length > 0 and hero.health < hero.maxHealth * 0.9:
        pickUpNearestItem(items)
    else:
        enemyToAttack = findTarget()
        if not enemyToAttack:
            enemyToAttack = hero.findNearest(hero.findEnemies())
        if enemyToAttack:
            attack(enemyToAttack)
        else:
            hero.shield()
