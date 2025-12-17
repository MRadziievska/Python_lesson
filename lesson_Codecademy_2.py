weight = 8.4
print(weight)

# Ground Shipping
if 0 < weight <= 2:
  cost = 1.50 * weight + 20
  print("Ground Shipping = ", cost, '$')

elif 2 < weight <= 6:
  cost = 3.00* weight + 20
  print("Ground Shipping = ", cost, '$')

elif 6 < weight <= 10:
  cost = 4.00 * weight + 20
  print("Ground Shipping = ", cost, '$')

elif weight > 10:
  cost = 4.75 * weight + 20
  print("Ground Shipping = ", cost, '$')
else:
  print('Weight not selected')

#Ground Shipping Premium
cost = weight + 125.00
print("Ground Shipping Premium = ", cost, '$')

# Drone Shipping
if 0 < weight <= 2:
  cost = 4.50 * weight
  print("Drone Shipping = ", cost, '$')

elif 2 < weight <= 6:
  cost = 9.00 * weight
  print("Drone Shipping = ", cost, '$')

elif 6 < weight <= 10:
  cost = 12.00 * weight
  print("Drone Shipping = ", cost, '$')

elif weight > 10:
  cost = 14.25 * weight
  print("Drone Shipping = ", cost, '$')
else:
  print('Weight not selected')


