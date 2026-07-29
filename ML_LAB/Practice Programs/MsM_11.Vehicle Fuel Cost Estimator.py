distance = float(input("Enter Distance (km): "))
mileage = float(input("Enter Mileage (km/l): "))
fuel_price = float(input("Enter Fuel Price per litre: "))
fuel_needed = distance / mileage
cost = fuel_needed * fuel_price
print("Fuel Needed =", round(fuel_needed, 2), "litres")
print("Total Fuel Cost = ₹", round(cost, 2))
