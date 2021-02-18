from graphics import *
import numpy as np

def start():
    win = GraphWin('Lab1', 500, 500)

    x = -1
    y = 2

    cx = 100
    cy = 100
    r = 50

    P = np.array([x, y, 1])
    L = np.array([[1, 0, -cx], [0, 1, -cy], [-cx, -cy, cx ** 2 + cy ** 2 - r ** 2]])

    C = L.dot(P)
    a = C[0]
    b = C[1]
    c = C[2]

    g1 = -2 * cx
    g2 = -2 * cy
    g3 = cx ** 2 + cy ** 2 - r ** 2

    coef1 = b ** 2 + a ** 2
    coef2 = 2 * b * c - a * b * g1 + g2 * a ** 2
    coef3 = c ** 2 - a * c * g1 + a ** 2 * g3

    y1, y2 = np.roots([coef1, coef2, coef3])
    x1 = (-b * y1 - c) / a
    x2 = (-b * y2 - c) / a

    pt = Point(x, y)
    pt.draw(win)

    cir = Circle(center=Point(cx, cy), radius=r)
    cir.draw(win)

    line_1 = Line(pt, Point(x1, y1))
    line_1.draw(win)

    line_2 = Line(pt, Point(x2, y2))
    line_2.draw(win)

    win.getMouse()
    win.close()
