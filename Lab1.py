from graphics import *

def start():
    win = GraphWin('Lab1', 500, 500)

    dot_x = 15
    dot_y = 15

    a = 100
    b = 100
    radius = 50

    cathet = ((a - dot_x)**2 + (b - dot_y)**2)**(1./2)
    denominator = (cathet**2 - radius**2)**(1./2)
    k = radius / denominator



    A = 1 + k ** 2
    B = -2*k**2*dot_x + 2*k*dot_y - 2*k*b - 2*a
    C = a**2 + b**2 + k**2*dot_x**2 - 2*k*dot_y*dot_x + 2*b*k*dot_x + dot_y - 2*b*dot_y**2 - radius**2

    D = B**2 - 4*A*C

    x_line1 = (-B + D**(1./2)) / (2*A)
    #x_line2 = (-B - D**(1./2)) / (2*A)

    y_line1 = k*(x_line1 - dot_x) + dot_y
    #y_line2 = k*(x_line2 - dot_x) + dot_y

    line1 = Line(Point(dot_x, dot_y), Point(x_line1, y_line1))
    line1.draw(win)
    #line2 = Line(Point(dot_x, dot_y), Point(x_line2, y_line2))
    #line2.draw(win)

    #y = 0.37 * (200 - 15) + dot_y
    #ln = Line(Point(15, dot_y), Point(200, y))
    #ln.draw(win)

    pt = Point(dot_x, dot_y)
    pt.draw(win)
    cir = Circle(center=Point(a, b), radius=radius)
    cir.draw(win)

    win.getMouse()
    win.close()