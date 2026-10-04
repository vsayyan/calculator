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


print(add(1,2))
print(subtract(2,1))
print(multiply(1,2))

try:
    print(divide(7, 2))
    print(divide(5, 0))
except ValueError as error:
    print("Error:", error)

print(power(2, 3))