"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Detect when all tiles are revealed.
"""
# Libraries imported
# Random Library allows random enumeration
from random import *
# Turtle Library allows picture creation throught a virtual canvas
from turtle import * 

# Freegames Library include python games
from freegames import path 

# Creates the memory´s image (car will appear at the end)
car = path('car.gif')
# Shows number of total tiles
tiles = list(range(32)) * 2
# Shows the tiles marked
state = {'mark': None}
# Shows the initial condition of the hidden tiles
hide = [True] * 64

sum_taps=0

# Draw a square at a xy position 
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Coordinates converted to numbers on the grid 
def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Numbers converted to coordinates
def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Update initial status, when two numbers are same 
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    # Counts each tap
    global sum_taps, game_complete
    sum_taps= sum_taps + 1

    print("Número de taps: ", sum_taps)
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
            
# Draws the car image if numbers shown are the same. Otherwise,tiles are hidden again.
def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
       
    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

# Main, calling functions
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()