import math
def exp(a):
    return math.exp(a)
def log10(a):
    return math.log10(a)
def ln(a):
    return math.log(a)
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def cosec(a):
    return 1/math.sin(a)
def sec(a):
    return 1/math.cos(a)
def cot(a):
    return 1/math.tan(a)
def arcsin(a):
    return math.asin(a)
def arccos(a):
    return math.acos(a)
def arctan(a):
    return math.atan(a)
def arccosec(a):
    return math.asin(1/a)
def arcsec(a):
    return math.acos(1/a)
def arccot(a):
    return math.atan(1/a)
def hypsin(a):
    return math.sinh(a)
def hypcos(a):
    return math.cosh(a)
def hyptan(a):
    return math.tanh(a)
def factorial(a):
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result
