# Week 1 — Detailed Lab Plan

**Setup & the shape of a Python program**
*Year 2 Computer Science · 2-hour lab · Instructor design document*

**Builds on:** Nothing — this is the foundation. Everyone leaves with a working environment and a program they wrote, ran, and committed.

---

## 1. Concept parameter

This is the contract for the week: the exact surface area of syntax. Anything on the **In-lab** list is demonstrated and drilled in the room. Anything on the **Hop** list is *not taught directly* — the student reaches it themselves by combining in-lab pieces during the weekly challenge. Nothing in either column depends on a later week.

### 1a. Covered in the main lab (taught + drilled)

These are demonstrated live, then practised in the warm-up drills and the lab problem.

| # | Concept | Concrete syntax the student must end the lab able to use |
|---|---------|----------------------------------------------------------|
| 1 | Toolchain | Open VS Code, create a `.py` file, run it (Run button / `python file.py`), and use the REPL for quick experiments |
| 2 | `print()` | `print("text")`, printing multiple values `print(a, b)`, printing a variable |
| 3 | Comments | `# this is a comment` to annotate code |
| 4 | Variables & assignment | `name = value`; reassigning; `snake_case` naming and why names matter |
| 5 | `int` | Whole-number literals: `7`, `2026` |
| 6 | `float` | Decimal literals: `3.14`, `4.0` |
| 7 | `str` | Text in quotes: `"Dune"`, `'Le Guin'` |
| 8 | `bool` | `True` / `False` — *introduced only*; it becomes useful in Week 2 with comparisons and `if`, so it is named here but not drilled |
| 9 | `type()` (REPL only) | A **look-and-see tool** for interactive mode while learning — `type(x)` to check what you're holding. Deliberately *not* a graded drill: Python is dynamically typed, so real code almost never inspects types this way |
| 10 | Arithmetic | `+ - * /` plus `//` (floor), `%` (modulo), `**` (power); precedence |
| 11 | String concatenation | Joining strings with `+`; why `"a" + 1` fails |
| 12 | f-strings | `f"You own {count} books"`; embedding an expression `f"{a + b}"` |
| 13 | f-string formatting | Fixed decimals `f"{price:.2f}"` |
| 14 | `input()` | Reading user input — and the key fact that it **always returns a `str`** |
| 15 | Type conversion | `int(x)`, `float(x)`, `str(x)` to move between types |

### 1b. The "hop" — student reaches this on their own in the weekly challenge

No new syntax. These are the *combinations* the student discovers by assembling the above without being walked through it:

- **Sequencing a full interactive program**: chaining several `input()` → `convert` → compute → `f-string` print steps into one coherent script, deciding the order themselves.
- **Choosing the right type per field**: realising a *year* should be `int`, a *rating* should be `float`, a *title* stays `str` — and converting accordingly. The lab shows one example; the challenge makes them decide for every field.
- **Designing readable formatted output**: using `\n` newlines and f-string alignment to lay out a tidy "card" — they've seen `print` and f-strings, but composing them into a layout is theirs.
- **First Git workflow**: `git init`, `git add`, `git commit -m "..."` with a meaningful message (Pro practice — guided by a one-page cheat-sheet, performed solo).

If a student attended the lab, every piece of the hop is a recombination of something they already typed. They are never asked for syntax they haven't seen.

---

## 2. Suggested 2-hour timing

| Block | Minutes | Activity |
|-------|---------|----------|
| Environment check | 10 | Confirm Python + VS Code work; fix stragglers; run a one-line `print` |
| Concept demo | 25 | Live-code through the concept table (types, arithmetic, f-strings, `input`/conversion) in the REPL and a file |
| Practice questions | 50 | The 10 questions in §3 — one concept each, ~5 minutes apiece |
| Real-world problem (begin in room) | 30 | Start the Reading-Time Estimator in §4 — guided build |
| Wrap & Git brief | 5 | Demo the first commit; set up the weekly challenge |

**Note on the two 50-minute blocks.** The practice set (~50 min) and the Reading-Time Estimator (~50 min of effort) together exceed one session. That's intentional: students **begin and meaningfully progress** on the estimator in the room (~30 min), then finish the remaining ~20 minutes during self-study *before* starting the weekly challenge. This satisfies the course's "start in the room" rule without forcing both 50-minute blocks into 120 minutes.

---

## 3. Practice questions (≈50 minutes, 10 questions ≈5 min each)

Modelled on **CS50P Problem Set 0** (Indoor Voice, Tip, Einstein, …): every question is a small *program* with a scenario and an **exact example run** the student's output should match — not an abstract "what type is this?" exercise. Types are learned the way Python actually uses them: through `input()` returning a `str` and being converted, not through inspecting literals. Each leads with one concept; they run in order from a one-liner (Q1) to a bridge into the weekly challenge (Q10). Full text and example runs are in the student handout.

| Q | Title | Concept (lead) | Skill it forces |
|---|-------|----------------|-----------------|
| 1 | hello, you | `print`, `input`, variables | Read a name, greet with it — build up from `print("hello, world")` |
| 2 | a warmer welcome | f-strings | Rewrite Q1 as an f-string; combine two inputs in one sentence |
| 3 | tip calculator | `float`, arithmetic, `:.2f` | Convert money, take a percentage, format to 2 decimals |
| 4 | split the bill | `//`, `%` | Whole share vs. leftover — where floor-div and modulo *mean* something |
| 5 | Einstein | `int` conversion, `**` | `E = m·c²` — exponent in a real formula, not `2 ** 10` in a vacuum |
| 6 | how long alive | arithmetic, `:,` | Multiply out days; format a big number with a thousands separator |
| 7 | spine label | concatenation `+`, `str()` | Join text with `+`; hit the "can't add `str` + `int`" wall and fix it |
| 8 | the `input` trap | `input` returns a `str` | See `"3" + "4"` → `34`, then fix with `int()` |
| 9 | pocket calculator | synthesis | input → `int` → arithmetic → f-string, end to end |
| 10 | one-line catalogue entry | synthesis → challenge | Title/author/year/price into one formatted line — a dry run for Shelf |

Two deliberate design choices worth flagging to a co-teacher:

- **No `type()` drill.** Inspecting the type of a literal is a static-typing habit that doesn't transfer to idiomatic Python. `type()` still gets shown in the demo as a REPL tool for *seeing* what you hold; it just isn't graded practice.
- **Q7 and Q8 stage the two classic week-1 bugs on purpose** — `str + int` raising a `TypeError`, and `input()` concatenating instead of adding — so both are met, named, and fixed *before* the lab problem, where the same trap sits in step 3. Meeting a bug in a five-minute toy is far cheaper than meeting it for the first time inside a 50-minute build.

---

## 4. Real-world problem — "Will I finish this book in time?" (50 min)

### Why this problem

Every student has a book, episode count, or reading list they've wondered about. The **Reading-Time Estimator** answers a question they actually have ("can I finish this before the weekend?") while quietly exercising *every* concept on the week's list: input, three type conversions, four arithmetic operators, and formatted f-string output. It also sits on the course's media-library theme, so it feels like a warm-up for Shelf rather than a throwaway.

### The task given to the student

> Write a script, `reading_estimator.py`, that asks for a book's details and tells the reader how long it'll take to finish.

It should ask for: the **title**, the **total pages**, how many **pages they read per day**, and how many **minutes per page** they average. Then it prints a tidy summary: how many whole days it'll take, how many pages are left on the final day, and the total reading time in hours.

### Guided build (the steps printed for the student)

The handout walks them through it in six checkpoints, each reinforcing one idea. The point of the *solution shape* below is pedagogical — every line maps to a concept and the steps are written to make the student notice *why*.

1. **Print a header** — pure `print()`. Confidence first.
2. **Ask for the title** — `input()` into a `str`. No conversion needed; this anchors the "input is text" idea before they hit the case where it bites.
3. **Ask for total pages, then convert** — `input()` then `int()`. The handout deliberately tells them to first *try* doing arithmetic on the raw input and observe the failure/odd result, then fix it with `int()`. That contrast is the lesson: **`input()` always returns a string.**
4. **Ask for pages-per-day and minutes-per-page**, converting each — `int()` and `float()`. They now choose the type that fits the field.
5. **Do the maths** — `whole_days = total_pages // pages_per_day`, `leftover = total_pages % pages_per_day`, `total_minutes = total_pages * minutes_per_page`, `total_hours = total_minutes / 60`. This is where `//`, `%`, `*`, and `/` each earn their place, and where the difference between `//` and `/` finally *means* something ("whole days" vs "a fraction of a day").
6. **Print the summary with f-strings** — embed the title and numbers; format hours with `:.1f`. Output should read like a sentence a human would say.

### What "good" looks like

A correct program reads input, converts every numeric field, computes with the right operator for each quantity, and prints a clean, formatted, human-readable summary that names the book. The deeper win is conceptual: by the end the student can explain *why* `int()` is necessary, *why* `//` and `%` answer "how many whole days / what's left", and *why* an f-string beats gluing strings with `+`.

### Discussion prompts (if time)

- What happens if the user types `"two hundred"` for the pages? (Foreshadows week 7 error handling — note it, don't solve it.)
- Why did we use `//` for days but `/` for hours?
- Could you show the finish *date*? (You can't yet — dates need tools we meet later. Good "not yet" moment.)

---

## 5. Weekly challenge — "Shelf v0.1: your first library card"

This is the challenge problem that **extends the lab problem** and **starts the Shelf running project**. Same skills as the estimator (input → convert → format), aimed at a new target: a media item instead of a reading estimate.

### The brief

> Create `shelf.py`. Ask the user about **one** item in their media library and print it back as a neatly formatted "library card."

Collect, with the right type for each field (the student decides):

- **Title** — `str`
- **Creator** (author / director / studio) — `str`
- **Year released** — `int`
- **Your rating out of 10** — `float`
- **Hours to read / watch / play** — `float`

Then compute and show, using only week-1 tools:

- the rating as a **percentage** (`rating / 10 * 100`, formatted `:.0f%`),
- the length in **minutes** (`hours * 60`),

and print a bordered card with f-strings, for example:

```
========================================
  Dune  (1965)
  by Frank Herbert
  Rating: 8.5/10  (85%)
  Length: 21.0 hours  (1260 min)
========================================
```

### Constraints (keeps it in-scope)

Uses only week-1 concepts: variables, the four core types, `input()`, type conversion, arithmetic, and f-strings. No loops, no lists, no functions — those arrive in weeks 2–4. One item, entered once, is the whole job.

### Encouraged-but-not-required stretch (learning ahead)

Framed as optional curiosity, never marked, and explicitly flagged as "next week's material":

- *"Want a second item?"* You'd be copy-pasting the whole block — which is exactly the itch that **loops (week 2)** scratch. Feel free to copy-paste for now, or peek ahead.
- *"Want to refuse a rating above 10?"* That needs a decision (`if`) — also week 2. Note where you'd put it.

These pull the curious student toward weeks 2–4 without requiring anything beyond week 1 to get full credit.

### Shelf increment

This is Shelf's first commit: from nothing to an interactive program that models and displays a single media record. Every later week adds one capability on top of this card.

### Pro practice — first Git commit

Initialise a repo and make the first meaningful commit:

```
git init
git add shelf.py
git commit -m "Add Shelf v0.1: interactive single-item library card"
```

The habit being built: **commit working increments with a message that says what changed and why.** Graded on the *journey* — that the commit exists with a sensible message — not on polish.

### Definition of done

`shelf.py` runs, asks for all five fields, converts each to a sensible type, prints a clean formatted card with the computed percentage and minutes, and is committed to Git with a meaningful message.
