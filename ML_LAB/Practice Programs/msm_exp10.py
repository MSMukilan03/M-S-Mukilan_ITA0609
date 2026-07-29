fare = 500
age = int(input("Enter Age: "))
ticket = input("Enter Class (Sleeper/AC): ")

if ticket.lower() == "ac":
    fare += 300
if age < 12:
    fare *= 0.5
elif age >= 60:
    fare *= 0.7
print("Total Ticket Fare = ₹", fare)
