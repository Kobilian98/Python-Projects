'''
A project involving assigning variables to strings and integers.
Updating variables to reflect new totals.
Basic arithmetic.
'''

# Item descriptions.
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
luxurious_lamp_descirption = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# Item prices & sales tax.
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15
sales_tax = .088

# Customer total & purchased item descriptions.
customer_one_total = 0
customer_one_itemization = ""

# Customer one shopping spree.
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_descirption

# Customer one checkout. Sales tax and total and purchased item descriptions.
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
