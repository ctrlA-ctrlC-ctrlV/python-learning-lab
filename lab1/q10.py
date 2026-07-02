# Q10 — one-line catalogue entry (synthesis → bridges to Part C)

title = input("Title >> ")
author = input("Author >> ")
year = input("Year >> ")
price = input("Price >> ")

# print full lable in one line
print(f"\"{title}\" by {author} ({year}) - £{float(price):.2f}")