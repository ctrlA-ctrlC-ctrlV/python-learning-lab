# Q3 — tip calculator (float, arithmetic, `:.2f`)

# Ask meal price
print("What is the meal price?");
meal_price = float(input());

# Ask tip percentage
print("What is the tip percentage (%)?");
tip_percentage = float(input());

# Calculate and display
tip = meal_price * tip_percentage * .01;
print(f"Leave a tip of ${tip:.2f}");