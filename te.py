items = []

while True:
    print("Would you like to")
    print("(1) Add or")
    print("(2) Remove items or")
    print("(3) Quit?", end="")
    choice = int(input(": "))
    if choice == 1:
        item = input("What will be added?: ")
        items.append(item)
    elif choice == 2:
        if len(items) == 0:
            print("There are no items in the list.")            
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

