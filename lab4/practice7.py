# 2.3 Keyword arguments

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet(name="John", greeting="Hola"))