from lab import Fraction, solve_system, solve_system_r

from prettytable import PrettyTable

down = [Fraction(0), Fraction(1), Fraction(1), Fraction(1)]
mid = [Fraction(2), Fraction(10), Fraction(-5), Fraction(4)]
up = [Fraction(1), Fraction(-5), Fraction(2), Fraction(0)]
f = [Fraction(-5), Fraction(-18), Fraction(-40), Fraction(-27)]

down2 = [0, 1, 1, 1]
mid2 = [2, 10, -5, 4]
up2 = [1, -5, 2, 0]
f2 = [-5, -18, -40, -27]

sReal = solve_system_r(down2, mid2, up2, f2)
sFrac = solve_system(down, mid, up, f)

with open("res.txt", "w", encoding="utf-8") as f:
    mtrx = PrettyTable()
    mtrx.field_names = ["x1", "x2", "x3", "x4", "F"]
    mtrx.add_row([2, 1, 0, 0, -5])
    mtrx.add_row([1, 10, -5, 0, -18])
    mtrx.add_row([0, 1, -5, 2, -40])
    mtrx.add_row([0, 0, 1, 4, -27])

    f.write(mtrx.get_string())
    f.write("\n")
    f.write("Result:\n")
    f.write("\n")
    f.write("Using Real numbers:\n")
    for i in sReal:
        f.write(str(i))
        f.write(" ")
    f.write("\n")
    f.write("\n")
    f.write("Using Fractions:\n")
    for i in sFrac:
        f.write(str(i))
        f.write(" ")
