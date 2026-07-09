# Q6 — on the shelf? (membership `in`) 

shelf = ["1984", "Stardust", "Blood Reaver"]

title = input("Search for a title? >> ")

if title in shelf:
    print(f"Yes — {title} is on your shelf.")
else:
    print(f"No — {title} is not on your shelf.")