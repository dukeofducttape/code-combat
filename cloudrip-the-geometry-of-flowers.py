# You now have the Ring of Flowers! You can do:
# toggleFlowers(True/False) - turns flowers on or off.
# setFlowerColor("random") - can also be "pink", "red", "blue", "purple", "yellow", or "white".

# Here are some functions for drawing shapes:
# x, y - center of the shape
# size - size of the shape (radius, side length)
def drawCircle(x, y, size):
    angle = 0
    hero.toggleFlowers(False)
    while angle <= Math.PI * 2:
        newX = x + (size * Math.cos(angle))
        newY = y + (size * Math.sin(angle))
        hero.moveXY(newX, newY)
        hero.toggleFlowers(True)
        angle += 0.2

def drawSquare(x, y, size):
    hero.toggleFlowers(False)
    cornerOffset = size / 2
    hero.moveXY(x - cornerOffset, y - cornerOffset)
    hero.toggleFlowers(True)
    hero.moveXY(x + cornerOffset, y - cornerOffset)
    hero.moveXY(x + cornerOffset, y + cornerOffset)
    hero.moveXY(x - cornerOffset, y + cornerOffset)
    hero.moveXY(x - cornerOffset, y - cornerOffset)


redX = {"x": 28, "y": 36}
whiteX = {"x": 44, "y": 36}

# Pick a color.
hero.setFlowerColor("red")
# Draw a size 10 circle at the redX.
drawCircle(28, 36, 10)
# Change the color!
hero.setFlowerColor("white")
# Draw a size 10 square at the whiteX.
drawSquare(44, 36, 10)
# Now experiment with drawing whatever you want!
drawSquare(64, 36, 5)
