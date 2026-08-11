import pandas as pd
from sklearn.linear_model import LinearRegression

# Car dataset
data = {
    "Age": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Mileage": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "Engine": [1500, 1600, 1400, 1800, 1500,
               1300, 1200, 1400, 1100, 1000],
    "Horsepower": [120, 125, 110, 150, 120,
                   100, 90, 105, 80, 75],
    "Price": [18, 17, 15, 14, 12, 10, 8, 7, 5, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Input features
X = df[["Age", "Mileage", "Engine", "Horsepower"]]

# Target variable
y = df["Price"]

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(X, y)

# New car details
new_car = pd.DataFrame(
    [[3, 25, 1600, 125]],
    columns=["Age", "Mileage", "Engine", "Horsepower"]
)

# Predict price
prediction = model.predict(new_car)

print("Predicted Car Price:", round(prediction[0], 2), "Lakhs")
