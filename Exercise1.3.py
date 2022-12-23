
'''Make function bubble_sort using bubble sort algorithm to sort numbers given by user; order numbers into the ascending order.
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. '''


def bubble_sort(numbers):
  # Set a flag to indicate whether any swaps were made
  swapped = True

  # Continue looping until no swaps are made
  while swapped:
    # Set the flag to False to begin the loop
    swapped = False

    # Iterate through the list of numbers
    for i in range(len(numbers) - 1):
      # If the current number is greater than the next number, swap them
      if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        # Set the flag to True to indicate that a swap was made
        swapped = True

  # Return the sorted list of numbers
  return numbers

  a = []
  number = int(input("Please Enter the Total Number of Elements : "))
  for i in range(number):
    value = int(input("Please enter the % d Element : " % i))
    a.append(value)
  print("The Sorted List in Ascending Order : ", bubble_sort(a))
