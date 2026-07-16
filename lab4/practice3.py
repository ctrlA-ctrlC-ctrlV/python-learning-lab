# 1.3 The `main()` pattern

def main():
    name = input("Your name >> ")

    print(greet(name))

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    main()