# 1.2 `return` vs. `print` — the most important distinction today

# printing within function
def square_print(n):
    print(n*n)

square_print(2)

# printing from the return value
def square(n):
    return n*n

t = square(4) + square(5)
print(t)