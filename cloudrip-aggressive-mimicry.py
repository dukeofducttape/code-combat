# Protect the village from the ogres. 
# Watch for ogres, peasants and ogres disguised as ”peasants".

# This function checks if the text starts with the word.
def startsWith(text, word):
    # If the word is longer then the text:
    if len(word) > len(text):
        return False
    # Loop through the indexes of word and text.
    for index in range(len(word)):
        # If characters with the same index are different:
        if word[index] != text[index]:
            # Then the word doesn't coincide with the text.
            return False
    # We checked all letters and they are the same.
    return True

ogreNameStart = "Zog"

while True:
    enemy = hero.findNearestEnemy()
    suspect = hero.findNearest(hero.findFriends())
    # Use the function "startsWith" to check
    # if suspect's name (id) starts with "Zog", attack:
    if startsWith(suspect.id, "Zog"):
        while suspect.health > 0:
            if hero.isReady("bash"):
                hero.bash(suspect)
            else:
                hero.attack(suspect)
    # Else if there is an enemy, then attack it:
    elif enemy:
        while enemy.health > 0:
            if hero.isReady("bash"):
                hero.bash(enemy)
            else:
                hero.attack(enemy)
    # Else return to the red X mark:
    else:
        hero.move({"x":27, "y":27})
