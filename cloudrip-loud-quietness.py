# Move the hero and their pet to the exits.

def onHear(event):
    # Get the volume and the password.
    words = event.message.split(" ")
    volume = words[0]
    password = words[1]
    #  If the password should be loud:
    if volume == "Loud":
        # The pet repeats it in UPPER CASE.
        pet.say(words[1].toUpperCase())
    # If the password should be quiet:
    if volume == "Quiet":
        # The pet repeats it in lower case.
        pet.say(words[1].toLowerCase())
    pet.moveXY(pet.pos.x+ 24, pet.pos.y)

def passDoor():
    guard = hero.findNearest(hero.findFriends())
    password = guard.password
    #  If the password should be loud:
    if guard.isLoud:
        # Use the .toUpperCase() method on the password.
        hero.say(password.toUpperCase())
    # If the password should be quiet:
    elif guard.isQuiet:
        # Use the .toLowerCase() method on the password.
        hero.say(password.toLowerCase())
    hero.moveXY(hero.pos.x+ 24, hero.pos.y)

# Enable the pet to hear the guards.
pet.on("hear", onHear)
# The code for the hero to pass the doors.
hero.moveXY(10, 14)
passDoor()
passDoor()
