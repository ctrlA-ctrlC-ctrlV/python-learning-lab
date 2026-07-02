# Q1 — bigger, smaller, equal (comparisons + if/elif/else)
# Ask for two whole numbers and say how the first compares to the second.

x = int(input("x >> "))
y = int(input("y >> "))

if x > y:
    print("x is biger than y")
elif x < y:
    print("x is less than y")
else:
    print("x is the same as y")