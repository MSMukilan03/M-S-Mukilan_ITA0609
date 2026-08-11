import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Credit Score Dataset
data = {
    "Income": [20, 25, 30, 35, 40, 45, 50, 55, 60, 70,
               22, 28, 38, 48, 58],

    "Loan": [18, 20, 25, 22, 30, 28, 35, 30, 25, 20,
             19, 24, 27, 30, 22],

    "Repayment": [2, 3, 4, 5, 5, 6, 7, 8, 9, 10,
                  2, 4, 5, 7, 9],

    "Utilization": [90, 85, 80, 75, 70, 65, 60, 55, 45, 30,
                    88, 78, 72, 58, 40],

    "Score": [
        "Poor", "Poor", "Poor", "Average", "Average",
        "Average", "Good", "Good", "Good", "Good",
        "Poor", "Poor", "Average", "Good", "Good"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Input features
X = df[["Income", "Loan", "Repayment", "Utilization"]]

# Target
y = df["Score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Test prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Actual:", list(y_test))
print("Predicted:", list(y_pred))
print("Accuracy:", accuracy)

# New customer
new_customer = pd.DataFrame(
    [[45, 25, 7, 55]],
    columns=["Income", "Loan", "Repayment", "Utilization"]
)

# Predict credit score
prediction = model.predict(new_customer)

print("New Customer Credit Score:", prediction[0])
