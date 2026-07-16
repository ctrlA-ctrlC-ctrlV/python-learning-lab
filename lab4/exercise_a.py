# Exercise A — Temperature converter

def main():
    f = get_float(prompt="Enter temperatur in fahernheit (°F) >> ")
    c = fahernheit_to_celsius(f)
    print(f"{f:.1f}°F = {c:.1f}°C")

def get_float(prompt):  # take display prompt until the user input is a float
    while True:
        try:
            a_float = float(input(prompt))
            return a_float
        except ValueError:
            print("Please enter a valiad float number")

def fahernheit_to_celsius(f):   # convert temperature in fahernheit to celsius
    c = (f-32)*5/9
    return(c)

if __name__ == "__main__":
    main()