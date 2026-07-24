# Problem 1 — Tally counter

def get_input():
    return str(input("Enter words separated by spaces: "))

def tally(items):
    counts = {}
    for item in items.strip().lower().split():  # part of requirement that it's not case sensetive 
        counts[item] = counts.get(item, 0) + 1
    return counts

def main():
    while True: # loop until the process finish
        input = get_input() # get user input

        if input:   
            # if input exist, tally how many time each word (seperated by space) appears
            input_tally = tally(input)

        if input_tally:
            for entry in input_tally:
                print(entry)
            break   # break out of the loop, end process

if __name__ == "__main__":
    main()