import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Dataset: Balls faced vs Runs scored
balls = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]).reshape(-1, 1)
runs = np.array([12, 28, 45, 61, 82, 105, 121, 150, 171, 190])

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(balls, runs)

linear_pred = linear_model.predict(balls)

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
balls_poly = poly.fit_transform(balls)

poly_model = LinearRegression()
poly_model.fit(balls_poly, runs)

poly_pred = poly_model.predict(balls_poly)

# Prediction
test_balls = np.array([[55]])

linear_result = linear_model.predict(test_balls)
poly_result = poly_model.predict(poly.transform(test_balls))

print("Prediction for 55 balls")
print("Linear Regression:", linear_result[0])
print("Polynomial Regression:", poly_result[0])

# Plot
plt.scatter(balls, runs, label="Actual Data")
plt.plot(balls, linear_pred, label="Linear Regression")
plt.plot(balls, poly_pred, label="Polynomial Regression")

plt.xlabel("Balls Faced")
plt.ylabel("Runs")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.show()
