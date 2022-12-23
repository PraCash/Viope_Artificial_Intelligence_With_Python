#In the second exercise the idea is to create a small grocery shopping list with the list datastructure. In short, create a program that allows the user to (1) add products to the list, (2) remove items and (3) print the list and quit. 

#If the user adds something to the list, the program asks "What will be added?: " and saves it as the last item in the list. If the user decides to remove something, the program informs the user about how many items there are on the list (There are [number] items in the list.") and prompts the user for the removed item ("Which item is deleted?: "). If the user selects 0, the first item is removed. When the user quits, the final list is printed for the user "The following items remain in the list:" followed by the remaining items one per line. If the user selects anything outside the options, including when deleting items, the program responds "Incorrect selection.". When the program works correctly it prints out the following:

items = []

while True:
    print("Would you like to (1)Add or (2)Remove items or (3)Quit?: ", end="")
    choice = input()

    if choice == "1":
        print("What will be added?: ", end="")
        item = input()
        items.append(item)
    elif choice == "2":
        if not items:
            print("The list is empty.")
        else:
            print("There are {} items in the list.".format(len(items)))
            print("Which item is deleted?: ", end="")
            index = input()
            try:
                index = int(index)
                if index < 0 or index >= len(items):
                    print("Incorrect selection.")
                else:
                    del items[index]
            except ValueError:
                print("Incorrect selection.")
    elif choice == "3":
        break
    else:
        print("Incorrect selection.")

print("The following items remain in the list:")
for item in items:
    print(item)


