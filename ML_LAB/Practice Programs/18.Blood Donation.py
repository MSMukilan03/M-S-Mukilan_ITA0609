age = int(input("Enter Age: "))
weight = float(input("Enter Weight (kg): "))
hb = float(input("Enter Hemoglobin Level: "))

if age >= 18 and weight >= 50 and hb >= 12.5:
    print("Eligible to Donate Blood")
else:
    print("Not Eligible")
