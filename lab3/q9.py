# Q9 — reading total (accumulate over a list)

pages = [320, 180, 540]

total = 0

for i in range(len(pages)):
    total += pages[i]

print(f"Total: {total} pages")
print(f"Average: {total/len(pages):.1f} pages")