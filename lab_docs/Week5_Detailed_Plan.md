# Lab 5 — Dictionaries & Modelling Records
## Instructor / Facilitator Plan

**Course:** Python for New Grads — Interactive Onboarding
**Module:** Lab 5
**Duration:** 3.5 hours (half-day session)
**Prerequisites:** Labs 1–4 (variables & types; operators & I/O; conditionals & loops; **functions & exceptions**)
**Design reference:** Harvard CS50's *Introduction to Programming with Python* (dictionaries introduced within the Loops week; counting/tallies and record-modelling patterns)

---

## 1. Where this lab sits in the arc

Lab 3 gave learners the **list** — an *ordered* pile of values reached by position (`books[0]`). Lab 4 gave them **functions** to organise logic. Lab 5 gives them the **dictionary** — values reached by a *meaningful key* (`contact["phone"]`) instead of a number nobody can remember.

The real leap this week is **modelling**. A list of plain values can't say that `"Alice"` *has* the phone number `"555-1234"` — the association is lost. A dictionary captures exactly that: a set of labelled fields describing one thing. And the moment you need *many* such things — a whole address book, a product catalog, a gradebook — you reach for the pattern that carries the rest of the course: the **list of dictionaries**, our stand-in for a table of records.

By the end, a learner should look at "a book has a title, an author, and a year" and reach naturally for `{"title": ..., "author": ..., "year": ...}`, then store many of them in a list and write functions that search and summarise the collection. That data model is the backbone of Labs 6+ (files, then classes).

---

## 2. Learning objectives

By the end of Lab 5, each learner can:

1. **Create a dictionary** with `{key: value}` and read a value by key.
2. Explain when a **dictionary beats a list** — labelled fields vs. positional slots.
3. **Add, update, and remove** entries (`d[k] = v`, `del`, `.pop()`).
4. Safely read a possibly-missing key with **`.get(key, default)`** and test membership with **`key in d`** — and connect the alternative (a raw `d[k]` on a missing key) to the **`KeyError`** from Lab 4.
5. **Iterate** a dictionary with `.keys()`, `.values()`, and `.items()`.
6. Build the **counting / tally pattern** (`counts[x] = counts.get(x, 0) + 1`) — the single most reused dict idiom.
7. Model a record as a dictionary and store many in a **list of dictionaries**.
8. Use the string methods **`.lower()`, `.strip()`, `.split()`** to search records robustly (case- and whitespace-insensitive).
9. Write **functions** (from Lab 4) that take a collection and return a computed answer — average, maximum, a match, a report.

**Non-goals (out of scope — save for later):** nested dicts more than one level deep, dictionary comprehensions, `collections.Counter`/`defaultdict`, sorting theory, JSON/files (Lab 6), classes (Lab 8). If a learner asks "isn't there a `Counter` for this?" — yes, and building it by hand this week is exactly why they'll appreciate it later.

---

## 3. Timing at a glance

| Block | Topic | Time | Format |
|------:|-------|------|--------|
| 0 | Recap quiz (lists & functions) | 15 min | Instructor-led |
| 1 | Dictionaries: create, access, update | 30 min | Live-code + follow-along |
| 2 | `.get()`, `in`, and `KeyError` | 25 min | Live-code |
| 3 | Guided Exercise A (inventory lookup) | 20 min | Pairs |
| — | **Break** | 10 min | — |
| 4 | Iterating dicts + the tally pattern | 35 min | Live-code + follow-along |
| 5 | Guided Exercise B (word frequency) | 25 min | Pairs |
| — | **Break** | 10 min | — |
| 6 | List of dictionaries + string-method search | 30 min | Live-code |
| 7 | Problem Set (3 graded problems) | 60 min | Individual |
| 8 | Wrap-up, walkthrough, Q&A | 20 min | Instructor-led |
| | **Total** | **~3h 45m** | |

If short on time, make Problem 3 a take-home (it is the stretch problem) and trim Block 8.

---

## 4. Block-by-block facilitation notes

### Block 0 — Recap quiz (15 min)
Surface the Lab 3–4 foundations this lab stacks on:

- Given `books = ["Dune", "1984"]`, how do you get the last item? *(Reinforces positional access — the thing dicts replace.)*
- What's the difference between a function that `print`s and one that `return`s? *(You'll write returning functions all lab.)*
- What exception does `int("cat")` raise? Today you'll meet its cousin, `KeyError`.

**Facilitator tip:** Write `books = ["Alice", "555-1234"]` on the board and ask "which one is the name and which is the number — and how would the *program* know?" Let them feel that a list can't express the relationship. That confusion is the motivation for dictionaries.

### Block 1 — Dictionaries: create, access, update (30 min)
Live-code, learners follow along:

1. Motivate from the board example: `contact = {"name": "Alice", "phone": "555-1234"}`.
2. Read by key: `contact["phone"]`. Contrast with `books[1]` — "which is more readable in six months?"
3. Update: `contact["phone"] = "555-9999"`. Add a new key: `contact["email"] = "a@x.com"` — same syntax; assigning to a missing key *creates* it.
4. Remove: `del contact["email"]` and `contact.pop("email")`.
5. Emphasise: **keys are unique**; assigning to an existing key overwrites.

**Common misconception:** learners expect dictionaries to be ordered by value or sorted. Clarify: modern Python preserves *insertion* order, but you access by key, not position — there is no `dict[0]`.

### Block 2 — `.get()`, `in`, and `KeyError` (25 min)
1. Show the crash: `contact["age"]` on a missing key → **`KeyError`**. Tie it explicitly to Lab 4: "same family as `ValueError` — and you already know two ways to handle it."
2. Two defences:
   - Ask first: `if "age" in contact:` (note `in` checks **keys**, not values).
   - `.get()` with a fallback: `contact.get("age", "unknown")` — no crash, returns the default.
3. When to use which: `in` when you'll branch; `.get()` when you just want a safe value.

**Facilitator tip:** Have them predict `contact.get("phone")` vs `contact.get("phone", "none")` vs `contact["phone"]` on a *present* key — all three work — then the same three on a *missing* key. The contrast makes `.get()` click.

### Block 3 — Guided Exercise A (20 min, pairs)
Inventory lookup using `.get(item, 0)` so unknown items report `0 in stock` instead of crashing. Spec in handout. Watch for: using `in` + index where a single `.get()` is cleaner; confusing key-membership with value-membership.

### Block 4 — Iterating dicts + the tally pattern (35 min)
The conceptual heart of the lab. Live-code:

1. Three ways to loop:
   ```python
   for key in counts:            # keys (default)
   for value in counts.values(): # values
   for key, value in counts.items():  # both, unpacked
   ```
   Trace each once, out loud.
2. Build the **tally pattern** from scratch — do NOT just present the finished line. Start with the problem ("count how many times each word appears"), reach for a dict, and hit the missing-key problem *first*:
   ```python
   counts[word] = counts[word] + 1      # KeyError on the first sighting!
   ```
   Then fix it with `.get`:
   ```python
   counts[word] = counts.get(word, 0) + 1
   ```
   That "first time we see a key it isn't there yet" beat is the whole lesson. Let them feel the bug before the fix.
3. Print a sorted report with `for word in sorted(counts):`.

**Facilitator tip:** This idiom appears in Problems 1 and 2 and everywhere in real code. Make everyone write it once, live, before the break.

### Block 5 — Guided Exercise B (25 min, pairs)
Word-frequency counter over a sentence the user types. Reinforces `.split()` + tally + `.items()`. Spec in handout.

### Block 6 — List of dictionaries + string-method search (30 min)
1. One record: `{"name": "Alice", "phone": "555-1234"}`.
2. Many records: `contacts = [ {...}, {...} ]` — "a table where each row is a dict."
3. Iterate and search:
   ```python
   for contact in contacts:
       if contact["name"] == query:
           ...
   ```
4. **Robust matching** with string methods — motivate by typing `" Alice "` and watching an exact match fail:
   ```python
   if contact["name"].lower() == query.strip().lower():
   ```
   `.strip()` kills stray spaces; `.lower()` makes it case-insensitive. Mention `.split()` for multi-word input.
5. Return the whole matching dict (or `None` if not found) — a Lab 4 "return a value, handle the miss" callback.

### Block 7 — Problem Set (60 min, individual)
Three problems, increasing difficulty (Section 5). Learners work solo; facilitators give hints, not logic. Push spec-first thinking: "what does each function take in, and what does it return?"

### Block 8 — Wrap-up (20 min)
Walk through Problems 1 and 2. Ask a volunteer to show their tally line. Preview Lab 6 (files: "your contact book forgets everything when the program closes — next week we make it survive"). Collect submissions.

---

## 5. Problem Set — reference solutions & rubric

All specs are in the student handout. Reference solutions below (all verified to run).

### Problem 1 — Tally counter (warm-up, 25 pts)

```python
def tally(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def main():
    words = input("Enter words separated by spaces: ").lower().split()
    counts = tally(words)
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


if __name__ == "__main__":
    main()
```

**Rubric (25):** `tally` builds and **returns** a dict, doesn't print inside (6) · correct use of `.get(item, 0) + 1` — no `KeyError` on first sighting (8) · normalises input with `.lower().split()` (5) · iterates results to print counts, sorted for stable output (6).

### Problem 2 — Contact book (core, 35 pts)

```python
def add_contact(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})


def find_contact(contacts, query):
    query = query.strip().lower()
    for contact in contacts:
        if contact["name"].lower() == query:
            return contact
    return None


def main():
    contacts = []
    while True:
        action = input("Action (add / find / quit): ").strip().lower()
        if action == "quit":
            break
        elif action == "add":
            name = input("  Name: ").strip()
            phone = input("  Phone: ").strip()
            add_contact(contacts, name, phone)
            print(f"  Added {name}.")
        elif action == "find":
            match = find_contact(contacts, input("  Name to find: "))
            if match is None:
                print("  No contact found.")
            else:
                print(f"  {match['name']}: {match['phone']}")
        else:
            print("  Unknown action.")


if __name__ == "__main__":
    main()
```

**Rubric (35):** each contact is a **dict** with named fields stored in a **list** (8) · `add_contact` and `find_contact` are separate functions operating on the list (8) · search is case- and whitespace-insensitive via `.strip().lower()` (8) · `find_contact` returns the record or `None`, and `main` handles the miss without crashing (7) · menu loop routes add/find/quit cleanly (4).

### Problem 3 — Gradebook report (stretch, 40 pts)

```python
def average(student):
    scores = student["scores"]
    if not scores:
        raise ValueError(f"{student['name']} has no scores")
    total = 0
    for s in scores:
        total += s
    return total / len(scores)


def best(student):
    top = student["scores"][0]
    for s in student["scores"]:
        if s > top:
            top = s
    return top


def class_average(students):
    total = 0
    count = 0
    for student in students:
        for s in student["scores"]:
            total += s
            count += 1
    if count == 0:
        raise ValueError("no scores at all")
    return total / count


def build_report(students):
    lines = []
    for student in students:
        lines.append(f"{student['name']:<10} avg {average(student):5.1f}  best {best(student)}")
    return "\n".join(lines)


def main():
    students = [
        {"name": "Alice", "scores": [88, 92, 79]},
        {"name": "Bob",   "scores": [70, 65, 90]},
        {"name": "Carol", "scores": [95, 100, 91]},
    ]
    print(build_report(students))
    print(f"\nClass average: {class_average(students):.1f}")


if __name__ == "__main__":
    main()
```

Expected output:
```
Alice      avg  86.3  best 92
Bob        avg  75.0  best 90
Carol      avg  95.3  best 100

Class average: 85.6
```

**Rubric (40):** each student is a dict holding a name **and a list of scores** — nested structure (8) · `average` and `best` are functions taking one student and returning a number (10) · `average` raises `ValueError` on an empty score list — reuses Lab 4 (6) · `class_average` aggregates across all students (8) · `build_report` returns a formatted multi-line string, doesn't print inside (5) · overall decomposition & readability (3).

**Note on the stretch bonus (sorting):** the handout offers an optional bonus to print the report alphabetically with `sorted(students, key=lambda s: s["name"])`. This previews the `key=` argument; award it as a bonus only. A learner who sorts a different (correct) way, or doesn't sort at all, still earns full core credit — do not gate on the lambda.

---

## 6. Grading summary

| Item | Points |
|------|-------:|
| Guided Exercise A (completion) | 10 |
| Guided Exercise B (completion) | 10 |
| Problem 1 — Tally counter | 25 |
| Problem 2 — Contact book | 35 |
| Problem 3 — Gradebook report | 40 |
| **Total** | **120** |

Pass threshold: 70/120. A learner can pass comfortably on Exercises + P1 + P2; Problem 3 rewards the faster learners without penalising the rest — same shape as Lab 4.

---

## 7. Facilitator checklist

- [ ] Editors/interpreter verified before starting.
- [ ] Shared screen/board ready for live-coding the tally pattern.
- [ ] Student handout distributed (`Week5_Lab_Handout.md`).
- [ ] Reference solutions **not** shared until Block 8.
- [ ] Two facilitators circulating during Block 7 if cohort > 12.

## 8. Common pitfalls cheat-sheet (for circulating)

| Symptom | Likely cause | Nudge |
|---------|--------------|-------|
| `KeyError` the first time a key is counted | `counts[k] + 1` on a missing key | "Is that key there *yet* the first time? What does `.get(k, 0)` give you?" |
| `.get()` returns `None` unexpectedly | No default passed | "Give `.get` a second argument — the fallback." |
| `in` "not finding" a value | `in` on a dict checks **keys**, not values | "What are you searching — keys or values?" |
| Exact-match search fails on `" Alice "` | Whitespace / case mismatch | "Normalise both sides: `.strip().lower()`." |
| Looping `for x in d` and expecting values | Default iteration yields **keys** | "Want values? `.values()`. Want both? `.items()`." |
| Reaches for `books[0]` on a dict | List habit | "Dicts have no position — what's the *key*?" |

---

*End of instructor plan. Companion file: `Week5_Lab_Handout.md`.*
