from graphics import *
import numpy as np


def start():
    win = GraphWin('Lab2', 700, 700)
    k = 2 #degree

    x = np.array([100, 300, 350, 100, 200, 220]) #point x
    y = np.array([400, 300, 200, 200, 250, 250]) #point y

    #t = [100, 100, 100, 300, 400, 600, 600, 600, 600]

    t = make_knot_vector(k, len(x))
    print(t)

    xx = np.linspace(100, 600, 300)

    xt_p, yt_p = 0, 0
    for j in range(len(xx)):
        xt, yt = 0, 0
        for i in range(len(x)):
            xt += x[i] * B(xx[j], k, i, t)
            yt += y[i] * B(xx[j], k, i, t)
            if j == 0:
                cir = Circle(Point(x[i], y[i]), 2)
                cir.setFill('red')
                cir.setOutline('red')
                cir.draw(win)
        if xt + yt != 0 and j > 0:
            Line(Point(xt_p, yt_p), Point(xt, yt)).draw(win)
        xt_p, yt_p = xt, yt
        #print(xt_p, yt_p)
        #print(xt, yt)
    win.getMouse()


def B(x, k, i, t):
   if k == 0:
      return 1.0 if t[i] <= x < t[i+1] else 0.0
   if t[i+k] == t[i]:
      c1 = 0.0
   else:
      c1 = (x - t[i])/(t[i+k] - t[i]) * B(x, k-1, i, t)
   if t[i+k+1] == t[i+1]:
      c2 = 0.0
   else:
      c2 = (t[i+k+1] - x)/(t[i+k+1] - t[i+1]) * B(x, k-1, i+1, t)
   return c1 + c2

def make_knot_vector(k, n):
    """
    k - degree
    n - len
    """

    total_knots = n + k + 2
    outer_knots = k + 1
    inner_knots = total_knots - 2 * (outer_knots)

    knots = [100] * (outer_knots)
    knots += [i * 100 for i in range(2, inner_knots+1)]
    knots += [(inner_knots+1) * 100] * (outer_knots)

    return tuple(knots)