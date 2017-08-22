# The inner gate can hold for a long time.
# However, one of these peasants is an OGRE SPY!
# There is a hint! The spy's name has the letter "z"

# This function checks for a specific letter in a word.
# A string is just an array! Loop over it like an array
def letterInWord(word, letter):
    for i in range(len(word)):
        character = word[i]
        # If character is equal to letter, return True
        if character == letter:
            return True
    # The letter isn't in the word, so return False
    return False


spyLetter = "z"
friends = hero.findFriends()

for friend in friends:
    friendName = friend.id
    if letterInWord(friendName, spyLetter):
        # Reveal the spy!
        hero.say(friendName + " is a spy!")
    else:
        hero.say(friendName + " is a friend.")
