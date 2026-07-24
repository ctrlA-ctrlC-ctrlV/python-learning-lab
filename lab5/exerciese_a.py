# Exercise A — Inventory lookup

def main():
    inventory = {"apples": 12, "bread": 3}

    print("=============================")
    print("----- Inventory Lookup ------")
    print("=============================")

    while True:
        search_item = str(input("Please input the item you want to lookup >> "))
        try:
            print(f"{search_item}: {inventory[search_item]} in stock")
        except KeyError:
            print(f"{search_item}: 0 in stock")
        finally:
            print("-----------------------------")

if __name__ == "__main__":
    main()