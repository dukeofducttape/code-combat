# Incoming Ogre Brawlers!
# Make use of a Robot Walker to dispatch these enemies.
# The Robot Walker requires commands as strings.
# The first part will the enemy's health in ternary.
# The second part will be the enemy's type as binary.

def toTernary(number):
    # Start with an empty string.
    string = ""
    # Then, while the number isn't zero:
    while number != 0:
        # We grab the remainder of our number.
        remainder = number % 3
        # This is our iterator method. 'number' decrements here.
        number = (number - remainder) / 3
        # Append the string to the remainder.
        string = remainder + string
    # Finally we want to return our constructed string.
    return string
    
def toBinary(number):
    string = ""
    # Go through the steps again:
        # Get remainder, decrement, and append string.
    # Remember that binary is another way of saying '2'!
    while number != 0:
        remainder = number % 2
        number = (number - remainder) / 2
        string = remainder + string
    return string

while True:
    enemies = hero.findEnemies()
    dangerous = findMostDangerous(enemies)
    if dangerous:
        # The way the robot takes commands is in the form of:
        # ternary(enemyHealth) + " " + binary(enemyType)
        hero.say(toTernary(dangerous.health) + " " + toBinary(dangerous.type))

# In this level the Ogre Brawlers are more powerful if they have more health.
def findMostDangerous(enemies):
    mostDangerous = None
    mostHealth = 0
    for i in range(len(enemies)):
        enemy = enemies[i]
        if enemy.health > mostHealth:
            mostDangerous = enemy
            mostHealth = enemy.health
    return mostDangerous
