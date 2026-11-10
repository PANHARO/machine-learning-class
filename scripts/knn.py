import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# Assuming X_train and y_train are already defined
error_rate = []

# Test k values from 1 to 30
for i in range(1, 31):
    knn = KNeighborsClassifier(n_neighbors=i)
    # Using 10-fold cross-validation to get an accurate error rate
    score = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    error_rate.append(1 - score.mean())

# Plotting the Elbow Method Graph
plt.figure(figsize=(10, 6))
plt.plot(range(1, 31), error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markeredgecolor='black', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()