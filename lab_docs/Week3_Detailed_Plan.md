# Week 3 — Detailed Lab Plan

**Collections and iteration**
*Year 2 Computer Science · 2-hour lab · Instructor design document*

**Builds on:** Week 2's loops. Last week a `while` loop repeated *until a condition changed*. This week we meet the `for` loop — *do something for each item in a collection* — and the **list**, the first real data structure. The two together are the single most common shape in real code.

> **CS50P lineage.** This week mirrors CS50P's *Loops* lecture — its `range()` "meow" counting, iterating over a list of names, `len()`, and the nested-loop grid (the Mario "pyramid"). CS50P's Problem Set 2 (camelCase, Vanity Plates, twttr) mostly loops over the *characters of a string* using methods like `.isupper()`/`.lower()` — tools we don't have until Week 5 — so we borrow the loop *mechanics* and aim them squarely at **lists**, which is what this week is actually about.

---

## 1. Concept parameter

Everything on the **In-lab** list is demonstrated then drilled in the room. The **Hop** list is reached by the student unaided in the weekly challenge — each item is only a *combination* of in-lab pieces. Nothing depends on a later week.

### 1a. Covered in the main lab (taught + drilled)

| # | Concept | Concrete syntax the student must end the lab able to use |
|---|---------|----------------------------------------------------------|
| 1 | `for` + `range(n)` | `for i in range(5):` — repeat a known number of times |
| 2 | `range(a, b)` and `range(a, b, step)` | Count from a to b−1; count in steps (and downwards) |
| 3 | List literals | `[]`, `["Dune", "1984"]` — creating a collection |
| 4 | Iterating a list | `for title in books:` — the dominant real-world loop |
| 5 | `len()` | The number of items: `len(books)` |
| 6 | Indexing | `books[0]`, and negative `books[-1]` for the last |
| 7 | Slicing | `books[:3]`, `books[3:]`, `books[1:4]` — a sub-list |
| 8 | `.append()` | Growing a list one item at a time |
| 9 | Membership | `title in books`, `title not in books` |
| 10 | Accumulating over a collection | `total = total + n`; counting matches; tracking a running `longest` |
| 11 | Nested loops | A `for` inside a `for`, plus `print(char, end="")` to build a line before a final `print()` |

### 1b. The "hop" — reached alone in the weekly challenge

No new syntax — only new *combinations*:

- **A numbered listing**: `for i in range(len(shelf)): print(i + 1, shelf[i])` — the student fuses `range`, `len`, and indexing themselves to print `1. Dune / 2. 1984`.
- **Guarding the empty case**: checking `len(shelf) == 0` (or `if not shelf`) to say "your shelf is empty" before looping over nothing.
- **De-duplicating on add**: `if title not in shelf:` before `.append()` — membership + negation, both known, combined for a real purpose.
- **Merging the two structures**: dropping a growing list into last week's `while True` menu, so "Add" appends and "List all" iterates — the join is theirs to wire.
- **Imperative-mood commits** reviewed with `git log --oneline` (this week's Pro practice).

### 1c. Deliberately *out* of scope (guardrails)

Named so no problem accidentally needs them: **functions/`def`** (Week 4); **dictionaries** (Week 5) — which is *why* Shelf can still only remember a title, not title + author + year; **string methods** like `.lower()`/`.split()` (Week 5); **other list methods** (`.remove()`, `.pop()`, `.sort()`, `sorted()`, `enumerate()`) and **list comprehensions** — mentioned only as optional peeks; **files** (Week 6); **`try`/`except`** (Week 7). Every task below is solvable with the table in §1a alone.

---

## 2. Suggested 2-hour timing

| Block | Minutes | Activity |
|-------|---------|----------|
| Recap + concept demo | 30 | Live-code `for`/`range`, then build a list and show iterating, `len`, indexing, negative index, slicing, `.append()`, `in`, and a nested-loop grid |
| Practice questions | 50 | The 10 questions in §3 — one concept each, ~5 minutes apiece |
| Lab problem (begin in room) | 30 | Start the Reading List Stats tool in §4 |
| Wrap & Git | 10 | Review history with `git log --oneline`; brief the Shelf v0.3 challenge |

Same two-50s rule as before: the lab problem is ~50 minutes of effort; students *begin and progress* in the room (~30 min) and finish in self-study before the challenge.

---

## 3. Practice questions (≈50 minutes, 10 questions ≈5 min each)

Each is a small **program** with a scenario and an **exact example run** to match. They climb from raw `for`/`range` to a nested-loop synthesis, and every list operation on the week's list appears exactly once. Full text and runs are in the student handout.

| Q | Title | Concept (lead) | Skill it forces |
|---|-------|----------------|-----------------|
| 1 | count to five | `for` + `range(n)` | The plain counting loop |
| 2 | even numbers | `range(a, b, step)` | Start, stop, and a step |
| 3 | roll call | iterating a list | `for title in books:` over a literal list |
| 4 | how many? | `len()` | Report a list's length |
| 5 | first and last | indexing | `[0]` and negative `[-1]` |
| 6 | on the shelf? | membership `in` | Search a list, branch on the result |
| 7 | top three | slicing | `[:3]` and `[3:]` as two sub-lists |
| 8 | build a list | `.append()` in a loop | Grow an empty list from user input |
| 9 | reading total | accumulate over a list | Sum and average a list of numbers |
| 10 | star ratings | nested loops | A `for` inside a `for` to print rating bars |

Design notes for a co-teacher:

- **`range(5)` gives `0,1,2,3,4` — the off-by-one that bites everyone.** Q1 and Q2 exist to make students *see* that the stop value is excluded before it costs them in the lab.
- **Q8 is the pivot of the whole week.** "Start empty, append in a loop" is exactly how Shelf will collect books tonight; if a student nails only one question, make it this one.
- **Q10 (nested loops) is the conceptual peak**, and `print("*", end="")` — printing without a newline, then a bare `print()` to end the row — is the one small new print trick they need for it. It doubles as a genuinely useful star-rating display.

---

## 4. Real-world problem — "Reading List Stats" (50 min)

### Why this problem

Anyone who reads (or tracks films, or logs workouts) has wondered "how much have I got through, and what's my average?" The program is a natural home for every list-processing pattern of the week: build a list, measure it with `len`, total it with a loop, find an extreme by tracking a running best, and count the items that pass a test. It's the same shape as CS50P's number-averaging examples, aimed at something a student actually keeps.

### The task given to the student

> Write `reading_stats.py`. Keep asking for the page count of each book you've read until the user types `done`, storing each number in a list. Then report the count, total pages, average length, the longest book, and how many were "chunky" (over 400 pages).

An example run:
```
Pages in book (or 'done')? 320
Pages in book (or 'done')? 412
Pages in book (or 'done')? 180
Pages in book (or 'done')? 550
Pages in book (or 'done')? done

You logged 4 books.
Total pages: 1462
Average length: 365.5 pages
Longest book: 550 pages
Chunky books (over 400): 2
```

### Guided build (checkpoints in the handout)

1. **Start empty.** `pages = []`. *(list literal)*
2. **Collect in a loop.** A `while True` (Week 2) that reads input, `break`s on `"done"`, and otherwise `int(...)`-converts and `.append()`s. *(append + last week's menu loop)*
3. **Count them.** `len(pages)`. *(len)*
4. **Total them.** A `for` loop adding each into a `total`. *(accumulate)* — note in passing that `sum(pages)` is a built-in shortcut, but do it by hand once so the pattern sticks.
5. **Average.** `total / len(pages)`, shown with `:.1f`. *(arithmetic + formatting, Week 1)*
6. **Longest.** Loop with a running `longest`, updating it whenever a bigger value appears. *(comparison + accumulator)* — again, `max(pages)` exists, but the loop is the lesson.
7. **Count the chunky ones.** Loop with `if book > 400: chunky = chunky + 1`. *(count-with-condition)*
8. **Guard the empty case.** If the user typed `done` immediately, `len(pages)` is 0 — dividing by it would crash, so print "No books logged." instead. *(a real reason to check length first)*

### What "good" looks like

Numbers entered are stored and summarised correctly; the average matches total ÷ count; the longest is found in one pass; the chunky count is right; and an empty list is handled without dividing by zero. The deeper win: the student can now reach for the four core list-processing moves — **sum, count, find-extreme, filter-count** — which underlie a huge amount of real data code.

### Discussion prompts (if time)

- Python has `sum()`, `len()`, `max()`, `min()`. Where did you reimplement them by hand, and why is knowing the loop underneath still worth it?
- What if someone types `"lots"` for a page count? (Crashes — Week 7.)
- Could you also report the *shortest*? (Same pattern as longest, flipped — a clean stretch.)

---

## 5. Weekly challenge — "Shelf v0.3: a shelf that holds many books"

The headline upgrade of the term so far: Shelf stops being about *one* item and becomes a **list** of them.

### The brief

> Extend `shelf.py`. Keep all the books in a list and update the menu so you can add, list, and search across the whole collection.

```
--- Shelf (5 books) ---
[1] Add a book
[2] List all books
[3] Search for a book
[Q] Quit
Choose:
```

- **[1] Add a book** — ask for a title and `.append()` it to a `shelf` list. As a small guard, only add it `if title not in shelf` (say so if it's a duplicate).
- **[2] List all books** — if the shelf is empty, say so; otherwise print a **numbered** list with `for i in range(len(shelf)): print(i + 1, shelf[i])`.
- **[3] Search for a book** — ask for a title and use `in` to report whether it's on the shelf.
- **[Q] Quit** — goodbye and `break` (accept `q`/`Q`).
- Show the count in the menu header with `len(shelf)`.

### The honest limitation (by design)

Notice you can only remember each book's **title** — not its author or year. A list holds *single values*, so a book that has a title *and* an author *and* a year doesn't fit yet. That itch is exactly what **dictionaries** solve in Week 5. Don't work around it now; feeling the gap is the point.

### Constraints (keeps it in scope)

Uses only Weeks 1–3: variables, conversion, arithmetic, f-strings, comparisons, `and`/`or`/`not`, `if`/`elif`/`else`, `while True` + `break`, and lists (`[]`, `.append()`, `len`, indexing, `in`). No functions, dicts, or files yet.

### Encouraged-but-not-required stretch (learning ahead)

- *Remove a book?* Lists have `.remove()` and `.pop()` — methods we didn't formally cover. Try one out and read what it does.
- *List them alphabetically?* `sorted(shelf)` — a peek at Week 3+ tooling.
- *Remember author and year too?* You'd want each book to be more than a single value — that's a **dictionary** (Week 5). Note where it would go.
- *Cleaner numbered listing?* `enumerate()` is the idiomatic tool — an optional look ahead.

### Shelf increment

From one item to a growing collection you can add to, browse, and search. This is the data-shape the rest of the course refines: Week 5 makes each entry richer (dicts), Week 6 saves the list to disk, Week 8 turns each entry into an object.

### Pro practice — commit like a professional

Two Git habits this week: write commit subjects in the **imperative mood** — `Add search option`, not `added searching` — the convention Git itself uses; and after committing, run `git log --oneline` to read your own history back. Good history is a story of small, clearly-named changes.

### Definition of done

`shelf.py` stores books in a list, adds (without duplicates), lists them numbered, searches with `in`, shows the count in the header, handles an empty shelf gracefully, quits cleanly, and arrives as several imperative-mood Git commits.
