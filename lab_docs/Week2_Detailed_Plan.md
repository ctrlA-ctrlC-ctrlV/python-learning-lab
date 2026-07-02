# Week 2 — Detailed Lab Plan

**Making decisions and repeating work**
*Year 2 Computer Science · 2-hour lab · Instructor design document*

**Builds on:** Week 1's variables, `input()`/`print()`, type conversion, arithmetic and f-strings. Last week the program ran once, top to bottom. This week it can **choose** what to do and **repeat** work — the two ideas that turn a script into a tool.

> **CS50P lineage.** This week mirrors CS50P's *Conditionals* lecture — its "is x bigger, smaller or equal to y?" opener, the parity (`% 2`) and letter-grade ladders, and `and`/`or`/`not` — and the concrete, exactly-specified feel of its Problem Set 1 (Deep Thought, the bank greeting, time-of-day). Where CS50P reaches for `.lower()`, `.strip()`, `match`, or `def`, we don't — those land in later weeks — so the problems below get the same *spirit* within a tighter toolbox.

---

## 1. Concept parameter

Everything on the **In-lab** list is demonstrated then drilled in the room. The **Hop** list is reached by the student unaided during the weekly challenge — each item is only a *combination* of in-lab pieces. Nothing depends on a later week.

### 1a. Covered in the main lab (taught + drilled)

| # | Concept | Concrete syntax the student must end the lab able to use |
|---|---------|----------------------------------------------------------|
| 1 | Comparison operators | `==`, `!=`, `<`, `>`, `<=`, `>=` — and that they evaluate to a `bool` |
| 2 | `bool`, for real this time | `True`/`False` as the *result* of a comparison (the Week 1 "introduced only" type finally earns its keep) |
| 3 | The colon + indented block | `if ...:` then a 4-space-indented body — Python's most important new punctuation this week |
| 4 | `if` | Run a block only when a condition is true |
| 5 | `else` | The fallback block |
| 6 | `elif` | Chained, mutually exclusive choices (the letter-grade ladder) |
| 7 | `and` | Both conditions must hold: `15 <= temp and temp <= 25` |
| 8 | `or` | Either condition: `age < 5 or age >= 65` |
| 9 | `not` | Negation, and building a `bool` from a comparison: `is_reserved = (answer == "yes")` → `if not is_reserved:` |
| 10 | Modulo as a test | `n % 2 == 0` for even/odd — the classic conditional idiom |
| 11 | `while` loop | Repeat a block while a condition holds |
| 12 | Counter / accumulator | `count = count + 1`, `total = total + n` inside a loop |
| 13 | Boolean-flag loop | `solved = False` … `while not solved:` … `solved = True` |
| 14 | `while True` + `break` | The **menu-loop pattern**: loop forever, `break` on a quit condition |

### 1b. The "hop" — reached alone in the weekly challenge

No new syntax — only new *combinations*:

- **A menu dispatcher**: reading a choice and routing it with an `if`/`elif`/`else` ladder — the student wires the branches themselves.
- **A validation loop inside the menu loop**: a small `while` that re-asks until a rating is in range, nested inside the outer `while True`. Two loops, one inside the other, is theirs to assemble.
- **Guarding an action with a flag**: using a `has_item` boolean so "show the card" refuses politely before an item exists.
- **Accepting `q` or `Q`**: combining two comparisons with `or` to make the quit key case-tolerant (our stand-in for the case-cleaning we can't do until Week 5).
- **Incremental Git commits**: committing each menu option as it starts working, not one big dump at the end (this week's Pro practice).

### 1c. Deliberately *out* of scope (guardrails)

Named here so no problem accidentally requires them: **lists and `for`** (Week 3), **functions/`def`** (Week 4), the **`match` statement** and **string methods** like `.lower()`/`.strip()`/`.split()` (Week 5 / optional peek), and **`try`/`except`** for bad input (Week 7). Every task below is solvable without them.

---

## 2. Suggested 2-hour timing

| Block | Minutes | Activity |
|-------|---------|----------|
| Recap + concept demo | 30 | Live-code comparisons, `and`/`or`/`not`, the `if`/`elif`/`else` ladder, then `while`, the flag pattern, and `while True` + `break`. Hammer the colon-and-indentation rule |
| Practice questions | 50 | The 10 questions in §3 — one concept each, ~5 minutes apiece |
| Lab problem (begin in room) | 30 | Start the Number Guessing Game in §4 |
| Wrap & Git | 10 | Demo incremental commits; brief the Shelf v0.2 challenge |

**Two 50-minute blocks, same rule as Week 1.** The game is ~50 minutes of effort; students *begin and meaningfully progress* in the room (~30 min) and finish the last stretch in self-study before starting the weekly challenge.

---

## 3. Practice questions (≈50 minutes, 10 questions ≈5 min each)

CS50P-style: each is a small **program** with a scenario and an **exact example run** to match. They march through the week's concepts in order — comparison → `if`/`elif`/`else` → `or` → `and` → `not`/`bool` → string equality → longer `elif` chain → first `while` → the `while True`/`break` skeleton — so Q10 is a miniature of the challenge's menu loop. Full text and runs are in the student handout.

| Q | Title | Concept (lead) | Skill it forces |
|---|-------|----------------|-----------------|
| 1 | bigger, smaller, equal | comparisons + `if`/`elif`/`else` | The canonical first conditional — three-way branch on two numbers |
| 2 | odd or even | `%` + `if`/`else` | The parity idiom `n % 2 == 0` |
| 3 | letter grade | `elif` ladder | Ordered thresholds, mutually exclusive branches |
| 4 | free entry | `or` | `age < 5 or age >= 65` — either condition passes |
| 5 | just right | `and` | A value *between* two bounds |
| 6 | is it reserved? | `not` + building a `bool` | Turn a `== "yes"` into a boolean, then negate it |
| 7 | Deep Thought | string `==` | Exact string match; feel case-sensitivity (no `.lower()` yet) |
| 8 | what time is it? | `elif` chain on a range | Map an hour to morning/afternoon/evening/night |
| 9 | countdown | first `while` loop | A decrementing counter down to "Liftoff!" |
| 10 | echo until quit | `while True` + `break` | The menu-loop skeleton in miniature |

Design notes for a co-teacher:

- **The colon and the four spaces are the real week-2 hurdle**, more than the logic. Q1 exists mostly to make every student type a correctly-indented block once, early, and see the `IndentationError` if they don't.
- **Q7 (Deep Thought) meets case-sensitivity head-on.** `"Yes" == "yes"` is `False`, and we *can't* fix it with `.lower()` until Week 5 — so we name it honestly rather than hide it. It sets up why string-cleaning matters later.
- **Q9 → Q10 splits the two `while` shapes**: a *counter-driven* loop that ends by counting down, and an *event-driven* loop that ends on a sentinel. The lab problem then uses a third shape — a *flag-driven* loop — so students see all three.

---

## 4. Real-world problem — "Number Guessing Game" (50 min)

### Why this problem

It's the classic first loop for a reason: a guessing game is instantly understood, genuinely fun to run, and its natural shape *is* a `while` loop with an `if`/`elif`/`else` inside. One toy exercises every headline concept of the week — repetition, three-way branching, comparison, a boolean flag, a counter, and validation with `and`.

### The task given to the student

> Write `guess.py`. The program knows a secret number. It keeps asking the player to guess until they get it, telling them "too low" or "too high" each time, then reports how many guesses it took and rates the player.

An example run (secret is 42, so 3 guesses earns "Sharp!"):
```
I'm thinking of a number between 1 and 100.
Your guess? 50
Too high!
Your guess? 25
Too low!
Your guess? 42
Correct! You got it in 3 guesses. Sharp!
```

### Guided build (checkpoints in the handout)

1. **Set the secret.** `secret = 42` with a comment. Note honestly that a *random* secret needs the `random` library from Week 10 — for now it's fixed, and that's fine for learning the loop.
2. **Set up the loop with a flag.** `solved = False`, then `while not solved:` — this reuses `not` and the `bool` idea from the practice set, and gives the loop a clear reason to stop.
3. **Read and convert the guess.** `int(input(...))` — a Week 1 skill, now inside a loop.
4. **Branch on the guess.** `if guess < secret: "Too low"`, `elif guess > secret: "Too high"`, `else:` it's correct → set `solved = True`. This is the heart: comparison + `if`/`elif`/`else`.
5. **Count the guesses.** A `guesses = guesses + 1` accumulator — the pattern that reappears everywhere.
6. **Validate politely.** If the guess is out of range (`guess < 1 or guess > 100`), tell them and *don't* count it. Introduces `or` in a real guard.
7. **Rate the player after the loop.** An `elif` ladder on the guess count: `<= 3` "Sharp!", `<= 6` "Not bad", else "Got there in the end."

### What "good" looks like

The loop ends exactly when the guess is right; wrong guesses give the correct hint; out-of-range guesses are refused without ending the game or inflating the count; and the final message reports an accurate count and a sensible rating. The deeper win: the student can now explain *why* a `while` loop is the right tool ("repeat an unknown number of times until a condition changes") versus running the code once.

### Discussion prompts (if time)

- What happens if the player types `"fifty"`? (It crashes — a `ValueError`. Note it; Week 7 fixes it with `try`/`except`.)
- How would you make the secret unpredictable? (`random` — Week 10.)
- Could you cap it at, say, 7 guesses and let the house win? (A second exit condition — a good stretch.)

---

## 5. Weekly challenge — "Shelf v0.2: a menu that stays open"

Extends Week 1's single-item card by wrapping it in the **menu-loop pattern**. Same media item; now the program keeps running and lets the user act on it until they quit.

### The brief

> Extend `shelf.py`. Show a menu, do what the user picks, then show the menu again — looping until they choose Quit.

```
--- Shelf ---
[1] Set the item's details
[2] Show the library card
[3] Rate it (0–10)
[Q] Quit
Choose:
```

- **[1]** asks the five fields from Week 1 (title, creator, year, rating, hours) and stores them; set a `has_item = True` flag.
- **[2]** prints the formatted card — but if `has_item` is still `False`, it says "No item yet — choose 1 first" instead of crashing.
- **[3]** asks for a rating and **validates it in a loop**: keep re-asking while the number is outside `0`–`10`. Then categorise with an `elif` ladder: `>= 8` "must-read/watch", `>= 5` "worth your time", else "skip it."
- **[Q]** (accept `q` or `Q`) prints a goodbye and `break`s out of the loop.

### Constraints (keeps it in scope)

Still **one** item — storing many needs a list, which is next week. Uses only Week 1–2 tools: variables, conversion, arithmetic, f-strings, comparisons, `and`/`or`/`not`, `if`/`elif`/`else`, and `while True` + `break`. The rating validator is a `while` loop *inside* the menu loop — the one genuinely new structural idea, and it's just two things the student already knows, nested.

### Encouraged-but-not-required stretch (learning ahead)

- *Store more than one item?* You'd need a **list** to hold them — that's Week 3. Note where it would go; don't build it yet.
- *Stop a letter from crashing the rating?* That's **`try`/`except`** — Week 7. Assume numbers for now.
- *Tidy the menu dispatch?* Python's **`match`** statement is a cleaner alternative to a long `if`/`elif` — an optional peek at something we'll not formally cover.

### Shelf increment

From a run-once card to a **living program**: it stays open, takes commands, guards against acting before there's data, and validates input. This is the shape every later version keeps — the menu is Shelf's front door from here on.

### Pro practice — commit in slices

Last week: one meaningful commit. This week: **commit each menu option as it starts working** — e.g. `git commit -m "Add menu loop with quit"`, then `"Add show-card option"`, then `"Add rating validation and categories"`. The habit: small, self-contained commits that each leave the program runnable, rather than one giant end-of-week dump.

### Definition of done

`shelf.py` shows the menu on a loop, handles all four options, refuses to show a card before an item is set, keeps re-asking until the rating is in `0`–`10`, categorises the rating, quits cleanly on `q`/`Q`, and arrives as several small, sensibly-messaged Git commits.
