# Week 3 Lab — Collections and iteration

**Computer Programming (Python) · Year 2 · 2-hour lab**

---

## Goal of this lab

Last week you learned to repeat work *until a condition changed*. This week you'll do something *for each item in a collection* — the `for` loop — and meet the **list**, Python's first real data structure. By the end you'll create lists, walk through them, index and slice them, grow them with `.append()`, measure them with `len()`, and search them with `in`. Then you'll build a reading-stats tool, and grow **Shelf** from a single item into a whole collection of books.

You should leave able to:

- loop a fixed number of times with `for` and `range()`;
- create a list, iterate it, and read items by index (including `-1` for the last);
- slice a sub-list, and grow a list with `.append()`;
- measure a list with `len()` and search it with `in` / `not in`;
- accumulate a total, a count, and a running maximum across a list;
- nest one loop inside another.

**Builds on Weeks 1–2:** variables, I/O, conversion, arithmetic, f-strings, comparisons, `and`/`or`/`not`, `if`/`elif`/`else`, and `while`. Everything new is taught in the room.

> **The off-by-one to remember:** `range(5)` gives `0, 1, 2, 3, 4` — it *stops before* 5. Almost everyone trips on this once; now you won't.

---

## Part A — Practice questions (≈50 minutes)

Ten small **programs**, about five minutes each, each with an example run to match. Write each in its own file (`q1.py`, …) and run it. They build in order: Q1 is a plain counting loop; Q10 nests two loops together.

**Q1 — count to five** *(for + range)*
Print the numbers 1 to 5, one per line, using `for` and `range()`.
```
1
2
3
4
5
```

**Q2 — even numbers** *(range with a step)*
Print the even numbers from 2 to 10 using `range()` with a step of 2.
```
2
4
6
8
10
```

**Q3 — how many?** *(len)*
Using list `books = ["The Martian", "Stardust", "Blood Reaver"]` , print a sentence with `len()`.

```
You have 3 books on your shelf.
```
**Q4 — roll call** *(iterating a list)*
Start with the list `books = ["Dune", "1984", "Emma"]`. Loop over it and print each title on its own line with a dash in front.

```
- Dune
- 1984
- Emma
```

**Q5 — first and last** *(indexing)*
Using the same list, print the first title with `[0]` and the last with `[-1]` — without counting the items yourself.

```
First: Dune
Last: Emma
```

**Q6 — on the shelf?** *(membership `in`)*
Ask the user for a title, then use `in` to say whether it's in `books`.
```
Search for a title? 1984
Yes — 1984 is on your shelf.
```

**Q7 — top three** *(slicing)*
Start with `chart = ["A", "B", "C", "D", "E", "F"]`. Print the top three with a slice `[:3]`, then everything after them with `[3:]`.
```
Top three: ['A', 'B', 'C']
The rest: ['D', 'E', 'F']
```

**Q8 — build a list** *(.append() in a loop)*
Start with an empty list `titles = []`. Keep asking for a title and appending it until the user types `done`. Then print the list and how many you collected.
```
Add a title (or 'done'): Dune
Add a title (or 'done'): 1984
Add a title (or 'done'): done
You added 2 books: ['Dune', '1984']
```

**Q9 — reading total** *(accumulate over a list)*
Start with `pages = [320, 180, 540]`. Loop through it to add up the total pages, then print the total and the average (total ÷ how many), formatted to one decimal.
```
Total: 1040 pages
Average: 346.7 pages
```

**Q10 — star ratings** *(nested loops)*
Start with `ratings = [3, 5, 2]`. For each rating, print that many `*` on one line — using an inner loop and `print("*", end="")`, then a bare `print()` to end the row.
```
***
*****
**
```

---

## Part B — Lab problem: "Reading List Stats" (≈50 minutes)

*Start this in the lab; if you don't finish, complete it during self-study before you begin Part C.*

You want to know how much you've actually read this year — how many books, how many pages, your average, your longest, and how many were proper doorstops. Let's build a tool that tells you.

**Your task:** write `reading_stats.py` that collects page counts into a list and reports on them.

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

### Work through it in steps

1. **Start empty.** Create `pages = []`. *(a new, empty list)*
2. **Collect in a loop.** Use a `while True` loop: read input; if it's `done`, `break`; otherwise convert with `int()` and `.append()` it to `pages`. *(append + Week 2's menu loop)*
3. **Count.** After the loop, print `len(pages)` in a sentence. *(len)*
4. **Total.** Use a `for` loop to add every value into a `total`. *(accumulate)* — Python has `sum()`, but do it by hand once so you understand what it's doing.
5. **Average.** `total / len(pages)`, shown to one decimal with `:.1f`. *(arithmetic + f-string)*
6. **Longest.** Track a `longest` variable; loop through and update it whenever you find a bigger value. *(comparison + accumulator)*
7. **Chunky count.** Loop again and count how many are over 400 pages. *(count with a condition)*
8. **Guard the empty case.** If the user types `done` straight away, `pages` is empty — dividing by `len(pages)` would crash. Check for that first and print `No books logged.` instead. *(why len matters)*

### Check your understanding

- Where did you rebuild `sum()`, `max()`, and `len()` by hand? Why is knowing the loop underneath still worth it?
- What happens if you type `lots` instead of a number? (It crashes for now — Week 7 fixes that.)
- Could you also report the *shortest* book? It's the same idea as longest, flipped.

---

## Part C — Weekly challenge: "Shelf v0.3 — a shelf that holds many books"

Until now Shelf could only ever remember **one** item. Today it grows up: it keeps all your books in a **list**, and the menu works across the whole collection.

**Your task:** extend `shelf.py` so it stores books in a list and can add, list, and search them.

```
--- Shelf (2 books) ---
[1] Add a book
[2] List all books
[3] Search for a book
[Q] Quit
Choose:
```

Build each option:

- **[1] Add a book** — ask for a title and `.append()` it to a `shelf` list. Only add it `if title not in shelf`; if it's already there, say so.
- **[2] List all books** — if the shelf is empty, print `Your shelf is empty.` Otherwise print a **numbered** list:
  ```
  1. Dune
  2. 1984
  ```
  Build the numbering with `for i in range(len(shelf)): print(i + 1, shelf[i])`.
- **[3] Search for a book** — ask for a title and use `in` to report whether it's on the shelf.
- **[Q] Quit** — accept `q` or `Q`, print a goodbye, and `break`.
- Show the current count in the menu header using `len(shelf)`.

Wrap the whole thing in the `while True` menu loop from last week, routing the choice with `if` / `elif` / `else`.

### Notice the limitation (this is the point)

You can only store each book's **title** — there's nowhere to keep its author or year, because a list holds one value per slot. Hold that thought: **dictionaries** in Week 5 are exactly the fix. Don't hack around it now.

### Rules

Use only **Weeks 1–3**: variables, conversion, arithmetic, f-strings, comparisons, `and`/`or`/`not`, `if`/`elif`/`else`, `while True` + `break`, and lists (`[]`, `.append()`, `len`, indexing, `in`). No functions, dictionaries, or files yet.

### Optional stretch (curiosity only — not required, not marked)

- *Remove a book?* Lists have `.remove()` and `.pop()` — try one and see what it does.
- *List them alphabetically?* `sorted(shelf)` does it in one call.
- *Remember author and year too?* You'd want each entry to be more than a single value — that's a **dictionary** (Week 5).
- *Cleaner numbering?* Look up `enumerate()` — the idiomatic way to number a loop.

### Pro practice — commit like a professional

Two habits this week. Write commit subjects in the **imperative mood** — how you'd finish the sentence "This commit will…":

```
git commit -m "Add search option to Shelf"
git commit -m "Prevent duplicate books on add"
```

Not `"added search"` or `"searching stuff"`. Then run `git log --oneline` to read your history back — it should tell the story of the feature, one small step at a time.

### Done when…

`shelf.py` stores books in a list, adds without duplicates, lists them numbered, searches with `in`, shows the count in the header, handles an empty shelf gracefully, quits cleanly on `q`/`Q`, and is committed as several imperative-mood Git commits.

---

*Bring `reading_stats.py` and your updated `shelf.py` next week — Week 4 (functions) is where we carve this growing script into named, reusable pieces.*
