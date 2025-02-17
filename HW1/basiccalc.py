class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getsum(self):
        return self.a + self.b

    def getdiff(self):
        return self.a - self.b

    def getmult(self):
        return self.a * self.b
    
    def getlarge(self):
        if self.a < self.b:
            return self.b
        else:
            return self.a