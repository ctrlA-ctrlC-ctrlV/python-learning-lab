# Lab 4 — Functions & Exceptions
## Instructor / Facilitator Plan

**Course:** Python for New Grads — Interactive Onboarding
**Module:** Lab 4 (first "logic-complexity" lab)
**Duration:** 3.5 hours (half-day session)
**Prerequisites:** Labs 1–3 (variables & types, operators & I/O, conditionals & loops)
**Design reference:** Harvard CS50's *Introduction to Programming with Python* (Weeks 2–3: Loops, Exceptions; function decomposition themes throughout)

---

## 1. Where this lab sits in the arc

Labs 1–3 were about *reading and writing correct syntax*: a learner could follow a straight line of statements and produce output. Lab 4 is the pivot point. From here on, we stop asking "does the code run?" and start asking "**is the code organized, reusable, and resilient?**"

Two ideas do that work:

- **Functions** let learners *decompose* a problem — break one big script into named, testable pieces. This is the single biggest jump in "thinking like an engineer."
- **Exceptions** force learners to reason about the *unhappy path* — what happens when input is wrong, missing, or malicious. Real programs spend most of their code here.

By the end, a learner should be able to take a vague problem statement, split it into functions, validate input, and fail gracefully. That is the mental model every later lab builds on.

---

## 2. Learning objectives

By the end of Lab 4, each learner can:

1. **Define and call functions** with positional parameters and return values.
2. Explain the difference between **`return` and `print`**, and why returning is what makes a function reusable.
3. Use the **`def main(): ... main()`** top-level pattern and understand scope (local vs. global) at a working level.
4. Give functions **default parameter values** and call them with **keyword arguments**.
5. Wrap risky code in **`try` / `except`** and catch specific exceptions (`ValueError`, `ZeroDivisionError`, `KeyError`).
6. Use **`else` and `finally`** clauses appropriately.
7. **Raise** exceptions deliberately (`raise ValueError(...)`) to enforce a function's contract.
8. Build a **re-prompt loop** that keeps asking until the user gives valid input — the canonical CS50 pattern.
9. Decompose a multi-step problem into a small set of cooperating functions, each doing one thing.

**Non-goals (explicitly out of scope, save for later labs):** custom exception classes, classes/OOP, decorators, `*args`/`**kwargs`, unit-testing frameworks, file I/O. Keep learners from rabbit-holing on these.

---

## 3. Timing at a glance

| Block | Topic | Time | Format |
|------:|-------|------|--------|
| 0 | Welcome & recap quiz | 15 min | Instructor-led |
| 1 | Functions: def, call, return | 35 min | Live-code + follow-along |
| 2 | Guided Exercise A (temperature) | 25 min | Pairs |
| — | **Break** | 10 min | — |
| 3 | Parameters, defaults, scope | 30 min | Live-code |
| 4 | Exceptions: try/except/else/finally | 35 min | Live-code + follow-along |
| 5 | Guided Exercise B (safe divider) | 20 min | Pairs |
| — | **Break** | 10 min | — |
| 6 | Problem Set (3 graded problems) | 60 min | Individual |
| 7 | Wrap-up, walkthrough, Q&A | 20 min | Instructor-led |
| | **Total** | **~3h 40m** | |

If running short on time, cut Problem 3 to a take-home (it is the stretch problem) and shorten Block 7.

---

## 4. Block-by-block facilitation notes

### Block 0 — Recap quiz (15 min)
Warm up and surface gaps from Labs 1–3. Ask verbally or via a shared doc:

- What does `int(input(...))` do, and what breaks if the user types `"cat"`? *(Sets up the whole exceptions section — let them feel the pain before you name it.)*
- Predict the output of a 3-line `for` loop with an `if` inside.
- What is the difference between `=` and `==`?

**Facilitator tip:** When someone says `int("cat")` "crashes," write the actual `ValueError` traceback on the board. Tell them: "By the end of today, you'll make that never crash a user." Motivation set.

### Block 1 — Functions (35 min)
Live-code, learners follow along in their own editor. Progression:

1. Start with a repeated block of code (e.g., greeting three different names) — the *pain* of repetition.
2. Extract it into `def greet(name):`. Show the call.
3. Introduce **`return`** by contrasting two versions:
   ```python
   def square_print(n):
       print(n * n)        # does something, gives nothing back

   def square(n):
       return n * n        # gives a value back you can reuse
   ```
   Then: `total = square(4) + square(5)`. This *cannot* work with the print version. That contrast is the "aha."
4. Introduce the `main()` pattern and call it at the bottom.

**Common misconception to pre-empt:** learners confuse *printing* with *returning*. Hammer it: a function that only prints is a dead end; a function that returns is a Lego brick.

### Block 2 — Guided Exercise A (25 min, pairs)
Learners write `fahrenheit_to_celsius(f)` and a `main()` that reads a temperature and prints the converted value. Full spec in the student handout. Circulate. Look for: forgetting `return`, printing inside the converter instead of returning.

### Block 3 — Parameters, defaults, scope (30 min)
Live-code:

- Multiple parameters, order matters.
- **Default values:** `def greet(name, greeting="Hello"):`
- **Keyword arguments:** `greet(name="Sam", greeting="Hi")` — readable and order-independent.
- **Scope:** a variable created inside a function does not exist outside it. Demonstrate the `NameError` on purpose. Keep it practical; don't lecture on the LEGB rule.

### Block 4 — Exceptions (35 min)
This is the conceptual heart of the lab. Live-code:

1. Reproduce the `ValueError` from `int("cat")`.
2. Wrap it:
   ```python
   try:
       age = int(input("Age: "))
   except ValueError:
       print("That's not a whole number.")
   ```
3. Add **`else`** (runs only if no exception) and **`finally`** (always runs).
4. Show **catching a specific** exception vs. a bare `except:` — explain why bare except is a code smell (it hides bugs).
5. Introduce **`raise`**: a function enforcing its own rules.
   ```python
   def set_age(age):
       if age < 0:
           raise ValueError("Age cannot be negative")
       return age
   ```
6. Build the **re-prompt loop** — the pattern they'll reuse constantly:
   ```python
   def get_positive_int(prompt):
       while True:
           try:
               value = int(input(prompt))
               if value <= 0:
                   raise ValueError
               return value
           except ValueError:
               print("Please enter a positive whole number.")
   ```
   Trace it out loud twice: once with good input, once with `"cat"` then `-3` then `5`.

**Facilitator tip:** Many learners try to catch *all* errors with one broad handler. Reinforce "catch the specific thing you expect; let real bugs surface."

### Block 5 — Guided Exercise B (20 min, pairs)
`safe_divide(a, b)` that returns the quotient but handles division by zero. Then a `main()` re-prompt loop. Spec in handout.

### Block 6 — Problem Set (60 min, individual)
Three problems, increasing difficulty (see Section 5 for solutions and rubric). Learners work solo; facilitators answer clarifying questions but don't hand out logic. Encourage them to write the function signature and a docstring first, then fill in the body — spec-first thinking.

### Block 7 — Wrap-up (20 min)
Walk through Problem 1 and 2 solutions live. Ask a volunteer to share their `get_positive_int`. Preview Lab 5 (lists & dictionaries — "now that you can build reliable functions, let's give them real data to chew on"). Collect submissions.

---

## 5. Problem Set — reference solutions & rubric

All three problems are in the student handout with full specs. Reference solutions below.

### Problem 1 — Grade classifier (warm-up, 25 pts)

```python
def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    while True:
        try:
            score = int(input("Score (0-100): "))
            print(f"Grade: {letter_grade(score)}")
            break
        except ValueError as error:
            print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
```

**Rubric (25):** function returns rather than prints (6) · correct boundaries incl. 90/80/70/60 (7) · raises `ValueError` for out-of-range (6) · re-prompt loop handles both non-numeric and out-of-range (6).

### Problem 2 — Tip calculator with validation (core, 35 pts)

```python
def calculate_tip(bill, percent=15):
    if bill < 0:
        raise ValueError("Bill cannot be negative")
    if percent < 0:
        raise ValueError("Tip percent cannot be negative")
    return bill * percent / 100


def get_float(prompt, allow_blank=False):
    while True:
        raw = input(prompt).strip()
        if allow_blank and raw == "":
            return None
        try:
            return float(raw)
        except ValueError:
            print("Please enter a number.")


def main():
    bill = get_float("Bill amount: $")
    while bill < 0:
        print("Bill cannot be negative.")
        bill = get_float("Bill amount: $")

    percent = get_float("Tip percent (blank = 15): ", allow_blank=True)
    if percent is None:
        tip = calculate_tip(bill)
    else:
        tip = calculate_tip(bill, percent)

    print(f"Tip: ${tip:.2f}")
    print(f"Total: ${bill + tip:.2f}")


if __name__ == "__main__":
    main()
```

**Rubric (35):** `calculate_tip` uses a default parameter (7) · raises on negative inputs (6) · reusable `get_float` input helper (8) · correctly applies default when tip left blank (7) · output formatted to 2 decimals (4) · clean decomposition, no duplicated input logic (3).

### Problem 3 — Mini calculator / stretch (challenge, 40 pts)

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a number, try again.")


def get_operator():
    while True:
        op = input("Operator (+, -, *, /): ").strip()
        if op in OPERATIONS:
            return op
        print("Unknown operator.")


def main():
    a = get_number("First number: ")
    op = get_operator()
    b = get_number("Second number: ")
    try:
        result = OPERATIONS[op](a, b)
        print(f"{a} {op} {b} = {result:g}")
    except ZeroDivisionError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
```

**Rubric (40):** four arithmetic functions each returning a value (8) · `divide` raises `ZeroDivisionError` (6) · dictionary dispatch mapping operators to functions (10) · reusable input helpers with re-prompt loops (8) · division-by-zero handled at call site without crashing (5) · overall decomposition & readability (3).

**Note on the dispatch dict:** storing *functions as values* is the intended stretch — it previews first-class functions. If a learner instead writes an if/elif chain that works and validates correctly, award full functional credit; the dict is a bonus concept, not a gate.

---

## 6. Grading summary

| Item | Points |
|------|-------:|
| Guided Exercise A (completion) | 10 |
| Guided Exercise B (completion) | 10 |
| Problem 1 — Grade classifier | 25 |
| Problem 2 — Tip calculator | 35 |
| Problem 3 — Mini calculator (stretch) | 40 |
| **Total** | **120** |

Pass threshold: 70/120. Problem 3 is designed so that a learner can pass comfortably on Exercises + P1 + P2 alone; it rewards the faster learners without penalizing the rest.

---

## 7. Facilitator checklist

- [ ] Editors/interpreter installed and verified (from Lab 1 setup) — spot check before starting.
- [ ] Shared screen/board ready for live-coding.
- [ ] Student handout distributed (`Lab04_Student_Handout.md`).
- [ ] Starter files, if you use them, seeded in each learner's repo.
- [ ] Reference solutions **not** shared until Block 7.
- [ ] Two facilitators circulating during Block 6 if cohort > 12.

## 8. Common pitfalls cheat-sheet (for circulating)

| Symptom | Likely cause | Nudge |
|---------|--------------|-------|
| "My function prints nothing when I use its result" | Used `print` inside, expected a `return` value | "What does your function *give back*?" |
| Program crashes on bad input despite `try` | `int()` call is outside the `try` block | "Which exact line can fail? Wrap that one." |
| Bare `except:` swallowing real bugs | Over-broad handler | "Catch the specific error you expect." |
| Infinite loop in re-prompt | Missing `return` on the success path | "After valid input, how does the loop end?" |
| `NameError` on a function's local variable | Scope confusion | "That variable only lives inside the function." |

---

*End of instructor plan. Companion file: `Lab04_Student_Handout.md`.*
