class Fraction:

    def __init__(self, up, down = 1) -> None:
        self.up = up
        self.down = down
    
    def __neg__(self) -> None:
        res = Fraction(self.up, self.down)
        res.up = -res.up

        res.norm()

        return res
        
    def __add__(self, other) -> None:
        res = Fraction(self.up, self.down)
        if isinstance(other, Fraction):
            res.up = self.up * other.down + other.up * self.down
            res.down = self.down * other.down
        else:
            res.up = self.up + other * self.own

        res.norm()
        
        return res

    def __sub__(self, other) -> None:
        res = Fraction(self.up, self.down)
        if isinstance(other, Fraction):
            res.up = self.up * other.down - other.up * self.down
            res.down = self.down * other.down
        else:
            res.up = self.up - other * self.own

        res.norm()

        return res
    
    def __mul__(self, other) -> None:
        res = Fraction(self.up, self.down)
        if isinstance(other, Fraction):
            res.up = self.up * other.up
            res.down = self.down * other.down
        else:
            res.up *= other
        
        res.norm()

        return res

    def __truediv__(self, other) -> None:
        res = Fraction(self.up, self.down)
        if isinstance(other, Fraction):
            res.up = self.up * other.down
            res.down = self.down * other.up
        else:
            res.down *= other
        
        res.norm()

        return res
    
    def calculate(self):
        return self.up / self.down
    
    def norm(self):
        if self.up < 0 and self.down < 0:
            self.up = -self.up
            self.down = -self.down


def solve_system_r(down, mid, up, f):

    k = mid[0]
    alp = [-up[0] / k]

    bet = [f[0] / k]

    res = [0 for i in range(len(f))]

    n = len(f)

    for i in range(1, n-1):
        k = mid[i] + down[i] * alp[i - 1]
        alp.append(-up[i] / k)

        bet.append((f[i] - down[i] * bet[i - 1]) / k)



    bet.append((f[n - 1] - down[n - 1] * bet[n - 2]) / (down[n - 1] * alp[n - 2] + mid[n - 1]))


    res[n-1] = bet[n-1]

    for i in range(n-2, -1, -1):
        res[i] = alp[i] * res[i + 1] + bet[i]
    

    return res

def solve_system(down, mid, up, f):

    k = mid[0]
    alp = [-up[0] / k]
    print(alp[0].up, alp[0].down)
    bet = [f[0] / k]
    print(bet[0].up, bet[0].down)
    res = [0 for i in range(len(f))]

    n = len(f)

    for i in range(1, n-1):
        k = mid[i] + down[i] * alp[i - 1]
        alp.append(-up[i] / k)
        print(alp[i].up, alp[i].down)
        bet.append((f[i] - down[i] * bet[i - 1]) / k)
        print(bet[i].up, bet[i].down)


    bet.append((f[n - 1] - down[n - 1] * bet[n - 2]) / (down[n - 1] * alp[n - 2] + mid[n - 1]))
    print(bet[n-1].up, bet[n-1].down)

    res[n-1] = bet[n-1]

    for i in range(n-2, -1, -1):
        res[i] = alp[i] * res[i + 1] + bet[i]
    
    for i in range(len(res)):
        res[i] = res[i].calculate()

    return res

down = [Fraction(0), Fraction(1), Fraction(1), Fraction(1)]
mid = [Fraction(2), Fraction(10), Fraction(-5), Fraction(4)]
up = [Fraction(1), Fraction(-5), Fraction(2), Fraction(0)]
f = [Fraction(-5), Fraction(-18), Fraction(-40), Fraction(-27)]

down2 = [0, 1, 1, 1]
mid2 = [2, 10, -5, 4]
up2 = [1, -5, 2, 0]
f2 = [-5, -18, -40, -27]

print(solve_system_r(down2, mid2, up2, f2))
print(solve_system(down, mid, up, f))

# a1 = -1/2
# b1 = -5/2

# a2 = -5/(10 + a1*1)
# b2 = (-18 - 1*b1) / (10 + a1*1)

# a3 = 2/(-5 + a2*1)
# b3 = (-40 - 1*b2) / (-5 + a2*1)

# b4 = (-27 - 1*b3) / (4 + a3*1)

# print(a1, b1)
# print(a2, b2)
# print(a3, b3)
# print(b4)


            