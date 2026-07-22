# Problem 3 — Mini calculator (stretch, 40 pts)

def main():
    # decleared outside of while loop to not get reset each error was raised
    first_num = None
    operator = None
    second_num = None

    while True:
        try:
            if not first_num:   # user only need to input first_num once in the same calculation
                first_num = float(input("First number >> "))
            
            if not operator:   # user only need to input operator once in the same calculation
                operator = input("Operator (+, -, *, /) >> ")
                if operator not in ['+', '-', '*', '/']:    # if operator not part of expect value, reset it and let user input again
                    operator = None # if don't reset the "if" won't let user to input again
                    raise ValueError("Invalid input: must be one of the operator [+, -, *, /]")
                            
            if not second_num:   # user only need to input second_num once in the same calculation
                second_num = float(input("Second number >> "))
                if operator == '/' and second_num == 0:     # if divide operator and second_num (denominator) is 0,
                                                            # reset it and let user input again
                    second_num = None # if don't reset the "if" won't let user to input again
                    raise ValueError("Invalid input: denominator cannot be zero")
                
        except ValueError as e:
            error_message = str(e)
            if "could not convert string to float" in error_message:
                print("Invalid input: Input must be a number.")
            else:
                print(error_message)
        
        finally:            
            answer = calculate([first_num, operator, second_num])
            print(f"{first_num:g} {operator} {second_num:g} = {answer:g}")
            first_num, operator, second_num = reset([first_num, operator, second_num])

def reset(arr):
    for i in range(len(arr)):
        arr[i] = None
    return arr

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculate(arr):     # calculation with function dictionary
    return operations[arr[1]](arr[0],arr[2])

# def calculate(arr):   # calculation with if/elif loop
#     if arr[1] == '+':
#         return add(arr[0], arr[2])
#     elif arr[1] == '-':
#         return subtract(arr[0], arr[2])
#     elif arr[1] == '*':
#         return multiply(arr[0], arr[2])
#     elif arr[1] == '/': 
#         return divide(arr[0], arr[2])   

if __name__ == "__main__":
    main()