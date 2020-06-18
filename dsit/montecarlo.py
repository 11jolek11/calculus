#!/usr/bin python3
#-*- coding: utf-8 -*-

from random import randint


class MonteCarlo:
    """
    Class created for montecarlo method
     Works fine!
    """
    xp = 0
    xk = 0
    # s = 0
    dx = 0
    i = 0
    n = 0
    formula = ""
    # fx = 0

    def __init__(self, xp, xk, formula, n=1000):
        self.formula = formula
        for v in self.formula: self.formula.replace('\n', '')
        self.n = n
        self.xp = xp
        self.xk = xk
        self.dx = (self.xk - self.xp)/n

    def start(self):
        s = 0
        fx = 0
        for i in range(self.n):
            # BU: This condition never reach False!
            if i<= self.n-2:
                temp = s
                r = randint(self.xp, self.xk)
                fx = lambda x: eval(self.formula)
                s = temp + fx(r)
            else:
                # FIXM Problem with 1000x greater value can be here:
                # s = (s/self.n)*self.dx
                # s = (s)*self.dx
                s = (s/self.n)
        return s


test_object = MonteCarlo(0, 1, "x**2+2*x")
print(test_object.start())
