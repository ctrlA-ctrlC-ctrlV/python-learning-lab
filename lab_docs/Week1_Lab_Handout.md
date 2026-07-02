# Week 1 Lab — Setup & the shape of a Python program

**Computer Programming (Python) · Year 2 · 2-hour lab**

---

## Goal of this lab

By the end of today you will have a working Python environment and you'll be fluent with the building blocks every Python program is made of: **variables**, the four core **types** (`int`, `float`, `str`, `bool`), **arithmetic**, **f-strings**, reading **input** from a user, and **converting** between types. You'll prove it by writing a real, interactive program — and you'll start **Shelf**, the personal media-library app you'll grow every week this semester.

You should leave able to:

- create, run, and experiment with a `.py` file and the REPL;
- store values in well-named variables and recognise each core type;
- do arithmetic with `+ - * / // % **`;
- read input with `input()`, convert it with `int()` / `float()` / `str()`, and display results with f-strings;
- make your first Git commit.

Everything you need is taught in the room. Nothing below requires reading ahead.

---

## Part A — Practice questions (≈50 minutes)

Ten small **programs**, about five minutes each. Every one has a scenario, a clear job, and an example run showing exactly what it should do — your program's output should match that shape. Write each in its own file (`q1.py`, `q2.py`, …), run it, and try it with a couple of different inputs before moving on. They're ordered to build on each other: Q1 is one line; Q10 is a first taste of next week's challenge.

> Reading a run: lines the user types are shown after the `?` prompt. Everything else is your program's output.

**Q1 — hello, you** *(print, input, variables)*
Ask the user for their name and greet them by it.

```
What's your name? Ada
hello, Ada
```
Start with `print("hello, world")`, then replace `world` with a `name` variable you filled from `input("What's your name? ")`.

**Q2 — a warmer welcome** *(f-strings)*
Rewrite Q1's greeting using an **f-string** instead of gluing strings together. Then ask a second question and use both answers:

```
What's your name? Ada
What are you reading? Dune
Hello, Ada — enjoy Dune!
```

**Q3 — tip calculator** *(float, arithmetic, `:.2f`)*
Ask for a meal's price and a tip percentage, then say how much to tip. Convert the inputs with `float()` and format the money to 2 decimal places.
```
Meal price? 42.50
Tip percent? 15
Leave a tip of £6.38
```

**Q4 — split the bill** *(`//` and `%`)*
A bill is paid in whole pence and split evenly. Ask for the total (in pence) and the number of people. Print how much each person pays and how many pence are left over.

```
Total pence? 1000
People? 3
Each pays 333p, with 1p left over
```

**Q5 — Einstein** *(int conversion, `**`)*
Mass turns into energy by `E = m × c²`, where `c = 300000000` m/s. Ask for a mass in kilograms and print the energy in joules.

```
Mass in kg? 2
2 kg of mass is 180000000000000000 joules
```

**Q6 — how long have you been alive?** *(arithmetic, thousands formatting)*
Ask someone's age in years and print roughly how many days that is (use `365`). Format the number with a thousands separator using `f"{days:,}"`.

```
Age in years? 30
That's about 10,950 days old.
```

**Q7 — spine label** *(concatenation with `+`, `str()`)*
Build a library spine label by joining pieces with `+` (not an f-string, on purpose). Ask for an author's surname and a year, then print `Lovelace — 1815`. You'll find you must wrap the year in `str()` before you can join it to text — try it without and read the error.

**Q8 — the `input` trap** *(input always returns a `str`)*
Ask for two numbers and add them. First do it **without** converting and notice `"3" + "4"` gives `34`, not `7`. Then fix it with `int()` so the sum is correct. Add a one-line comment explaining what went wrong the first time.

```
First number? 3
Second number? 4
Glued together: 34
Actually added: 7
```

**Q9 — pocket calculator** *(synthesis: input, int, arithmetic, f-string)*
Ask for two whole numbers `x` and `y` and print their sum as a full sentence with an f-string.

```
x? 6
y? 7
6 + 7 = 13
```

**Q10 — one-line catalogue entry** *(synthesis → bridges to Part C)*
Ask for a book's title, author, year, and price, then print a single tidy catalogue line. This is a dry run for tonight's challenge.

```
Title? Dune
Author? Frank Herbert
Year? 1965
Price? 12.5
"Dune" by Frank Herbert (1965) — £12.50
```

---

## Part B — Lab problem: "Will I finish this book in time?" (≈50 minutes)

*Start this in the lab; if you don't finish, complete it during self-study before you begin Part C.*

You just picked up a new book and want to know whether you can finish it before the weekend. Let's build a tool that tells you.

**Your task:** write a script called `reading_estimator.py` that asks for a book's details and prints how long it'll take to finish.

It should ask for:

- the **title** of the book,
- the **total pages**,
- how many **pages you read per day**,
- how many **minutes per page** you average.

Then it should print: how many **whole days** it'll take, how many **pages are left** on the final day, and the **total reading time in hours**.

### Work through it in steps

1. **Header.** Print a friendly title line, e.g. `--- Reading Time Estimator ---`. *(print)*
2. **Title.** Use `input()` to ask for the book's title and store it. No conversion needed — it's text. *(input, str)*
3. **Total pages.** Ask for the total pages with `input()`. First, *try* using the answer directly in a calculation and see what happens — then fix it by wrapping it in `int()`. Remember: **`input()` always gives you a string.** *(input, int conversion)*
4. **Reading speed.** Ask for pages-per-day (convert with `int()`) and minutes-per-page (convert with `float()` — it might be `1.5`). *(input, int, float)*
5. **Do the maths.** Calculate:
   - whole days needed → use `//` (floor division)
   - pages left on the last day → use `%` (modulo)
   - total minutes → `total_pages * minutes_per_page`
   - total hours → `total_minutes / 60`

   *(arithmetic: `//`, `%`, `*`, `/`)*
6. **Summary.** Print a clear summary using **f-strings**. Mention the book by name and format the hours to one decimal place with `:.1f`. Aim for something a person would actually say out loud, e.g.:
   `"Dune" will take about 5 days (with 30 pages on the last day) — roughly 14.6 hours of reading.`

### Check your understanding

- Why did step 3 need `int()`? What happened before you added it?
- Why `//` for days but `/` for hours?
- What would happen if someone typed `two hundred` for the pages? (You don't need to fix it today — just notice it.)

---

## Part C — Weekly challenge: "Shelf v0.1 — your first library card"

This is the first brick of **Shelf**, the media-library app you'll build all semester. It uses exactly what you practised today.

**Your task:** create `shelf.py`. Ask the user about **one** item in their media library (a book, film, or game) and print it back as a neat "library card."

Collect these, choosing a sensible type for each one yourself:

- **Title** (text)
- **Creator** — author, director, or studio (text)
- **Year released** (whole number)
- **Your rating out of 10** (can be a decimal, e.g. `8.5`)
- **Hours to read / watch / play** (can be a decimal)

Then compute and display, using only this week's tools:

- the rating as a **percentage** → `rating / 10 * 100`, shown with no decimals (`:.0f`) and a `%` sign,
- the length in **minutes** → `hours * 60`.

Print a tidy bordered card with f-strings. Something like:

```
========================================
  Dune  (1965)
  by Frank Herbert
  Rating: 8.5/10  (85%)
  Length: 21.0 hours  (1260 min)
========================================
```

### Rules

Use only **week-1 concepts**: variables, the four core types, `input()`, type conversion, arithmetic, and f-strings. One item, entered once. (No loops, lists, or functions yet — those are coming.)

### Optional stretch (curiosity only — not required, not marked)

- *Want to enter a second item?* You'd have to copy-paste the whole block. That's annoying on purpose — repeating work is what **loops** solve next week. Copy-paste for now, or peek ahead.
- *Want to reject a rating above 10?* That needs an **if-decision**, also next week. Just note where it would go.

You can earn full marks without either of these — they're a taste of where we're headed.

### Pro practice — your first Git commit

Put your challenge under version control and make a meaningful first commit:

```
git init
git add shelf.py
git commit -m "Add Shelf v0.1: interactive single-item library card"
```

From now on, every weekly challenge is submitted through Git. Good commit messages say *what changed and why* — start the habit now.

### Done when…

`shelf.py` runs, asks for all five fields, converts each to a sensible type, prints a clean formatted card with the rating percentage and length in minutes, and is committed to Git with a meaningful message.

---

*Bring your `reading_estimator.py` and `shelf.py` next week — week 2 (decisions and loops) builds straight on top of them.*
