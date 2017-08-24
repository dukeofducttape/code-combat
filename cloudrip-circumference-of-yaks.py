# Calculate the circumference of yak circles.

# The first yak circle.
yak1 = hero.findNearestEnemy()
# The distance to the yak is the radius.
radius1 = hero.distanceTo(yak1)
# The circumference is calculated the following way:
circumference1 = 2 * Math.PI * radius1
# Let's say the result.
hero.say(circumference1)

# Move to the next mark.
hero.moveXY(60, 34)
# Find an yak from the second circle.
yak2 = hero.findNearestEnemy()
# Find the radius of the second circle.
radius2 = hero.distanceTo(yak2)
# Calculate the circumference of the second circle:
circumference2 = 2 * Math.PI * radius2
# Say the result.
hero.say(circumference2)
