# Part 3 — Iterating & the tally pattern

## 3.1 Three ways to loop

prices = {
    "apple": 5, 
    "bread": 3
}

for key in prices:
    print(key)

print("------------------")

for value in prices.values():
    print(value)

print("------------------")

for key, value in prices.items():
    print(f"{key} costs ${value}")

print("======================================================================")

## 3.2 The tally pattern — build it yourself

words = ["cherry", "apple", "banana", "apple", "banana", "apple"]

counts = {}

### using if statement for first count
# for word in words:
#     if word in counts:
#         counts[word] = counts[word] + 1
#     else:
#         counts[word] = 1

# using fallback for first count
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
print(list(counts.items()))

print("======================================================================")
## 3.3 Dictionary sort

### Sort with bubble sort algorithm 
# items = list(counts.items())
# n = len(items)

# for i in range(n):
#     swapped = False
#     for j in range(0, n-i-1):
#         if items[j][1]<items[j+1][1]:
#             items[j], items[j+1] = items[j+1], items[j]
#             swapped = True
    
#     if not swapped:
#         break

# counts = dict(items)
# print(list(counts.items()))

### sort with "sorted()" function
counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
print(list(counts.items()))