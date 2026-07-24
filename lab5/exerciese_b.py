# Exercise B — Word frequency

def main():
    user_input = input("Sentence: ")    # taking user input
    input_list = user_input.strip().lower().split() # clean input into a array

    counts = {} # declear dictionary for word counting

    for word in input_list: # go through every word in input list
        counts[word] = counts.get(word, 0) + 1  # if word not in dictionary create new entry with default of 0

    # sort key-value pair tuple - `counts.items()`, by `value(item[1])` in ascending order, then covert the output back into a dictionary
    counts = dict(sorted(counts.items(), key=lambda item:item[1], reverse=False))

    print(counts)

if __name__ == "__main__":
    main()