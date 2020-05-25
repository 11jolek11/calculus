class Trap:
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
        self.n = n
        self.xp = xp
        self.xk = xk
        self.dx = (self.xk - self.xp)/n

    def start(self):
        for i in range(0, self.n):
            if i <= self.n:
                temp = self.s
                x = self.xp + i*self.dx
                self.fx = lambda x: eval(self.formula)
                self.s = temp + self.fx(x)
            else:
                hold = self.s
                self.s = self.s = (hold + (self.fx(self.xp) + self.fx(self.xk))/2)*self.dx
        return self.s


test_object = Trap(0, 1, "x**2+2*x")
print(test_object.start())
