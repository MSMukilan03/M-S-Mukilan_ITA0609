# ============================================================
# URBAN WATER QUALITY ASSESSMENT USING DECISION TREE
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ------------------------------------------------------------
# A. DATASET PREPARATION
# ------------------------------------------------------------

# Create a sample water-quality dataset
data = {
    "pH": [7.2, 6.5, 8.1, 7.0, 5.8, 8.5, 7.4, 6.2, 7.8, 5.5,
           7.1, 8.2, 6.8, 7.6, 5.9, 8.0, 7.3, 6.4, 7.9, 5.7],

    "Turbidity": [2.1, 4.5, 1.2, 3.0, 8.5, 1.0, 2.5, 6.8, 1.8, 9.0,
                  2.2, 1.4, 5.0, 2.0, 7.5, 1.6, 2.8, 5.8, 1.5, 8.0],

    "Dissolved_Oxygen": [7.5, 6.2, 8.0, 7.0, 3.5, 8.2, 7.3, 4.5, 7.8, 3.0,
                         7.0, 8.1, 5.5, 7.4, 4.0, 8.0, 7.2, 5.0, 7.7, 3.8],

    "TDS": [250, 400, 180, 300, 700, 150, 280, 600, 220, 800,
            270, 190, 450, 260, 650, 200, 290, 500, 210, 750],

    "Temperature": [25, 27, 24, 26, 31, 23, 25, 30, 24, 32,
                    26, 24, 28, 25, 30, 23, 26, 29, 24, 31],

    "Quality": [
        "Good", "Good", "Good", "Good", "Poor",
        "Good", "Good", "Poor", "Good", "Poor",
        "Good", "Good", "Poor", "Good", "Poor",
        "Good", "Good", "Poor", "Good", "Poor"
    ]
}

df = pd.DataFrame(data)

print("========== DATASET ==========")
print(df)

# ------------------------------------------------------------
# Pandas DATA INSPECTION
# ------------------------------------------------------------

print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DATA DESCRIPTION ==========")
print(df.describe())

print("\n========== SORTED DATA ==========")
print(df.sort_values("pH"))

print("\n========== GROUPING ==========")
print(df.groupby("Quality")["pH"].mean())


# ------------------------------------------------------------
# B. CONCEPT REPRESENTATION
# ------------------------------------------------------------

print("\n========== CONCEPT REPRESENTATION ==========")

print("Attributes:")
print("1. pH")
print("2. Turbidity")
print("3. Dissolved Oxygen")
print("4. TDS")
print("5. Temperature")

print("\nTarget Concept: Water Quality")
print("Classes: Good and Poor")

print("\nHypothesis Space:")
print("Possible Decision Tree rules formed using water-quality attributes.")

print("\nInductive Bias:")
print("The model prefers useful attribute splits that produce pure and")
print("interpretable classification branches.")


# ------------------------------------------------------------
# C. HEURISTIC ATTRIBUTE SELECTION
# ------------------------------------------------------------

X = df.drop("Quality", axis=1)
y = df["Quality"]

# Train a temporary tree to determine feature importance
temp_tree = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

temp_tree.fit(X, y)

importance = pd.DataFrame({
    "Attribute": X.columns,
    "Importance": temp_tree.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n========== ATTRIBUTE IMPORTANCE ==========")
print(importance)


# ------------------------------------------------------------
# D. TRAINING AND TESTING
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

print("\n========== DATA SPLIT ==========")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# ------------------------------------------------------------
# DECISION TREE MODEL
# ------------------------------------------------------------

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)

print("\nDecision Tree Model Trained Successfully!")


# ------------------------------------------------------------
# E. CLASSIFICATION
# ------------------------------------------------------------

y_pred = model.predict(X_test)

print("\n========== PREDICTIONS ==========")

result = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print(result)


# ------------------------------------------------------------
# F. PERFORMANCE EVALUATION
# ------------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

print("\n========== PERFORMANCE ==========")

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)

print("\n========== CLASSIFICATION REPORT ==========")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))


# ------------------------------------------------------------
# CONFUSION MATRIX
# ------------------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\n========== CONFUSION MATRIX ==========")
print(cm)


# ------------------------------------------------------------
# G. DECISION TREE VISUALIZATION
# ------------------------------------------------------------

plt.figure(figsize=(18, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True,
    rounded=True
)

plt.title("Decision Tree for Urban Water Quality Classification")

plt.show()


# ------------------------------------------------------------
# DECISION RULES
# ------------------------------------------------------------

from sklearn.tree import export_text

rules = export_text(
    model,
    feature_names=list(X.columns)
)

print("\n========== DECISION RULES ==========")
print(rules)


# ------------------------------------------------------------
# NEW / UNSEEN WATER SAMPLE
# ------------------------------------------------------------

new_sample = pd.DataFrame({
    "pH": [7.0],
    "Turbidity": [2.5],
    "Dissolved_Oxygen": [7.0],
    "TDS": [300],
    "Temperature": [26]
})

prediction = model.predict(new_sample)

print("\n========== NEW WATER SAMPLE ==========")
print(new_sample)

print("\nPredicted Water Quality:", prediction[0])


# ------------------------------------------------------------
# TREE COMPLEXITY
# ------------------------------------------------------------

print("\n========== TREE COMPLEXITY ==========")

print("Number of Nodes :", model.tree_.node_count)
print("Tree Depth      :", model.tree_.max_depth)

print("\nProject completed successfully!")
