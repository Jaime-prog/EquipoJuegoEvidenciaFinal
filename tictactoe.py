"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
import turtle

from freegames import line


def grid():
    """Draw the grid of tictactoe game."""
    turtle.pencolor("blue")
    turtle.bgcolor("black")
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    turtle.pencolor("orange")
    line(x+30, y+30, x + 100, y + 100)
    line(x+30, y + 100, x + 100, y+30)


def drawo(x, y):
    """Draw O player."""
    turtle.pencolor("red")
    turtle.up()
    turtle.goto(x + 64, y + 20)
    turtle.down()
    turtle.circle(45)


def floor(value):
    """Round value down to grid."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
places_on_grid = [
    " ", " ", " ", " ", " ", " ", " ", " ", " "
]  # Array to verify if a place has already been taken


def make_symbol(x, y, player):
    """Draw either the x or the o accordingly"""
    draw = players[player]
    draw(x, y)
    turtle.update()
    state['player'] = not player  # Changes from x to o


def tap(x, y):
    """Draw X or O in tapped square."""
    global places_on_grid
    x = floor(x)
    y = floor(y)
    column = (x+205)
    row = (-y+205)
    square = column + row*3
    square = int(square)  # Set a specific value for each square
    player = state['player']

    if square == 422:
        if places_on_grid[0] == " ":
            places_on_grid[0] = 1
            make_symbol(x, y, player)

        elif places_on_grid[0] != "":
            print("This space has already been used")
    elif square == 555:
        if places_on_grid[1] == " ":
            places_on_grid[1] = 1
            make_symbol(x, y, player)

        else:
            print("This space has already been used")
    elif square == 688:
        if places_on_grid[2] == " ":
            places_on_grid[2] = 1
            make_symbol(x, y, player)

        else:
            print("This space has already been used")
    elif square == 821:
        if places_on_grid[3] == " ":
            places_on_grid[3] = 821
            make_symbol(x, y, player)

        else:
            print("This space has already been used")

    elif square == 954:
        if places_on_grid[4] == " ":
            places_on_grid[4] = 1
            make_symbol(x, y, player)

        else:
            print("This space has already been used")

    elif square == 1087:
        if places_on_grid[5] == " ":
            places_on_grid[5] = 1
            make_symbol(x, y, player)

        else:
            print("This space has already been used")

    elif square == 1220:
        if places_on_grid[6] == " ":
            places_on_grid[6] = 1
            make_symbol(x, y, player)

        else:
            print("This space has already been used")

    elif square == 1353:
        if places_on_grid[7] == " ":
            places_on_grid[7] = 1
            make_symbol(x, y, player)

        else:
            print("This space has already been used")

    elif square == 1486:
        if places_on_grid[8] == " ":
            places_on_grid[8] = 1
            make_symbol(x, y, player)

        else:
            print("This space has already been used")


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.update()
turtle.onscreenclick(tap)
turtle.done()
