# Problem 1 — Grade classifier

letter_score = ['A', 'B', 'C', 'D', 'F']    # array of letter scores

def main():
    while True: # loop until break
        try:    # catching non-float user entry
            number_score = float(input("Score (0-100) >> "))    # getting user to input number score
            letter = letter_grade(number_score) # convert number score into letter score

            if letter:  # if the letter score is in range "letter" will not be empty
                print(f"Grade: {letter}")
                break   # break out of the while loop

        except ValueError:  # custom error message for non-float user entry
            print("Invalid input: Score must be a float number")

def letter_grade(score):
    try:
        # assigning letter score based on the number score
        if score >= 90 and score <= 100:    # A
            return letter_score[0]
        elif score >= 80 and score < 90:    # B
            return letter_score[1]
        elif score >= 70 and score < 80:    # C
            return letter_score[2]
        elif score >= 60 and score < 70:    # D
            return letter_score[3]
        elif score >= 0 and score < 60:     # F
            return letter_score[4]
        else:                               # out of range othervise
            raise ValueError
    except ValueError:  # custom error message for out of range numbers
        print("Invalid input: Score must be between 0 and 100")

if __name__ == "__main__":
    main()