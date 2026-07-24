# Part 4 — Records: the list of dictionaries

## 4.1 One record, then many
contacts = [
    {"name": "Alice", "phone": "555-1234"},
    {"name": "Bob",   "phone": "555-9999"},
]


for contact in contacts:    # go through each contact to see if a "name"
    if contact["name"] == "Alice":
        print(contact["phone"])

print("======================================================================")

## 4.2 Searching robustly with string methods
txt  = "  Alice Smith  "
print(txt.strip())  # if no string is passed it default to strip all leading/lagging white space
print("------------------")

txt = ",,,,,rrttgg.....Alice Smith....rrr"
print(txt.strip("tr.g,"))   # strip string in the bracket, the string can be any order
print("------------------")

txt  = "  AlIcE SmiTH  "
print(txt.strip().lower())
print("------------------")

txt = "  welcome to the jungle     "
print(txt.strip().lower().split())
print("------------------")

contacts.append({"name": "  Alice Smith  ", "phone": "555-1111"})
for contact in contacts:
    if contact["name"].strip().lower().split()[0] == "alice":
        # howerver `if "alice" in contact["name"].strip().lower().split()` is more efficient
        print(contact["phone"])
