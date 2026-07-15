amount = float(input("Enter Recharge Amount: "))
if amount >= 500:
    cashback = amount * 0.20
elif amount >= 200:
    cashback = amount * 0.10
else:
    cashback = 0
final = amount - cashback
print("Cashback = ₹", cashback)
print("Final Amount = ₹", final)
