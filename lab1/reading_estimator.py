print("--- Reading Time Estimator ---")

title = input("What is the title of the book\n")
t_page = int(input("What is the total pages\n(int) "))
page_per_day = float(input("What is the pages you read per day\n(int) "))
minutes_per_page = int(input("how many minutes per page you average\n"))

# how many whole days
whole_days = t_page // page_per_day

# the leftover on the last day
page_left_final_day = t_page % page_per_day

# if there are left over > 0 then it will need an addtional day to finish
if page_left_final_day > 0:
    whole_days + 1

# total reading time
t_reading_time = t_page * minutes_per_page / 60;

# final message
# book name; how many whole days with no decimal; how many page left on the final day; if more than one pages left change "page" to "pages"; how long it takes to read the book (in hours)
print(f"\"Dune\" will take about {whole_days:.0f} days (with {page_left_final_day:.0f} {"pages" if page_left_final_day>1 else "page"} on the last day) - roughly {t_reading_time:.0f} hours of reading")