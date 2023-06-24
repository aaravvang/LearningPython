'''Aarav goes to Ikea store and purchase 5 chairs at $15 each and 4 tables at $20 each. He got a discount of 25% on the total amount. Write a Python code to calculate and print the final amount'''
chair = 15
table = 20
chair_cost = chair * 5 #(total cost of chairs is $75)
table_cost = table * 4 #(total cost of tables is $80)
total_cost = chair_cost+ table_cost #(total cost of the chairs and table)
print("Total cost before discount is:$", total_cost)
discount = total_cost * 0.25
print("Your discount is:$", discount)
new_price = total_cost - discount #(price after discount)
print("Aarav, your price for 5 chairs and 4 tables after a 25% discount is:$", new_price)