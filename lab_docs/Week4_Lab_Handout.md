# Lab 4 — Functions & Exceptions
## Student Handout

Welcome to the first lab where we care about more than "does it run." Today you'll learn to **break a problem into functions** and to **handle things going wrong** without your program crashing. These two skills are the foundation for everything that follows.

**What you'll be able to do by the end:**
- Write functions that *return* values you can reuse
- Give functions default and keyword arguments
- Catch errors with `try` / `except` so bad input never crashes your program
- `raise` your own errors to enforce a function's rules
- Build the "keep asking until the input is valid" loop you'll use forever

Work through the sections in order. Type the examples yourself — don't just read them. Then do the two guided exercises, then the problem set.

---

## Part 1 — Functions

### 1.1 Why functions?

Look at this repetition:

```python
print("Hello, Alice")
print("Hello, Bob")
print("Hello, Carol")
```

Three lines that differ only by a name. A **function** lets you write the pattern once and reuse it:

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
greet("Bob")
greet("Carol")
```

`def` *defines* the function. `name` is a **parameter** — a placeholder for whatever you pass in. Calling `greet("Alice")` runs the body with `name` set to `"Alice"`.

### 1.2 `return` vs. `print` — the most important distinction today

A function can *do* something (like print) or *give something back* (return a value). These are not the same, and mixing them up is the #1 beginner mistake.

```python
def square_print(n):
    print(n * n)          # shows it on screen, hands nothing back

def square(n):
    return n * n          # hands the value back to the caller
```

Watch why `return` matters:

```python
total = square(4) + square(5)   # 16 + 25 = 41  ✅ works
print(total)

total = square_print(4) + square_print(5)   # ❌ TypeError
```

The second line fails: `square_print` returns `None`, and you can't add `None + None` meaningfully. **Rule of thumb: a function that only prints is a dead end. A function that returns is a reusable building block.** Prefer `return`.

### 1.3 The `main()` pattern

As programs grow, we put the top-level logic in a function called `main()` and call it at the bottom:

```python
def main():
    name = input("Your name: ")
    print(greet_text(name))

def greet_text(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    main()
```

`if __name__ == "__main__":` means "only run `main()` when this file is run directly." You'll use this shape in every problem today. Don't overthink it yet — just use it as a template.

### 1.4 Scope: where a variable lives

A variable created *inside* a function exists only inside that function:

```python
def compute():
    result = 42
    return result

compute()
print(result)   # ❌ NameError: 'result' is not defined out here
```

`result` is **local** to `compute`. Once the function ends, it's gone. If you want the value outside, `return` it and catch it: `answer = compute()`.

---

## Part 2 — Parameters in depth

### 2.1 Multiple parameters (order matters)

```python
def power(base, exponent):
    return base ** exponent

power(2, 3)   # 8   → base=2, exponent=3
power(3, 2)   # 9   → base=3, exponent=2
```

The order you pass arguments maps to the order of parameters.

### 2.2 Default values

Give a parameter a fallback so callers can skip it:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

greet("Sam")              # "Hello, Sam"
greet("Sam", "Welcome")   # "Welcome, Sam"
```

Parameters *with* defaults must come after parameters *without* defaults.

### 2.3 Keyword arguments

You can name arguments at the call site. This is readable and order-independent:

```python
greet(greeting="Hi", name="Sam")   # "Hi, Sam"
```

---

## Part 3 — Exceptions (handling things going wrong)

### 3.1 The problem

Remember this from earlier labs?

```python
age = int(input("Age: "))   # user types "cat"
```

If the user types `cat`, Python throws a `ValueError` and your whole program crashes with an ugly traceback. Real programs can't do that to users.

### 3.2 `try` / `except`

Wrap the risky line and handle the failure:

```python
try:
    age = int(input("Age: "))
    print(f"Next year you'll be {age + 1}")
except ValueError:
    print("That's not a whole number.")
```

If `int()` fails, Python jumps straight to the `except` block instead of crashing. **Only wrap the line(s) that can actually fail** — keep the `try` block small so you don't accidentally hide other bugs.

### 3.3 Catch the *specific* error

```python
try:
    result = 10 / int(input("Divisor: "))
except ValueError:
    print("Please type a number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
```

Different problems, different messages. Avoid a bare `except:` that catches everything — it hides real bugs. Name the exception you expect.

### 3.4 `else` and `finally`

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Not a number.")
else:
    print(f"Thanks, you are {age}.")   # runs only if no error
finally:
    print("Done.")                      # runs no matter what
```

`else` runs when the `try` succeeded. `finally` always runs (great for cleanup).

### 3.5 Raising your own errors

Functions can enforce their own rules with `raise`:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

Now `set_age(-5)` raises a clear error the caller can catch. You're defining the *contract* of your function: "I accept non-negative ages only."

### 3.6 The re-prompt loop (memorize this shape)

The single most useful pattern today — keep asking until the input is valid:

```python
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value            # valid → return ends the loop
        except ValueError:
            print("Please enter a positive whole number.")
```

Trace it: type `cat` → caught, asks again. Type `-3` → we `raise ValueError` → caught, asks again. Type `5` → returns `5`. You'll reuse this everywhere.

---

## Part 4 — Guided Exercises

Do these in pairs. They're for practice, not a grade beyond completion.

### Exercise A — Temperature converter (25 min)

Write a function `fahrenheit_to_celsius(f)` that **returns** the Celsius value (formula: `(f - 32) * 5 / 9`). Then write `main()` that reads a Fahrenheit number and prints the Celsius value to one decimal place.

**Requirements:**
- The converter must `return`, not `print`.
- Round display to 1 decimal: `f"{c:.1f}"`.

**Expected run:**
```
Fahrenheit: 98.6
98.6°F = 37.0°C
```

### Exercise B — Safe divider (20 min)

Write `safe_divide(a, b)` that returns `a / b` but `raise`s a `ZeroDivisionError` with a friendly message when `b == 0`. Then write a `main()` that reads two numbers and prints the result, catching the zero case.

**Expected runs:**
```
Numerator: 10
Denominator: 2
10 / 2 = 5.0
```
```
Numerator: 10
Denominator: 0
Error: cannot divide by zero
```

---

## Part 5 — Problem Set (graded, ~60 min)

Work individually. For each problem: **write the function signature first**, think about what it takes in and gives back, then fill in the body. Use the `main()` template.

### Problem 1 — Grade classifier (25 pts)

Write `letter_grade(score)` that takes an integer 0–100 and **returns** a letter:

| Score | Grade |
|-------|-------|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 0–59 | F |

**Requirements:**
- `return` the letter (don't print inside the function).
- If `score` is below 0 or above 100, `raise ValueError`.
- `main()` re-prompts until it gets a valid score (handle both non-numeric input *and* out-of-range).

**Expected run:**
```
Score (0-100): 200
Invalid input: Score must be between 0 and 100
Score (0-100): abc
Invalid input: ...
Score (0-100): 85
Grade: B
```

### Problem 2 — Tip calculator (35 pts)

Write `calculate_tip(bill, percent=15)` that **returns** the tip amount (`bill * percent / 100`). The `percent` parameter must have a **default of 15**.

**Requirements:**
- `raise ValueError` if `bill` or `percent` is negative.
- Write a reusable input helper (e.g., `get_float(prompt)`) with a re-prompt loop — don't copy-paste input logic.
- If the user leaves the tip percent blank, use the default 15%.
- Print the tip and the total, each formatted to 2 decimals.

**Expected run:**
```
Bill amount: $40
Tip percent (blank = 15): 20
Tip: $8.00
Total: $48.00
```

### Problem 3 — Mini calculator (stretch, 40 pts)

Build a calculator that reads a number, an operator (`+ - * /`), and a second number, then prints the result.

**Requirements:**
- Write a separate function for each operation: `add`, `subtract`, `multiply`, `divide`. Each **returns** its result.
- `divide` must `raise ZeroDivisionError` when dividing by zero; `main()` catches it and prints a friendly message instead of crashing.
- Use reusable input helpers with re-prompt loops for both the numbers and the operator (reject unknown operators).
- **Stretch bonus:** instead of an if/elif chain to pick the operation, build a dictionary that maps each operator symbol to its function, e.g. `{"+": add, ...}`, and call it with `operations[op](a, b)`. (Storing functions as dictionary values is a real technique you'll see a lot.)

**Expected runs:**
```
First number: 6
Operator (+, -, *, /): *
Second number: 7
6 * 7 = 42
```
```
First number: 5
Operator (+, -, *, /): /
Second number: 0
Error: Cannot divide by zero
```

---

## Submission

Save each problem as its own file: `problem1.py`, `problem2.py`, `problem3.py`. Make sure each runs with `python problem1.py` and uses the `if __name__ == "__main__": main()` pattern.

## Quick reference card

```python
# Define & return
def area(w, h):
    return w * h

# Default + keyword args
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}"
greet(name="Sam")

# Handle errors
try:
    n = int(input("n: "))
except ValueError:
    print("not a number")
else:
    print("ok")
finally:
    print("always runs")

# Enforce a rule
if x < 0:
    raise ValueError("x must be >= 0")

# Re-prompt until valid
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("try again")
```

Good luck — ask a facilitator if you're stuck for more than a few minutes on *setup*; but wrestle with the *logic* yourself first. That struggle is the learning.
