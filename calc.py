def add(a,b):
    return a + b 

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a * b 


def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b 

def power(a,b):
    return a ** b

def modulo(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b

def average(numbers):
    if len(numbers) == 0:
        raise ValueError("Cannot list length by zero")
    return sum(numbers) / len(numbers)

try:
    print(average([1,2,3,4,5,6]))
    print(average([]))
except ValueError as error:
    print("Error:",error)

print("add:", add(1, 2))
print("sum =",subtract(2,1))
print(multiply(1,2))

try:
    print(divide(7, 2))
    print(divide(5, 0))
except ValueError as error:
    print("Error:", error)

print(power(2, 3))
print(modulo(7, 3))

