# This question was asked by ContextLogic.

# Implement division of two positive integers without using 
# the division, multiplication, or modulus operators. Return 
# the quotient as an integer, ignoring the remainder.

def divide(a, b):
    quotient = 0
    while a >= b:
        quotient += 1
        a -= b
    return quotient

print(divide(27, 3))
print(divide(1024, 64))
print(divide(10, 3))
print(divide(4, 8))