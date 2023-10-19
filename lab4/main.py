from lab import squares_left_integral, squares_right_integral
from lab import trapezoid_integral, Simpson_integral
from lab import Gauss3, Gauss3_extended, myf

from prettytable import PrettyTable
from scipy.integrate import quad

left = 0.4
right = 0.9

test = quad(myf, left, right)
test = test[0]

eps = [0.1, 0.01, 0.001, 0.0001, 0.000001]
with open("res.txt", "w", encoding="utf=8") as f:
    f.write("Results:\n")
    f.write("Right squares:\n")

    table = PrettyTable()
    table.field_names = ["eps", "Integral", "real_res", "compare"]
    for i in eps:
        k = squares_right_integral(left, right, i)
        table.add_row([i, k, test, abs(k - test)])

    f.write(table.get_string())

    f.write("\n")
    f.write("Left squares:\n")

    table = PrettyTable()
    table.field_names = ["eps", "Integral", "real_res", "compare"]
    for i in eps:
        k = squares_left_integral(left, right, i)
        table.add_row([i, k, test, abs(k - test)])

    f.write(table.get_string())

    f.write("\n")
    f.write("Trapezoid:\n")

    table = PrettyTable()
    table.field_names = ["eps", "Integral", "real_res", "compare"]
    for i in eps:
        k = trapezoid_integral(left, right, i)
        table.add_row([i, k, test, abs(k - test)])

    f.write(table.get_string())

    f.write("\n")
    f.write("Simpson:\n")

    table = PrettyTable()
    table.field_names = ["eps", "Integral", "real_res", "compare"]
    for i in eps:
        k = Simpson_integral(left, right, i)
        table.add_row([i, k, test, abs(k - test)])
    f.write(table.get_string())

    f.write("\n\n")
    f.write("Gauss_ext:\n")

    table = PrettyTable()
    table.field_names = ["eps", "Integral", "real_res", "compare"]
    for i in eps:
        k = Gauss3_extended(left, right, i)
        table.add_row([i, k, test, abs(k - test)])
    f.write(table.get_string())
