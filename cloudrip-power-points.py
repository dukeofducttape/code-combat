# You need to find and destroy 3 skeletons.
# Skeletons and items are summoned at points of power.
# Move to a point and say the spell: "VENI".
# To find the required points, use the wizard's map.
# 0s are bad points. Positive numbers are good.

spell = "VENI"
# The map of points is a 2D array of numbers.
wizard = hero.findNearest(hero.findFriends())
powerMap = wizard.powerMap

# This function converts grid into x-y coordinates.
def convert(row, col):
    return {'x': 16 + col * 12, 'y': 16 + row * 12}

# Loop through the powerMap to find positive numbers.
# First, loop through indexes of rows.
for i in range(len(powerMap)):
    # Each row is an array. Iterate through it.
    for j in range(len(powerMap[i])):
        # Get the value of the i row and j column.
        pointValue = powerMap[i][j]
        # If it's a positive number:
        if pointValue > 0:
            # Use convert to get XY coordinates.
            moveTo = convert(i, j)
            # Move there, say "VENI" and be prepared!
            hero.moveXY(moveTo.x, moveTo.y)
            hero.say(spell)
            enemy = hero.findNearestEnemy()
            item = hero.findNearestItem()
            if enemy:
                while enemy.health > 0:
                    hero.attack(enemy)
            if item:
                hero.moveXY(item.pos.x, item.pos.y)
