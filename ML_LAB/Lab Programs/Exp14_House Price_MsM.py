import pandas as pd
from sklearn.linear_model import LinearRegression

# House dataset
data = {
    "Area": [800, 1000, 1200, 1400, 1600,
             1800, 2000, 2200, 2400, 2600],

    "Bedrooms": [1, 2, 2, 3, 3,
                 3, 4, 4, 4, 5],

    "Age": [15, 12, 10, 8, 7,
            6, 5, 4, 3, 2],

    "Price": [25, 32, 38, 45, 52,
              58, 65, 72, 80, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Input features
X = df[["Area", "Bedrooms", "Age"]]

# Target variable
y = df["Price"]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# New house details
new_house = pd.DataFrame(
    [[1500, 3, 5]],
    columns=["Area", "Bedrooms", "Age"]
)

# Predict house price
prediction = model.predict(new_house)

print("Predicted House Price:",
      round(prediction[0], 2), "Lakhs")
