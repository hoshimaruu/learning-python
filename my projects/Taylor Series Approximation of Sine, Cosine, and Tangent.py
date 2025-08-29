# Approximation of Sine, Cosine, and Tangent using Taylor Series



# exponent
def exponent(base, exp):
    result = 1
    for i in exp:
        result *= base
    
    return result

# factorial
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

'''
    Sine Approxmiation Function:
        This functions approxiates the sine of a value using the Taylor series expansion.
        The series is defined as:
            sin(x) = x - ((x^3)/3)! + ((x^5)/5)! - ((x^7)/7)! + ...
        where n! is the factorial of n.
'''

def sinApprox(value, nth):
    sin = 0.000
    for i in range(1, nth + 1):
        term = exponent((1 if i % 2 == 0 else -1), i) * ((exponent(value, 2 * i + 1)) / (2 * i + 1))
        sin+=term
    return sin

'''
    Cosine Approximation Function:
        This function approximates the cosine of a value using the Taylor series expansion.
        The series is defined as:
            cos(x) = 1 - ((x^2)/2)! + ((x^4)/4)! - ((x^6)/6)! + ...
        where n! is the factorial of n.
'''

def cosApprox(value, nth):
    cos = 0.000
    for i in range(1, nth + 1):
        