# Q8 — build a list (.append() in a loop)

titles = []

t = ""

while True:
    t = input("Add a title (or 'q','done') >> ")  
    if t.lower() == 'q' or t.lower() =='done':
        break; 
    titles.append(t)

print(f"You added {len(titles)} books: {titles}")