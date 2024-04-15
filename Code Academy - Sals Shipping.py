weight = 12.5
premium = 125.00
#method = input("Shipping method: ")


#Ground shipping
#if method == "Ground":
if weight <= 2:
  cost = weight * 1.50 + 20.00
elif (weight > 2) and (weight <= 6):
  cost = weight * 3.00 + 20.00
elif (weight > 6) and (weight <= 10):
  cost = weight * 4.00 + 20.00
elif (weight > 10):
  cost = weight * 4.75 + 20.00
else:
  print("Invalid Weight")

print("Ground Shipping:", cost)
print("Premium Ground Shipping:", premium)

#if method == "Premium":
#  cost = 125.00

#if (cost > 125.00):
#  cost = 125.00

#Drone shipping
#if method == "Drone":
if weight <= 2:
  cost = weight * 4.00
elif (weight > 2) and (weight <= 6):
  cost = weight * 9.00
elif (weight > 6) and (weight <= 10):
  cost = weight * 12.00
elif (weight > 10):
  cost = weight * 14.25
else:
  print("Invalid Weight")

print("Drone Shipping:", cost)

#print("Your shipping method is:", method)
#print("Your total is:", cost)