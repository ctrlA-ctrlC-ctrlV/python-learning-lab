# 2.2 Default values

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("John"))

print(greet("Paul", "Good Morning"))