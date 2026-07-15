food = float(input("Food Bill: "))
gst = food * 0.05
service = food * 0.10
total = food + gst + service
print("GST =", gst)
print("Service Charge =", service)
print("Total Bill =", total)
