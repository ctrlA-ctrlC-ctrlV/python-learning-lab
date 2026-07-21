# Problem 2 — Tip calculator (35 pts)

def main():
    while True:
        try:
            bill = float(input("Bill Amount >> $"))
            if bill <= 0:
                raise ValueError("Invalid input: \"Bill\" cannot be less than or equal to zero")
            
            tip_percent = input("Tip percent (blank = 15) >> ")
            if not tip_percent:
                tip = calculate_tip(bill)
            else:
                tip_percent = float(tip_percent)
                
                if tip_percent and tip_percent < 0:
                    raise ValueError("Invalid input: \"Tip\" cannot be less than zero")
                
                tip = calculate_tip(bill, tip_percent)
                
            if tip:
                print(f"Tip: ${tip}")
                print(f"Total: ${calculate_total(bill, tip)}")
                break

        except ValueError as e:
            error_message = str(e)

            if "could not convert string to float" in error_message:
                print("Invalid input: Input must be a number.")
            else:
                print(error_message)


def calculate_total(bill, tip):
    return bill+tip
    
def calculate_tip(bill, percent=15):
    return bill * percent / 100


if __name__ == "__main__":
    main()