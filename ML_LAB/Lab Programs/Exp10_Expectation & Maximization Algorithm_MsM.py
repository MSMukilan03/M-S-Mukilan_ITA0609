import numpy as np
from sklearn.mixture import GaussianMixture

# Cricket scores
scores = np.array([
    12, 18, 20, 25, 30,
    65, 70, 75, 82, 90
]).reshape(-1, 1)

# EM algorithm using Gaussian Mixture Model
em = GaussianMixture(n_components=2, random_state=42)

# Fit model
em.fit(scores)

# Predict groups
groups = em.predict(scores)

print("Score\tGroup")

for score, group in zip(scores.flatten(), groups):
    print(score, "\t", group)

print("\nEstimated Means:")
print(em.means_.flatten())
