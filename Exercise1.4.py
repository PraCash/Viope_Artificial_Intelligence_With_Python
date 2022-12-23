'''Make simple Supermarket -program,

having 10 products with prices in a list as follows:[10,14,22,33,44,13,22,55,66,77].
asking product number from 1 to 10 and summing its price to totalsum and printing product number and price for every product as in example.
asking products until user gives '0' to quit the program (while-loop).
printing  "Total:" and the total sum of prices.
asking "Payment:" from user and printing "Change:" and finally  calculating and printing the amount of change (payment - totalsum) to customer.
You must use in this program: while, input'''


print("Supermarket")
print("===========")
prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]

total_sum = 0

product_num = 1
while product_num != 0:
  product_num = int(input("Please select product (1-10) 0 to quit: "))
  if product_num > 0 and product_num <= 10:
    price = prices[product_num-1]
    total_sum += price
    print("Product:", product_num, "Price:", price)

print("Total:", total_sum)

payment = float(input("Payment: "))
change = int(payment - total_sum)
print("Change:", change)
