# I don't know what the problem but it solves something, but only with rounding, and other it dosen't solve 
# correctrly with and without rounding, but approximately everything's right


def solve_system(down, mid, up, f, p):

    k = mid[0]
    alp = [round(-up[1] / k, p)]
    bet = [round(f[0] / k, p)]
    res = [0 for i in range(len(f))]

    print(alp)
    print(bet)

    n = len(f)

    for i in range(1, n-1):
        k = round(mid[i] + down[i - 1] * alp[i - 1], p)
        print(k)
        alp.append(round(-up[i+1] / k, n))
        bet.append(round((f[i] - down[i - 1] * bet[i - 1]) / k, p))

        print(alp)
        print(bet)
    k = round(mid[n-1] + down[n-1] * alp[n - 2], p)
    betn = round((f[n - 1] - down[n - 1] * bet[n - 2]) / k, p)

    res[n-1] = betn


    print(betn)

    for i in range(n-2, -1, -1):
        res[i] = round(alp[i] * res[i + 1] + bet[i], p)
    
    return res

def solve_system_raw(down, mid, up, f):

    k = mid[0]
    alp = [-up[1] / k]
    bet = [f[0] / k]
    res = [0 for i in range(len(f))]

    print(alp)
    print(bet)

    n = len(f)

    for i in range(1, n-1):
        k = mid[i] + down[i - 1] * alp[i - 1]
        print(k)
        alp.append(-up[i+1] / k)
        bet.append((f[i] - down[i - 1] * bet[i - 1]) / k)

        print(alp)
        print(bet)
    k = mid[n-1] + down[n-1] * alp[n - 2]
    betn = (f[n - 1] - down[n - 1] * bet[n - 2]) / k

    res[n-1] = betn


    print(betn)

    for i in range(n-2, -1, -1):
        res[i] = alp[i] * res[i + 1] + bet[i]
    
    return res

down = [1, 1, 1, 0]
mid = [2, 10, -5, 4]
up = [0, 1, -5, 2]
f = [-5, -18, -40, -27]

print(solve_system(down, mid, up, f, 2))

a1 = -1/2
b1 = -5/2

a2 = -5/(10 + a1*1)
b2 = (-18 - 1*b1) / (10 + a1*1)

a3 = 2/(-5 + a2*1)
b3 = (-40 - 1*b2) / (-5 + a2*1)

b4 = (-27 - 1*b3) / (4 + a3*1)

print(a1, b1)
print(a2, b2)
print(a3, b3)
print(b4)

class Fraction:

    def __init__(self, up, down = 1) -> None:
        self.up = up
        self.down = down
    

    def __add__(self, other):
        if isinstance(other, Fraction):
            self.up = self.up * other.down + other.up * self.down
            self.down = self.down * other.down
        else:
            self.up = self.up + other * self.own

    def __sub__(self, other):
        if isinstance(other, Fraction):
            self.up = self.up * other.down - other.up * self.down
            self.down = self.down * other.down
        else:
            self.up = self.up - other * self.own

    def __mul__(self, other):
        if isinstance(other, Fraction):
            self.up = self.up * other.up
            self.down = self.down * other.down
        else:
            self.up *= other


    def __trudiv__(self, other):
        self.up = self.up * other.up
        self.up = self.down * other.down
            