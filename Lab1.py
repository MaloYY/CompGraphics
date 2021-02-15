from graphics import *

def start():

    win = GraphWin('Lab1', 500, 500)

    pt = Point(100, 100)

    cir = Circle(center=pt, radius=50)

    cir.draw(win)

    win.getMouse()
    win.close()