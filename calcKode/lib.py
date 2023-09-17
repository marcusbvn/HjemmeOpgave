from math import gcd

class Rational:
    def __init__(self, num, dem):
        self.num = num
        self.dem = dem

    def __repr__(self):
        return f"{self.num}/{self.dem}"
    
    def reduce(self):
        d = gcd(self.num, self.dem)
        self.num = self.num//d
        self.dem = self.dem//d
        return str(self)

    def negate(self):
        if self.num < 0:
            self.num = abs(self.num)
        elif self.dem < 0:
            self.dem = abs(self.dem)
        else:
            self.num = -abs(self.num)
        return str(self)

    def invert(self):
        tempNum = 0
        tempNum += self.num
        tempDem = 0
        tempDem += self.dem
        self.num = tempDem
        self.dem = tempNum
        return str(self)

    def add(self, Rational):
        self.num = self.dem*Rational.num + self.num*Rational.dem
        self.dem = self.dem*Rational.dem
        return str(self)
    
    def sub(self, Rational):
        self.num = (self.num*Rational.dem) - (self.dem*Rational.num)
        self.dem = self.dem*Rational.dem
        return str(self)

    def mul(self, Rational):
        self.dem = self.dem*Rational.dem
        self.num = self.num*Rational.num
        return str(self)

    def div(self, Rational):
        self.dem = self.dem*Rational.num
        self.num = self.num*Rational.dem
        return str(self)

    def cmp(self, Rational):
        relTempDem = Rational.dem
        
        Rational.dem = self.dem*Rational.dem
        Rational.num = self.dem*Rational.num

        self.dem = self.dem*relTempDem
        self.num = self.num*relTempDem

        if self.num > Rational.num:
            return 1
        elif Rational.num > self.num:
            return -1
        else:
            return 0