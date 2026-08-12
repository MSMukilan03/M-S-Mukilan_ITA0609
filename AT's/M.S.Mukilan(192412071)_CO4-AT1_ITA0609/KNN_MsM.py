import math
from collections import Counter

data = [
    [450, 135, 45, "Good"],
    [380, 128, 38, "Good"],
    [520, 142, 52, "Good"],
    [300, 120, 30, "Poor"],
    [250, 110, 25, "Poor"],
    [280, 115, 28, "Poor"],
    [470, 138, 47, "Good"],
    [220, 105, 22, "Poor"],
    [410, 130, 41, "Good"],
    [270, 112, 27, "Poor"]
]

train_data = data[:8]
test_data = data[8:]

def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def knn_predict(training_data, test_point, k):
    distances = []

    for row in training_data:
        features = row[:3]
        label = row[3]
        distance = euclidean_distance(features, test_point)
        distances.append((distance, label))

    distances.sort(key=lambda x: x[0])
    nearest_neighbors = distances[:k]

    labels = [label for distance, label in nearest_neighbors]
    prediction = Counter(labels).most_common(1)[0][0]

    return prediction

print("K-NEAREST NEIGHBOUR - CRICKET CLASSIFICATION")

k = int(input("Enter the value of K: "))

if k <= 0 or k > len(train_data):
    print("Invalid value of K")
    exit()

correct = 0

for row in test_data:
    test_features = row[:3]
    actual_label = row[3]

    predicted_label = knn_predict(
        train_data,
        test_features,
        k
    )

    print("\nRuns:", test_features[0])
    print("Strike Rate:", test_features[1])
    print("Average:", test_features[2])
    print("Actual Class:", actual_label)
    print("Predicted Class:", predicted_label)

    if predicted_label == actual_label:
        correct += 1

accuracy = (correct / len(test_data)) * 100

print("\nCorrect Predictions:", correct)
print("Total Test Samples:", len(test_data))
print("Accuracy:", round(accuracy, 2), "%")
