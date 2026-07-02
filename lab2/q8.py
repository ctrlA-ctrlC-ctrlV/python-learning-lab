# Q8 — what time is it? (elif chain on a range) 

hour = int(input("Hour (int, 0-23)? >> "))

if hour >= 5 and hour <= 11:
    msg = "morning"
elif hour >= 12 and hour <= 16:
    msg = "afternoon"
elif hour >= 17 and hour <= 20:
    msg = "evening"
elif hour >= 0 and hour <= 4:
    msg = "night"
elif hour >= 21 and hour <= 23:
    msg = "night"
else:
    msg = "ERROR"

if msg != "ERROR":
    print(f"Good {msg}!")
else:
    print("ERROR: OUT OF RANGE")