from graphics import *
import numpy as np

class Lab1():
    def __init__(self, x, y, cx, cy, r):
        self.win = GraphWin('Lab1', 500, 500)

        #point coords
        self.x = x
        self.y = y

        #circle center coords
        self.cx = cx
        self.cy = cy
        #circle radius
        self.r = r

    def start(self):
        if(abs(self.cx - self.x) > 50) and (abs(self.cy - self.y) > 50):
            self.draw()
        else:
            print('A point inside a circle')

    def tangent_line_calc(self):
        #point
        P = np.array([self.x, self.y, 1])
        #circle https://bit.ly/37tF5ix
        L = np.array([[1, 0, -self.cx], [0, 1, -self.cy],
                      [-self.cx, -self.cy, self.cx ** 2 + self.cy ** 2 - self.r ** 2]])

        C = L.dot(P)
        return C[0], C[1], C[2] #tangent line Ax + By + C = 0

    def intersect_calc(self, a, b, c):
        #precalculated coefs from
        '''
        {
            (x - cx)^2 + (y - cy)^2 - r^2 = 0, //the equation of the circle
            ax + by + c = 0 //tangent line
        }
        '''

        g1 = -2 * self.cx
        g2 = -2 * self.cy
        g3 = self.cx ** 2 + self.cy ** 2 - self.r ** 2

        coef1 = b ** 2 + a ** 2
        coef2 = 2 * b * c - a * b * g1 + g2 * a ** 2
        coef3 = c ** 2 - a * c * g1 + a ** 2 * g3

        #coef1 * y^2 + coef2 * y + coef3 = 0
        y1, y2 = np.roots([coef1, coef2, coef3])
        x1 = (-b * y1 - c) / a
        x2 = (-b * y2 - c) / a
        return x1, y1, x2, y2

    def draw(self):
        a, b, c = self.tangent_line_calc()
        line1_x, line1_y, line2_x, line2_y = self.intersect_calc(a, b, c)

        pt = Point(self.x, self.y)
        pt.draw(self.win)

        cir = Circle(center=Point(self.cx, self.cy), radius=self.r)
        cir.draw(self.win)

        line_1 = Line(pt, Point(line1_x, line1_y))
        line_1.draw(self.win)

        line_2 = Line(pt, Point(line2_x, line2_y))
        line_2.draw(self.win)

        self.win.getMouse()
        self.win.close()