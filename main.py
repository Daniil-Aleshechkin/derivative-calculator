import polynomial

equation = input("Enter equation: ")

polynomial = polynomial.Polynomial(equation)

print("{} is the derivative of {}".format(polynomial.derive().toStr(),equation))