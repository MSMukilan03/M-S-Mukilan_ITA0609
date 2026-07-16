stock = int(input("Enter Available Stock: "))
minimum = int(input("Enter Minimum Stock Level: "))

if stock < minimum:
    print("Low Stock! Reorder Required.")
else:
    print("Stock Level is Sufficient.")
