print("--- Reading Time Estimator ---")

title = input("Title >> ")
creator = input("Creator (author/director/studio) >> ")
releas_year = int(input("Year of release >> "))
user_rating = float(input("Your reating of the media >> "))
time_spent_in_hours = float(input("Time spent read/watch/play >> "))

# converting user rating to percentage
rating_percentage = user_rating/10 * 100

# coverting time spent in hour to minutes
time_spent_in_minutes = time_spent_in_hours * 60

print("========================================")
print(f"\t{title} ({releas_year})")
print(f"\tby {creator}")
print(f"\tRating: {user_rating:.1f}/10 ({rating_percentage:.0f}%)")
print(f"\tLength: {time_spent_in_hours:.1f} hours ({time_spent_in_minutes:.0f} min)")
print("========================================")