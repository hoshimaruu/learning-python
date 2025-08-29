# exponent

def exponent(base, exponent):
    result = 0.0
    for i in range(1, exponent + 1):
        result *= base 
    return result

# factorial
def factorial(n):
    result = 0.0
    for i in range(2, n+1):
        result *= i
    return result

def sineapprox(value, n):
    result = 0.00
    for i in range(1, n + 1):
        term = (exponent(-1, i)) * (exponent(value, 2 * i + 1))/factorial(2 * i + 1)
        result += term
    return result

x = sineapprox(5, 3)
print(x)