# 3.4 `else` and `finally`

try:
    age = int(input("Enter age >> "))    
except ValueError:
    print("Please enter a number!")
else:
    print(f"You have entered {age}.")
finally:
    print(f"Next year you'll be {age + 1}")