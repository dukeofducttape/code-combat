# Find the soldiers who break the circle.

# All soldiers should be on the circle with the radius:
circleRadius = 20

# The function checks if an unit is placed on the circle
# with the radius with the hero in the center.
def onCircle(unit, radius):
    distance = hero.distanceTo(unit)
    # We check the approximation.
    inaccuracy = 2
    minDistance = radius - inaccuracy
    maxDistance = radius + inaccuracy
    return distance <= maxDistance and distance >= minDistance

while True:
    soldiers = hero.findByType("soldier")
    for soldier in soldiers:
        # Use onCircle function to find
        # if the soldier is not on the circle:
        if not onCircle(soldier, circleRadius):
            # Then say their name (id) to get rid of that one:
            hero.say(soldier.id)
