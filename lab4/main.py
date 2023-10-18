from lab import squares_left_integral, squares_right_integral
from lab import trapezoid_integral, Simpson_integral
from lab import Gauss3, Gauss3_extended

from prettytable import PrettyTable

left = 0.4
right = 0.9

h = [0.1, 0.01, 0.001, 0.0001, 0.00001]
with open("res.txt", "w", encoding="utf=8") as f:
    f.write("Results:\n")
    f.write("Right squares:\n")

    table = PrettyTable()
    table.field_names = ["h", "Integral"]
    for i in h:
        table.add_row([i, squares_right_integral(left, right, i)])

    f.write(table.get_string())

    f.write("\n")
    f.write("Left squares:\n")

    table = PrettyTable()
    table.field_names = ["h", "Integral"]
    for i in h:
        table.add_row([i, squares_left_integral(left, right, i)])

    f.write(table.get_string())

    f.write("\n")
    f.write("Trapezoid:\n")

    table = PrettyTable()
    table.field_names = ["h", "Integral"]
    for i in h:
        table.add_row([i, trapezoid_integral(left, right, i)])

    f.write(table.get_string())

    f.write("\n")
    f.write("Simpson:\n")

    table = PrettyTable()
    table.field_names = ["h", "Integral"]
    for i in [2, 4, 10, 1000, 10000]:
        table.add_row([i, Simpson_integral(left, right, i)])

    f.write(table.get_string())

    f.write("\n")
    f.write("Gauss:\n")

    f.write(str(Gauss3(left, right)))

    f.write("\n\n")
    f.write("Gauss_ext:\n")

    table = PrettyTable()
    table.field_names = ["h", "Integral"]
    for i in h:
        table.add_row([i, Gauss3_extended(left, right, i)])

    f.write(table.get_string())
