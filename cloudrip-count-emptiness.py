# Solve the riddler puzzle and find the treasure.
# Count the whitespace on both sides of a riddle.

# This function moves the hero N steps right.
def moveNSteps(n):
    hero.moveXY(hero.pos.x + 8 * n, hero.pos.y)

# Read the riddle.
riddle = hero.findNearestEnemy().riddle
# Trim whitespace from both sides and store in a variable
trimmed = riddle.trim()
# Find the difference between the lengths:
diff = len(riddle) - len(trimmed)
# Use the result and moveNSteps function to move to the spot:
moveNSteps(diff)
# Say something there!
hero.say("something there!")
