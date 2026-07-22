# Lab 5 — Dictionaries & Modelling Records
## Student Handout

Last lab you learned to organise *logic* into functions. This lab you'll learn to organise *data*. Lists (Lab 3) hold values by **position** — `books[0]`. Dictionaries hold values by a **meaningful key** — `contact["phone"]`. That small change unlocks the way real programs describe real things.

**What you'll be able to do by the end:**
- Create dictionaries and read, add, update, and remove entries
- Look up possibly-missing keys safely with `.get()` and `in` (and recognise `KeyError` from Lab 4)
- Loop over a dictionary's keys, values, or both
- Count things with the tally pattern — the most reused dict idiom there is
- Model a record as a dictionary and store many in a **list of dictionaries**
- Search those records robustly with `.lower()`, `.strip()`, and `.split()`

Work through the sections in order and type the examples yourself. Where you see a skeleton with blanks (`____`), the point is for **you** to fill it in — that's the learning, not the reading.

---

## Part 1 — Dictionaries

### 1.1 Why a dictionary?

Suppose you want to store a contact. With a list you'd write:

```python
contact = ["Alice", "555-1234"]
```

But now `contact[0]` is the name and `contact[1]` is the number — and nothing in the code *says so*. Six months later, was the phone at index 1 or 2? A **dictionary** labels each value:

```python
contact = {"name": "Alice", "phone": "555-1234"}
```

Each entry is a **key** (`"name"`) paired with a **value** (`"Alice"`). You read a value by its key:

```python
print(contact["name"])    # Alice
print(contact["phone"])   # 555-1234
```

`contact["phone"]` says what it means. `contact[1]` never did.

### 1.2 Add, update, remove

Assigning to a key sets it — creating the key if it's new, overwriting if it exists:

```python
contact["phone"] = "555-9999"   # update existing
contact["email"] = "a@x.com"    # add a brand-new key
```

Remove with `del` or `.pop()`:

```python
del contact["email"]
contact.pop("email")            # same effect
```

**Keys are unique.** There is no `dict[0]` — dictionaries have no position, only keys. Don't reach for list habits here.

---

## Part 2 — Missing keys, safely

### 2.1 The crash

Reading a key that isn't there raises an error you'll recognise from Lab 4:

```python
print(contact["age"])   # ❌ KeyError: 'age'
```

`KeyError` is `ValueError`'s cousin. You already know two ways to deal with a missing thing — here they are for dicts.

### 2.2 Ask first with `in`

```python
if "age" in contact:
    print(contact["age"])
else:
    print("No age on file.")
```

Note: `in` checks the **keys** of a dictionary, not the values.

### 2.3 Or use `.get()` with a fallback

```python
contact.get("age")            # None if missing — no crash
contact.get("age", "unknown") # your own fallback if missing
```

Rule of thumb: use `in` when you're going to *branch*; use `.get(key, default)` when you just want a safe value to use.

---

## Part 3 — Iterating & the tally pattern

### 3.1 Three ways to loop

```python
prices = {"apple": 30, "bread": 25}

for key in prices:              # keys (this is the default)
    print(key)

for value in prices.values():   # values
    print(value)

for key, value in prices.items():   # both at once, unpacked
    print(f"{key} costs {value}p")
```

If you write `for x in prices`, `x` is a **key**. Want values? `.values()`. Want both? `.items()`.

### 3.2 The tally pattern — build it yourself

Counting how often each thing appears is *the* classic dictionary job (word counts, vote tallies, inventory). Here's the trap people hit first. Suppose you try:

```python
counts = {}
for word in words:
    counts[word] = counts[word] + 1   # ❌ what happens the FIRST time we see a word?
```

**Predict it before reading on:** the first time a word appears, is its key already in `counts`? What error do you get? (You met this error in Part 2.)

The fix uses the safe lookup you just learned. **Complete this skeleton:**

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, ____) + 1   # what fallback makes the first count correct?
```

Once it works, print the tallies. Try it with `.items()`, and try printing them in order with `for word in sorted(counts):`. This four-line pattern will follow you through the whole course — make sure you can write it from memory.

---

## Part 4 — Records: the list of dictionaries

### 4.1 One record, then many

A single dictionary describes one thing:

```python
{"name": "Alice", "phone": "555-1234"}
```

Put many of them in a list and you have a **table of records** — each dict is a row:

```python
contacts = [
    {"name": "Alice", "phone": "555-1234"},
    {"name": "Bob",   "phone": "555-9999"},
]
```

To search, loop over the list and check a field on each record:

```python
for contact in contacts:
    if contact["name"] == query:
        print(contact["phone"])
```

### 4.2 Searching robustly with string methods

Exact matching is brittle. If the user types `" alice "` (stray spaces, lowercase), `contact["name"] == query` fails even though Alice is right there. Clean both sides first:

- `.strip()` removes leading/trailing whitespace
- `.lower()` makes the comparison case-insensitive
- `.split()` breaks a string into a list of words (useful for multi-word input)

**Try each one in the REPL** on a messy string like `"  Alice Smith  "` and watch what it does before you use it. Then decide where they belong in your search: you want `"  ALICE  "` to match a stored `"Alice"`.

---

## Part 5 — Guided Exercises

Do these in pairs — practice, not graded beyond completion. No solution code is given; that's the point.

### Exercise A — Inventory lookup (20 min)

Start with an inventory dictionary, e.g. `inventory = {"apples": 12, "bread": 3}`. Ask the user for an item name and report how many are in stock — but if the item isn't tracked, report `0 in stock` instead of crashing.

**Requirements:**
- Use `.get()` with a sensible default — no `if`/`else` needed for the missing case.

**Expected runs:**
```
Item: apples
apples: 12 in stock
```
```
Item: milk
milk: 0 in stock
```

### Exercise B — Word frequency (25 min)

Ask the user for a sentence. Print how many times each word appears, case-insensitively.

**Requirements:**
- Normalise with `.lower()` and split into words with `.split()`.
- Build the counts with the tally pattern from Part 3.2 (you write it).

**Expected run:**
```
Sentence: the cat sat on the mat the cat
cat: 2
mat: 1
on: 1
sat: 1
the: 3
```
*(Order shown is sorted — printing sorted is a nice touch, not required.)*

---

## Part 6 — Problem Set (graded, ~60 min)

Work individually. For each problem, **write your function signatures first**: what does each take in, and what does it return? Then fill the bodies. Use the `main()` pattern from Lab 4.

### Problem 1 — Tally counter (25 pts)

Write a function `tally(items)` that takes a list of things and **returns** a dictionary mapping each thing to how many times it appears. Then a `main()` that reads a line of words and prints each word with its count.

**Requirements:**
- `tally` must **return** the dict (don't print inside it).
- Use the tally pattern — no `KeyError` on a word's first appearance.
- Treat words case-insensitively (`Apple` and `apple` are the same word).

**Expected run:**
```
Enter words separated by spaces: apple Banana apple APPLE banana
apple: 3
banana: 2
```

### Problem 2 — Contact book (35 pts)

Build a command-line contact book that stores contacts as a **list of dictionaries** and lets the user add and find them.

**Requirements:**
- Each contact is a dictionary with `"name"` and `"phone"` keys; all contacts live in one list.
- Write at least two functions: one to **add** a contact to the list, one to **find** a contact by name and **return** it (or `None` if there's no match).
- Search must be case- and whitespace-insensitive (finding `bob` should match a stored `Bob`).
- A menu loop offers `add`, `find`, and `quit`; a failed search prints a friendly message instead of crashing.

**Expected run:**
```
Action (add / find / quit): add
  Name: Alice Smith
  Phone: 555-1234
  Added Alice Smith.
Action (add / find / quit): find
  Name to find:  alice smith
  Alice Smith: 555-1234
Action (add / find / quit): find
  Name to find: Bob
  No contact found.
Action (add / find / quit): quit
```

### Problem 3 — Gradebook report (stretch, 40 pts)

Model a small class as a list of dictionaries, where each student has a name **and a list of scores**, then print a report.

Start from this data (you may hard-code it):
```python
students = [
    {"name": "Alice", "scores": [88, 92, 79]},
    {"name": "Bob",   "scores": [70, 65, 90]},
    {"name": "Carol", "scores": [95, 100, 91]},
]
```

**Requirements:**
- Write a function `average(student)` that **returns** that student's average score, and `raise`s a `ValueError` if the student has no scores (reuse Lab 4's `raise`).
- Write a function that returns a student's best (highest) score.
- Write a function `class_average(students)` that returns the average across *everyone's* scores.
- Print one line per student showing their name, average (one decimal), and best score, then the class average at the end.
- **Stretch bonus (optional):** print the students in alphabetical order by name. Look up how `sorted()` takes a `key=` argument — e.g. `sorted(students, key=lambda s: s["name"])`. Not required for full core credit.

**Expected output (unsorted is fine):**
```
Alice      avg  86.3  best 92
Bob        avg  75.0  best 90
Carol      avg  95.3  best 100

Class average: 85.6
```

---

## Submission

Save each problem as its own file: `problem1.py`, `problem2.py`, `problem3.py`. Each should run with `python problem1.py` and use the `if __name__ == "__main__": main()` pattern from Lab 4.

## Quick reference card

```python
# Create & read
d = {"name": "Alice", "phone": "555-1234"}
d["name"]                 # "Alice"

# Add / update / remove
d["email"] = "a@x.com"    # add or overwrite
del d["email"]            # remove

# Safe lookup (avoid KeyError)
"age" in d                # is that KEY present?
d.get("age")              # None if missing
d.get("age", "unknown")   # your fallback if missing

# Iterate
for k in d: ...           # keys
for v in d.values(): ...  # values
for k, v in d.items(): ...# both

# List of records
people = [{"name": "A"}, {"name": "B"}]
for person in people:
    ...                   # person["name"]

# Clean up input for searching
query.strip().lower()     # trim spaces, ignore case
```

**Tally pattern — the ingredients, not the recipe.** You'll write it yourself (Part 3.2): start an empty dict, loop the items, and for each one set `counts[item] = counts.get(item, ?) + 1`. Work out the fallback that makes a first-time count come out right.

Good luck — wrestle with the *logic* yourself before asking. That struggle is where the learning lives.
