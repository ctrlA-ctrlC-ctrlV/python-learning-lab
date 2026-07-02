# Q4 — split the bill (`//` and `%`)

# Ask meal price in pence
meal_price = float(input("What is the meal price?\n(*in pence)"));

# Ask tip percentage
num_of_ppl = float(input("How many people attend the meal?\n"));

# Calculate and display
pence_per_percen = meal_price // num_of_ppl;
left_over = meal_price % num_of_ppl;
print(f"Each pays {pence_per_percen:.0f}p, with {left_over}p left over");