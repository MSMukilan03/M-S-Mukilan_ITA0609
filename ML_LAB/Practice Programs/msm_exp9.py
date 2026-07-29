days = int(input("Enter Overdue Days: "))
if days <= 5:
    fine = days * 2
elif days <= 10:
    fine = days * 5
else:
    fine = days * 10
print("Library Fine = ₹", fine)
