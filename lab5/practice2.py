# Part 2 — Missing keys, safely

contact = {
    # key: value    "email": "alice@example.com"
    "name": "Alice",
    "phone": "555-1234",    
}

## 2.1 The crash

# print(contact["age"])   # asking for entry that doesn't exist will raise a KeyError

print("======================================================================")

## 2.2 Ask first with `in`

if "age" in contact:
    print(contact["age"])
else:
    print("No age on file.")

## 2.3 Or use `.get()` with a fallback
#age = contact.get("age")   # samething can be achieved with get() function, 
                            # however if the entry doesn't exist it will crash
                            
age = contact.get("age", "unkown")  # so use "unkown" as a fallback, if the entry 
                                    # doesn't exist it will print "unknow" instead.
                                    # "unknown" can be replaced with anything else
print(f"age >> {age}")