from math import cos, sin, pi

def myfunc(x):
    return x*x - cos(0.5*pi*x)

def LagrangeN(a, b, n):
    h = (b - a) / (n + 1)

    print(h)
    def inner(x):
        xn = []

        for i in range(n):
            xn.append(round(a + h * i, 2))
        xn.append(b)

        print(xn)

        res = 0
        for i in range(n + 1):
            k = myfunc(xn[i])
            for j in range(n + 1):
                if i != j:
                    k *= (x - xn[j]) / (xn[i] - xn[j])

            res += k

        return res

    return inner

test = 0.6

lag = LagrangeN(0.4, 0.9, 2)
print(myfunc(test))
print(lag(test))
