def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b


def average(numbers):
    if len(numbers) == 0:
        raise ValueError("Cannot compute average of an empty list")
    return sum(numbers) / len(numbers)

def percentage(part,whole):
    if whole == 0:
        raise ValueError("Canot percentage by zero")
    return part / whole * 100

def main():
    print("add:", add(1, 2))
    print("subtract:", subtract(2, 1))
    print("multiply:", multiply(1, 2))
    print("divide:", divide(7, 2))
    print("power:", power(2, 3))
    print("modulo:", modulo(7, 3))
    print("average:", average([1, 2, 3, 4, 5, 6]))
    print("percentage:",percentage(50,200))

    try:
        divide(5, 0)
        percentage(50,0)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()