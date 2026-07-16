age = int(input("Enter Age: "))
nationality = input("Enter Nationality: ")

if age >= 18 and nationality.lower() == "indian":
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")
