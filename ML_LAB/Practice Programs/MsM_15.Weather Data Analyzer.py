temps = []
for i in range(1, 8):
    temp = float(input("Enter Temperature Day " + str(i) + ": "))
    temps.append(temp)
print("Maximum Temperature =", max(temps))
print("Minimum Temperature =", min(temps))
print("Average Temperature =", sum(temps) / len(temps))
