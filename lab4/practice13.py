# 3.6 The re-prompt loop (you'll build this yourself)

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive whole number.")

print(get_positive_int("Enter a positive integer >> "))