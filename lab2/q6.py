# Q6 — is it reserved? (not + building a bool)

is_reserved = input("Is the book resered? (yes/no) >> ").lower().strip()

if (is_reserved=="no") is True:
    print("It's yours - borrow away.")
else:
    print("Not yours.")