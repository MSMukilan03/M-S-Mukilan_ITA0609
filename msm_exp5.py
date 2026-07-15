amount = float(input("Enter Purchase Amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0
price = amount - discount
gst = price * 0.18
total = price + gst
print("Discount =", discount)
print("GST =", gst)
print("Final Bill =", total)
