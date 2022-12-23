# Get the total number of elements
n = int(input("Please Enter the Total Number of Elements : "))

# Initialize an empty list
lst = []

# Read the elements from the user and add them to the list
for i in range(n):
    ele = int(input(f"Please enter the {i} Element : "))
    lst.append(ele)

# Sort the list in ascending order
lst = sorted(lst)

# Print the sorted list
print("The Sorted List in Ascending Order : ", lst)
