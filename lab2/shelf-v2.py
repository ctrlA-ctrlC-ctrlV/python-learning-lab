# Weekly challenge: "Shelf v0.2 — a menu that stays open"
title = ""
creator = ""
releas_year = ""
user_rating = -1
rating_percentage = float
time_spent_in_hours = ""
catagory = ""
has_item = False

while 1:
    print("--- Shelf ---")
    
    p = input("[1] Set the item's details\n[2] Show the library card\n[3] Rate it (0-10)\n[Q] Quit\nChose: ")

    if p.strip() == "1":    #[1] Set the item's details
        title = input("Title >> ")
        creator = input("Creator (author/director/studio) >> ")
        releas_year = int(input("Year of release >> "))
        time_spent_in_hours = float(input("Time spent read/watch/play >> "))

        has_item = True

        # coverting time spent in hour to minutes
        time_spent_in_minutes = time_spent_in_hours * 60

        print("========================================")
        print(f"\t{title} ({releas_year})")
        print(f"\tby {creator}")
        print(f"\tLength: {time_spent_in_hours:.1f} hours ({time_spent_in_minutes:.0f} min)")
        print("========================================")

    elif p.strip() == "2":  # [2] Show the library card
        if has_item is True:
            print("========================================")
            print(f"\t{title} ({releas_year})")
            print(f"\tby {creator}")
            
            if user_rating == -1: # if user_rating is default
                print("\tRating: N/A (select [3] to rate the media)")
            else:   #if user_rating is not default
                print(f"\tRating: {user_rating:.1f}/10 ({rating_percentage:.0f}%)")

            print(f"\tLength: {time_spent_in_hours:.1f} hours ({time_spent_in_minutes:.0f} min)")

            if catagory:
                print(f"\tCatagory: {catagory}")
            print("========================================")
        else:
            print("No item yet — choose 1 first")

    elif p.strip() == "3":        
        user_rating = float(input("Your reating of the media (0-10)>> "))

        while(user_rating < 0 or user_rating > 10):
            user_rating = float(input("Please input valid number (0-10) >> "))

        # converting user rating to percentage
        rating_percentage = user_rating/10 * 100

        # catagorise the media
        if user_rating >= 8:
            catagory = "A must read/watch"
        if user_rating >= 5:
            catagory = "Worth your time"
        if user_rating < 5:
            catagory = "Skip it"

    elif p.lower().strip() == "q":
        break

    else:
        print("Not part of the option, please input again.")
