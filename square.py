class Square:
    """
    Class created for square method
     Works fine!
    """
    n = 1
    xp = 0
    xk = 0
    dx = 0
    temp = []
    var = []
    sum = 0
    formula = ""
    # eval()
    #  https://stackoverflow.com/questions/40828921/parsing-a-string-input-into-a-lambda-function-python
    # https://www.w3schools.com/python/python_lambda.asp

    def __init__(self, xp, xk, formula, n=1000):
        self.formula = formula
        self.n = n
        self.xp = xp
        self.xk = xk
        self.dx = (xk-xp)/n

        for i in range(self.n):
            self.temp.append(self.xp+(i/self.n)*(self.xk - self.xp))
        for a in range(self.n):
            y = lambda x: eval(self.formula)
            self.var.append(y(self.temp[a]))
        self.sum = self.dx*(sum(self.var))
        
    def start(self):
        return self.sum

test_object = Square(0, 1, "x**2+2*x")
test_object.start()