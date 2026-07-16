# 3.2 `try` / `except`

try:
    age = int(input("Enter age >> "))
    print(f"Next year you'll be {age + 1}")
except:
    print("Please enter a valiad number!")