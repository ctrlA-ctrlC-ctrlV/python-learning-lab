# Exercise B — Safe divider

def main():
    numerator = safe_input_float(prompt="Enter numerator >> ", condition=1)
    denominator = safe_input_float(prompt="Enter denominator >> ", condition=0)

    # from python 3.6 {var:g} will remove insignificant trailing zero
    print(f"{numerator:g}/{denominator:g}={divide(numerator, denominator):.2f}")     

def divide(a, b):   # simple divide function
    return a/b

def safe_input_float(prompt, condition=1):  # check if input is a float or non-zero float
    while True: # always loop
        try:
            user_input = float(input(prompt))   # will rais ValueError if input not float (int is a float)
            
            if condition == 0:  # will raise ValueError if "condition" flag met and input is zero
                if user_input == 0:
                    print("Must be none zero.", end=" ")    # add addtional error message before 
                                                            # ValueError message, letting user know that 
                                                            # it can't be zero
                    raise ValueError
            return user_input   # break loop
        except ValueError:
            print("Please enter a valiad float number")


if __name__ == "__main__":
    main()