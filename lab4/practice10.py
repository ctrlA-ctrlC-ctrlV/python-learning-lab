# 3.3 Catch the specific error

try:
    result = 10 / float(input("Divisor >> "))
    print(f"{result:.1f}")
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("Please enter a none zero number.")