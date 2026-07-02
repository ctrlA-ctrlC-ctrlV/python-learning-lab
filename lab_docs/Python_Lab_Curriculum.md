# Computer Programming (Python) — Lab Curriculum

**Year 2, Computer Science | 12 weeks | 2-hour weekly lab**

---

## Design philosophy

This curriculum assumes students arrive understanding *general* programming ideas (a loop is a loop, a condition is a condition) but treat **Python syntax and idiom as new**. That lets us move at pace and still land at "Junior Dev ready" by week 12.

Three commitments shape every lab:

1. **Start in the room.** Each lab opens with a concept you can demonstrate and a problem the student can begin — and meaningfully progress — inside the 2 hours. No lab depends on pre-reading to get going.
2. **Finish over the week.** Each lab ends with a *challenge* that extends the same concept introduced in class. It is larger than the in-lab task but uses nothing that wasn't covered. A student who attended the lab has everything they need.
3. **Nothing is orphaned.** Concepts are strictly incremental. Week *n* only relies on weeks *1…n-1*. The "Builds on" line in each week makes the dependency explicit, so a student who attended every session never hits an unexplained gap.

### Two tracks running in parallel

- **In-lab problems** are small, self-contained concept drills. They isolate the week's new idea so it's learned cleanly.
- **The weekly challenge** feeds a single **running project** that grows all semester: **"Shelf"**, a personal media-library command-line app. Starting as a hardcoded print statement in week 1, it accumulates one new capability per week and ends as a tested, structured, API-connected application the student can put in a portfolio. This spine is what turns twelve disconnected topics into one coherent thing they *built*.

### The professional-practices thread

Junior-dev readiness is not just syntax. From week 1, every challenge is submitted via **Git** with meaningful commit history. A small "Pro practice" item is woven into each week (commit messages → docstrings → PEP 8 → code review → READMEs) so good habits form alongside the language.

### Suggested assessment split

- Weekly challenge submissions (Git history + working code): **40%** — continuous, low-stakes, builds the project.
- Mid-semester checkpoint (end of week 7, the persistence + robustness milestone): **20%**.
- Final project submission (week 12 Shelf + short README + test suite): **40%**.

Grade the *journey* (commits, incremental progress, code quality), not just the final artifact.

---

## Week-by-week

Each week follows the same template: **Concept → Builds on → In-lab problem → Weekly challenge → Shelf increment → Pro practice.**

---

### Week 1 — Setup & the shape of a Python program

**Concept:** Toolchain (Python interpreter, VS Code, running a `.py` file, the REPL). Values, variables, the core types (`int`, `float`, `str`, `bool`), `input()`/`print()`, f-strings, basic arithmetic and type conversion.

**Builds on:** Nothing — this is the foundation. Everyone leaves with a working environment.

---

### Week 2 — Making decisions and repeating work

**Concept:** Booleans, comparison and logical operators (`and`/`or`/`not`), `if`/`elif`/`else`, the `while` loop, and the menu-loop pattern (`while True` + a quit condition).

**Builds on:** Week 1's variables and I/O — now the program can branch and repeat instead of running once top-to-bottom.

---

### Week 3 — Collections and iteration

**Concept:** The `for` loop and `range()`, and the **list** as the first real data structure — creating, indexing, slicing, `append`, `len`, iterating, and membership (`in`).

**Builds on:** Week 2's loops. We move from "repeat until a condition" to "do something for each item in a collection" — the dominant pattern in real code.

---

### Week 4 — Functions: organising and reusing code

**Concept:** `def`, parameters, `return`, default arguments, local vs. global scope, docstrings, and the DRY principle (don't repeat yourself). Why a 200-line script of copy-pasted blocks is a problem.

**Builds on:** Everything so far has lived in one flat script. Now we *carve it into named, reusable pieces* — the single biggest leap in code maturity this semester.

---

### Week 5 — Dictionaries and modelling real records

**Concept:** The **dictionary** (key/value), nested data, and the workhorse pattern **list-of-dictionaries** as a stand-in for a table of records. Useful string methods (`.lower()`, `.strip()`, `.split()`, `in`) for searching.

**Builds on:** Week 3 gave us lists; week 4 gave us functions. A list of *single values* can't represent a book with a title *and* author *and* year — the dictionary solves that, and functions keep the operations tidy.

---

### Week 6 — Persistence: files, CSV and JSON

**Concept:** Reading and writing files, the `with` statement, text vs. structured formats. Introduce **CSV** then **JSON**, and why JSON maps perfectly onto our list-of-dictionaries.

**Builds on:** Week 5's data model. Until now, everything vanished when the program closed. This is the week the app becomes *real*: data survives between runs.

---

### Week 7 — Errors, exceptions and robustness

**Concept:** `try`/`except`/`finally`, catching specific exceptions, raising your own, input validation, and defensive programming. Debugging properly: reading tracebacks (revisited), and stepping with a debugger vs. scattering `print()`.

**Builds on:** Weeks 5–6 introduced file reading and user input — both of which *fail* in the real world (missing file, letters where a year should be). This week turns "works on the happy path" into "doesn't crash."

---

### Week 8 — Object-oriented programming I: classes

**Concept:** Classes vs. objects, `__init__`, instance attributes, methods, `self`, and `__str__`/`__repr__` for readable objects. Modelling a *thing* as data **and** behaviour together.

**Builds on:** Week 5's "a book is a dictionary." A dictionary holds data but the logic about it lives elsewhere. A *class* binds the two. Students already understand the data; we're upgrading the container.

---

### Week 9 — Object-oriented programming II: inheritance & polymorphism

**Concept:** Inheritance, `super()`, method overriding, polymorphism, and basic encapsulation with `@property`. Extending a model *without rewriting it*.

**Builds on:** Week 8's single `Book` class. The moment the library needs to hold *films* and *games* too, copy-pasting the class is wrong — inheritance is the answer. Directly motivated by the project's own growth.

---

### Week 10 — Modules, packages, environments & libraries

**Concept:** Splitting code across files with `import`, the `if __name__ == "__main__"` guard, organising a **package**, virtual environments (`venv`), `pip`, `requirements.txt`, and using a **third-party library** by reading its docs.

**Builds on:** Shelf is now several hundred lines of classes in one file — past the point a single script should hold. This week teaches the structure real projects use, and how to safely pull in others' code.

---

### Week 11 — Testing & code quality

**Concept:** Automated testing with **pytest**, the arrange-act-assert pattern, testing edge cases, basic fixtures. Then quality tooling: **PEP 8**, a linter (`ruff`/`flake8`), an auto-formatter (`black`), type hints as documentation, and proper docstrings.

**Builds on:** Week 10 gave a structured package with logic now cleanly separated into testable functions/methods. You can only test code that's well organised — which is exactly what weeks 4, 8, and 10 produced.

---

### Week 12 — Talking to the world: APIs, JSON over HTTP & wrap-up

**Concept:** HTTP basics, REST and JSON, the `requests` library, calling a public API, parsing the JSON response, and handling network failure. Then: finalising a project — the README as the front door.

**Builds on:** The whole course. Students already parse JSON (week 6), model the data as objects (weeks 8–9), and defend against failure (week 7). An API is just JSON arriving over the network instead of from disk — every prerequisite is in place.

---

## Where this leaves the student

By week 12 a student who attended every lab has, hands-on:

- written, structured and **refactored** real Python across procedural and object-oriented styles;
- modelled data with lists, dicts and class hierarchies;
- **persisted** data, **defended** against failure, and **debugged** with real tools;
- organised a multi-module package in a virtual environment with pinned dependencies;
- **tested** their own code and met professional **style** standards;
- consumed a live **API**; and
- used **Git** for the entire semester, finishing with one substantial, documented, end-to-end project.

That is a credible junior-developer baseline.

## Beyond this course (signpost in the final lecture)

Natural next steps that this curriculum deliberately sets up but doesn't cover: **SQLite/SQL** (swap Shelf's JSON store for a database — the cleanest possible follow-on project), a **web framework** (Flask/FastAPI to put a web UI or REST API on Shelf), **Git branching & pull-request workflow** for team development, and **CI** to run the test suite automatically. Point strong students at these as a bridge to year 3.
