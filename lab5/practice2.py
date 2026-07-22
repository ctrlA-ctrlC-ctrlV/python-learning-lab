# 1.2 Add, update, remove

# Step one
contact = {
    # key: value    "email": "alice@example.com"
    "name": "Alice",
    "phone": "555-1234",    
}
print(contact)

contact["email"] = "alice@example.com"  # add through assignment
contact["phone"] = "555-9999"           # this can also edit the value
print(contact)

# or through updated function
contact.update({"age": "25"})           # it can create new entry
contact.update({"phone": "555-1111"})   #or updated existing
print(contact)

print("======================================================================")

# Step two
del contact["email"]    # remove dictionary entry by using keyword "del" and pointing at the key
print(contact)

contact.pop("age")      # or use dictionary's build in function "pop" to acheive the samething
print(contact)

# print(contact)
# print(contact["name"])
# print(contact["phone"])