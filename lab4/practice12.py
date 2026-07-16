# 3.5 Raising your own errors

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be lower than 0")
    return age

print(set_age(int(input("Enter age >> "))))