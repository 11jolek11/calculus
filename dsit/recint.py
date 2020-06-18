class RecInt:
    """
    Need fixes!
    """
    # TODO: Find bug!ma
    xp = 0
    xk = 0
    s = 0
    dx = 0
    i = 0
    n = 0
    formula = ""
    fx = 0

    def __init__(self, xp, xk, formula, n=1000):
        self.formula = formula
        self.formula = self.formula.replace('^', '**')
        self.n = n
        self.xp = xp
        self.xk = xk
        self.dx = (self.xk - self.xp)/n

    def start(self):
        for i in range(self.n):
            if i <= self.n:
                temp = self.s
                x = self.xp + i*self.dx
                self.fx = lambda x: eval(self.formula)
                self.s = temp + self.fx(x)
            else:
                hold = self.s
                self.s = hold
        return self.s*self.dx




test_object = RecInt(0, 1, "x**2+2*x", 1000)
print(test_object.start())

# [5,2,10]   5x^2+2*x+10