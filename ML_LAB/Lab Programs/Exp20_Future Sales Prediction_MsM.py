import pandas as pd
from sklearn.linear_model import LinearRegression

# Monthly sales dataset
data = {
    "Month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Sales": [120, 135, 150, 160, 175, 190,
              205, 220, 235, 250, 270, 290]
}

df = pd.DataFrame(data)

# Input
X = df[["Month"]]

# Target
y = df["Sales"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict future sales
future_month = pd.DataFrame(
    [[13]],
    columns=["Month"]
)

prediction = model.predict(future_month)

print("Predicted Sales for Month 13:",
      round(prediction[0], 2), "units")
