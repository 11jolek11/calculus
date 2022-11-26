#!/usr/bin python3
# -*- coding: utf-8 -*-
import random
import math


class MonteCarlo:
    """
    Integrating using Monte Carlo method.
    Supports some of elementary functions
    """
    xp = 0
    xk = 0
    dx = 0
    i = 0
    n = 0
    formula = ""

    def __init__(self, xp, xk, formula, n=100000):
        self.formula = formula
        for _ in self.formula:
            self.formula.replace('\n', '')
        self.n = n
        self.xp = xp
        self.xk = xk
        self.dx = (self.xk - self.xp)/n

    def fx(self):
        """
        Function fx represents function f(x) provided by user
        """
        return eval("lambda x:" + self.formula, math.__dict__)
        # return lambda x: eval(self.formula)

    def start(self):
        """
        Starts calculating value.
        """
        s = 0
        for i in range(self.n):
            if i <= self.n-2:
                temp = s
                r = random.uniform(self.xp, self.xk)
                func = self.fx()
                s = temp + func(r)
            else:
                s = (s/self.n)
        return s


if __name__ == "__main__":
    test_object = MonteCarlo(0, 1, "sin(x)")
    print(test_object.start())
