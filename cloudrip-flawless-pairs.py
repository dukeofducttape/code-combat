# Collect 4 pairs of gems.
# Each pair must contain equal valued gems.

# This function returns two items with the same value.
def findValuePair(items):
    # Check each possible pair in the array.
    # Iterate indexes 'i' from 0 to the last one.
    for i in range(len(items)):
        itemI = items[i];
        # Iterate indexes 'j' from 0 to the last.
        for j in range(len(items)):
            # If it's the same element, then skip it.
            if i == j:
                continue
            itemJ = items[j];
            # If we found a pair with two equal gems, then return them.
            if itemI.value == itemJ.value:
                return [itemI, itemJ]
    # Return an empty array if no pair exists.
    return None

while True:
    gems = hero.findItems()
    gemPair = findValuePair(gems)
    # If the gemPair exists, collect the gems!
    if gemPair:
        gemA = gemPair[0]
        gemB = gemPair[1]
        # Move to the first gem.
        hero.moveXY(gemA.pos.x, gemA.pos.y)
        # Return to get the haste from the wizard.
        hero.moveXY(40, 44)
        # Then move to the second gem.
        hero.moveXY(gemB.pos.x, gemB.pos.y)
        # Return to get the haste from the wizard.
        hero.moveXY(40, 44)
