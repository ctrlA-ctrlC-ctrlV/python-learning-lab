# Part B — Lab problem: "Reading List Stats"

book_list = []
page_list = []

title = ""
page = -1
total_page = 0
page_highest = 0
chunky_cnt = 0

while True:
    title = input("Please enter book title (or 'done' to quit) >> ")  
    if title.lower() =='done':
        break; 
    else:
        while page < 0:
            page = int(input("Pages in book >> "))
        book_list.append(title)
        page_list.append(page)

        page = -1

# calc total page length
# for i in range(len(page_list)):
#     total_page += page_list[i]
total_page = sum(page_list)

# calc average page length
avg_page_len = total_page/len(page_list)

# find longest book
page_highest = max(page_list)
for i in range(len(page_list)):
    # if page_highest < page_list[i]:
    #     page_highest = page_list[i]

    if page_list[i] >= 400:
        chunky_cnt += 1

print(f"You logged {len(book_list)} books.")
print(f"Total pages: {total_page}")
print(f"Average length: {avg_page_len:.1f} pages")
print(f"Longest book: {page_highest} pages")
print(f"Chunky books (over 400): {chunky_cnt}")