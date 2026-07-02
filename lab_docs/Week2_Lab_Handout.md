# Week 2 Lab — Making decisions and repeating work

**Computer Programming (Python) · Year 2 · 2-hour lab**

---

## Goal of this lab

Last week your programs ran once, straight down the page. Today they learn to **choose** and to **repeat**. By the end you'll be fluent with comparisons (`==`, `<`, `>=`, …), the logical operators `and` / `or` / `not`, the `if` / `elif` / `else` ladder, and the `while` loop — including the **menu loop** (`while True` with a quit key) that keeps a program open until the user is done. You'll build a guessing game, and grow **Shelf** from a run-once card into a living, menu-driven app.

You should leave able to:

- compare values and combine conditions with `and` / `or` / `not`;
- branch with `if` / `elif` / `else`, correctly using the colon and indentation;
- repeat work with a `while` loop, using a counter and a boolean flag;
- build a `while True` menu that loops until the user quits;
- validate user input by re-asking until it's acceptable.

**Builds on Week 1:** variables, `input()`/`print()`, type conversion, arithmetic, f-strings. Everything new is taught in the room.

> **Watch the punctuation.** Every `if`, `elif`, `else`, and `while` line ends in a colon `:`, and the lines it controls are indented by 4 spaces. Get this wrong and Python stops with an `IndentationError` — that's normal, just fix the spacing.

---

## Part A — Practice questions (≈50 minutes)

Ten small **programs**, about five minutes each. Every one has a scenario and an example run to match. Write each in its own file (`q1.py`, …), run it, and try a couple of different inputs. They build in order: Q1 is one decision; Q10 is your first menu loop.

**Q1 — bigger, smaller, equal** *(comparisons + if/elif/else)*
Ask for two whole numbers and say how the first compares to the second.
```
x? 3
y? 5
x is less than y
```
Use `if x < y:` / `elif x > y:` / `else:`. Mind the colon and the indentation.

**Q2 — odd or even** *(modulo + if/else)*
Ask for a whole number and say whether it's even or odd. A number is even when `number % 2 == 0`.
```
Number? 7
7 is odd
```

**Q3 — letter grade** *(elif ladder)*
Ask for a score out of 100 and print a grade: 90+ = A, 80–89 = B, 70–79 = C, 60–69 = D, below 60 = F.
```
Score? 84
Grade: B
```

**Q4 — free entry** *(or)*
A museum is free for the very young or the retired. Ask an age and print whether entry is free — it's free if the age is under 5 **or** 65 and over.
```
Age? 70
Free entry!
```

**Q5 — just right** *(and)*
Perfect reading weather is between 15 and 25 degrees (inclusive). Ask the temperature and say whether it's just right — true when `temp >= 15 and temp <= 25`.
```
Temperature? 20
Just right for reading outside.
```

**Q6 — is it reserved?** *(not + building a bool)*
Ask "Is the book reserved? (yes/no)". Turn the answer into a boolean with `is_reserved = (answer == "yes")`, then use `if not is_reserved:` to tell the reader whether they can borrow it.
```
Is the book reserved? (yes/no) no
It's yours — borrow away.
```

**Q7 — Deep Thought** *(string ==)*
Ask for the answer to "the Great Question of Life, the Universe, and Everything." If they type exactly `42`, print `Yes`; otherwise print `No`. Try typing `forty-two` and notice it's counted wrong — exact text matters, and we can't tidy input until later in the course.
```
What is the answer? 42
Yes
```

**Q8 — what time is it?** *(elif chain on a range)*
Ask for the hour as a whole number (0–23) and greet accordingly: 5–11 morning, 12–16 afternoon, 17–20 evening, otherwise night.
```
Hour (0-23)? 9
Good morning!
```

**Q9 — countdown** *(your first while loop)*
Ask for a starting number, then count down to 1, one per line, and finish with `Liftoff!`. Use a `while` loop and subtract 1 each time.
```
Start from? 3
3
2
1
Liftoff!
```

**Q10 — echo until quit** *(while True + break)*
Keep asking the user to say something and echo it back. When they type `quit`, stop. This is the exact skeleton of tonight's Shelf menu.
```
Say something (or 'quit'): hi
You said: hi
Say something (or 'quit'): bye
You said: bye
Say something (or 'quit'): quit
Goodbye!
```

---

## Part B — Lab problem: "Number Guessing Game" (≈50 minutes)

*Start this in the lab; if you don't finish, complete it during self-study before you begin Part C.*

The computer is thinking of a secret number and you have to guess it. After each guess it tells you whether you're too high or too low, until you get it — then it tells you how many tries it took.

**Your task:** write `guess.py` that plays this game.

An example run:
```
I'm thinking of a number between 1 and 100.
Your guess? 50
Too high!
Your guess? 25
Too low!
Your guess? 42
Correct! You got it in 3 guesses. Sharp!
```

### Work through it in steps

1. **Set the secret.** Start with `secret = 42` and a comment. *(A truly random number needs a tool we meet in Week 10 — a fixed secret is fine for learning the loop.)*
2. **Start the loop.** Create `solved = False` and a counter `guesses = 0`, then write `while not solved:` — the loop keeps going until you get it. *(while, boolean flag, not)*
3. **Read the guess.** Inside the loop, `int(input("Your guess? "))`. *(input + conversion, from Week 1)*
4. **Check the range first.** If the guess is `< 1 or > 100`, print a warning and don't count it. *(or)*
5. **Compare.** Otherwise: `if guess < secret:` → "Too low!"; `elif guess > secret:` → "Too high!"; `else:` → it's correct, so set `solved = True`. *(comparisons + if/elif/else)*
6. **Count the tries.** Add 1 to `guesses` for each real guess. *(accumulator)*
7. **Rate the player.** After the loop ends, use an `elif` ladder on `guesses`: 3 or fewer → `Sharp!`, 6 or fewer → `Not bad`, otherwise → `Got there in the end`. Print it as part of the winning message.

### Check your understanding

- What happens if you type `fifty` instead of a number? (It crashes for now — we'll defend against that in Week 7.)
- Why is a `while` loop the right tool here, rather than writing the guess code out several times?
- Where exactly does `solved` change from `False` to `True`, and why does that end the loop?

---

## Part C — Weekly challenge: "Shelf v0.2 — a menu that stays open"

Last week Shelf printed one library card and stopped. This week it becomes a program that **stays open**: it shows a menu, does what you ask, and shows the menu again — until you quit.

**Your task:** extend `shelf.py` so it runs this menu on a loop.

```
--- Shelf ---
[1] Set the item's details
[2] Show the library card
[3] Rate it (0-10)
[Q] Quit
Choose:
```

Build each option:

- **[1] Set the item's details** — ask for the five fields from Week 1 (title, creator, year, rating, hours) and store them in variables. Set a flag `has_item = True`.
- **[2] Show the library card** — print the formatted card from Week 1. But if `has_item` is still `False`, print `No item yet — choose 1 first` instead.
- **[3] Rate it** — ask for a rating and **keep re-asking with a `while` loop until it's between 0 and 10**. Then categorise it: 8 or above → `A must-read/watch`; 5 or above → `Worth your time`; below 5 → `Skip it`.
- **[Q] Quit** — accept `q` or `Q` (use `or`), print a goodbye, and `break` out of the loop.

Wrap the whole menu in `while True:` and route the user's choice with an `if` / `elif` / `else` ladder.

### Rules

Use only **Week 1–2 concepts**: variables, conversion, arithmetic, f-strings, comparisons, `and` / `or` / `not`, `if` / `elif` / `else`, and `while True` + `break`. Still just **one** item — holding several needs a list, which is next week. The only genuinely new shape is the rating validator: a small `while` loop *inside* the menu loop.

### Optional stretch (curiosity only — not required, not marked)

- *Want to store more than one item?* You'd reach for a **list** — that's Week 3. Note where it would go.
- *Want a letter typed for the rating to not crash the app?* That's **`try` / `except`** — Week 7. Assume numbers for now.
- *Curious about a tidier menu?* Python's **`match`** statement is a neat alternative to a long `if` / `elif` ladder — a peek ahead, entirely optional.

### Pro practice — commit in slices

Last week you made one meaningful commit. This week, **commit each menu option as it starts working**, so every commit leaves the program runnable:

```
git commit -m "Add menu loop with quit option"
git commit -m "Add set-details and show-card options"
git commit -m "Add rating validation and categories"
```

Small, focused commits with clear messages are exactly what a code reviewer wants to see.

### Done when…

`shelf.py` shows the menu on a loop, handles all four options, refuses to show a card before an item is set, keeps re-asking until the rating is 0–10, categorises the rating, quits cleanly on `q`/`Q`, and is committed to Git as several small, sensibly-messaged commits.

---

*Bring `guess.py` and your updated `shelf.py` next week — Week 3 (lists and `for` loops) is what finally lets Shelf hold more than one item.*
