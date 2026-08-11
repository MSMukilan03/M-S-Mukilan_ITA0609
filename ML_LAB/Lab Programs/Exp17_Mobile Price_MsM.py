import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Mobile dataset
data = {
    "RAM": [2, 2, 3, 3, 4, 4, 6, 6, 8, 8,
            3, 4, 6, 8, 12],

    "Storage": [32, 32, 64, 64, 128, 128, 128, 256, 256, 512,
                64, 128, 256, 256, 512],

    "Battery": [3000, 3500, 4000, 4000, 4500,
                5000, 5000, 4500, 5000, 5000,
                4200, 4500, 5000, 5000, 5500],

    "Camera": [12, 13, 16, 20, 24, 32, 48, 48, 64, 108,
               16, 32, 50, 64, 108],

    "Price_Range": [
        "Low", "Low", "Low", "Medium", "Medium",
        "Medium", "High", "High", "High", "Premium",
        "Low", "Medium", "High", "High", "Premium"
    ]
}

df = pd.DataFrame(data)

# Input features
X = df[["RAM", "Storage", "Battery", "Camera"]]

# Target
y = df["Price_Range"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Decision Tree
model = DecisionTreeClassifier(random_state=42)

# Train
model.fit(X_train, y_train)

# Test
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# New mobile
new_mobile = pd.DataFrame(
    [[8, 256, 5000, 64]],
    columns=["RAM", "Storage", "Battery", "Camera"]
)

prediction = model.predict(new_mobile)

print("Predicted Mobile Price Range:", prediction[0])
