p = float(input("Principal Amount: "))
r = float(input("Rate of Interest: "))
t = float(input("Time (Years): "))
si = (p * r * t) / 100
ci = p * ((1 + r / 100) ** t) - p
print("Simple Interest =", si)
print("Compound Interest =", ci)
