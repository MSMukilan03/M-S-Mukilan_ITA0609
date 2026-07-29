pin = 1234
balance = 10000
user_pin = int(input("Enter PIN: "))
if user_pin == pin:
    amount = float(input("Enter Withdrawal Amount: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
        print("Remaining Balance =", balance)
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")
