category = input("Seat Category (Silver/Gold): ")
seats = int(input("Number of Seats: "))

if category.lower() == "gold":
    price = 250
else:
    price = 150

total = price * seats

if seats >= 5:
    discount = total * 0.10
else:
    discount = 0

final = total - discount

print("Ticket Cost = ₹", total)
print("Discount = ₹", discount)
print("Final Amount = ₹", final)
