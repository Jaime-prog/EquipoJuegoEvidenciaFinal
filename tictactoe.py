"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
from turtle import *

from freegames import line

def grid():
    """Draw the grid of tictactoe game."""
    pencolor("blue")
    bgcolor("black")
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    pencolor("orange")
    line(x+30, y+30, x + 100, y + 100)
    line(x+30, y + 100, x + 100, y+30)


def drawo(x, y):
    """Draw O player."""
    pencolor("red")
    up()
    goto(x + 64, y + 20)
    down()
    circle(45)


def floor(value):
    """Round value down to grid."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]

def make_symbol(x,y,player):
    """Draw either the x or the o accordingly"""
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player  #Changes from x to o


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    column=(x+205) 
    row= (-y+205)
    square= column +row*3
    square=int(square)  # Set a specific value for each square
    player = state['player']
    make_symbol(x,y,player)
    


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
