print("Parking Fee Calculator")
vehicle = input("Enter Vehicle Type (Bike/Car): ")
hours = int(input("Enter Parking Hours: "))
if vehicle.lower() == "bike":
    fee = hours * 20
else:
    fee = hours * 50
print("Parking Fee = ₹", fee)
