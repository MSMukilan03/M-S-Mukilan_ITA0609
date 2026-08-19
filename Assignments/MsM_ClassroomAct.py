import numpy as np
import matplotlib.pyplot as plt

# Dataset
players = np.array(["Virat", "Dhoni", "Gayle", "AB", "Raina"])

runs = np.array([12000, 10773, 10480, 9577, 5615])
innings = np.array([250, 350, 301, 228, 205])
fifties = np.array([65, 73, 54, 53, 36])
hundreds = np.array([50, 10, 22, 25, 1])

# Mathematical operations
print("Total Runs =", np.sum(runs))
print("Average Runs =", np.mean(runs))
print("Maximum Runs =", np.max(runs))
print("Minimum Runs =", np.min(runs))
print("Median Runs =", np.median(runs))
print("Standard Deviation =", np.std(runs))

# Runs per innings
average = runs / innings

print("\nRuns Per Innings:")
for i in range(5):
    print(players[i], "=", round(average[i], 2))

# Highest run scorer
x = np.argmax(runs)
print("\nHighest Run Scorer =", players[x])
print("Runs =", runs[x])

# Bar Graph
plt.bar(players, runs)
plt.title("Runs of Players")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.show()

# Line Graph
plt.plot(players, runs, marker='o')
plt.title("Player Runs")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.grid()
plt.show()

# Scatter Plot
plt.scatter(innings, runs)
plt.title("Innings vs Runs")
plt.xlabel("Innings")
plt.ylabel("Runs")
plt.show()

# Pie Chart
plt.pie(runs, labels=players, autopct='%1.1f%%')
plt.title("Run Contribution")
plt.show()

# 50s and 100s Bar Graph
x = np.arange(5)

plt.bar(x - 0.2, fifties, width=0.4, label="50s")
plt.bar(x + 0.2, hundreds, width=0.4, label="100s")

plt.xticks(x, players)
plt.xlabel("Players")
plt.ylabel("Number")
plt.title("50s and 100s")
plt.legend()
plt.show()

# Histogram
plt.hist(runs)
plt.title("Distribution of Runs")
plt.xlabel("Runs")
plt.ylabel("Players")
plt.show()
