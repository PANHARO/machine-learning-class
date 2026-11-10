import numpy as np

class MyKNNModel:

    def __init__(self, k=3, distance_type="euclidean", weight_type="uniform", p=2):
        self.k = k
        self.distance_type = distance_type
        self.weight_type = weight_type
        self.p = p   # parameter for Minkowski distance

    # Training function
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    # Distance Functions
    def calculate_distance(self, x1, x2):
        if self.distance_type == "euclidean":
            return np.sqrt(np.sum((x1 - x2)**2))
        
        elif self.distance_type == "manhattan":
            return np.sum(np.abs(x1 - x2))
        
        elif self.distance_type == "chebyshev":
            return np.max(np.abs(x1 - x2))
        
        elif self.distance_type == "minkowski":
            return np.sum(np.abs(x1 - x2)**self.p)**(1/self.p)
        
        else:
            raise ValueError("Unsupported distance type")

    # Weight Functions
    def compute_weights(self, distances):
        epsilon = 1e-8

        if self.weight_type == "uniform":
            weights = np.ones(len(distances))

        elif self.weight_type == "inverse":
            weights = 1 / (distances + epsilon)

        elif self.weight_type == "inverse_square":
            weights = 1 / (distances**2 + epsilon)

        elif self.weight_type == "linear":
            d_max = np.max(distances)
            d_min = np.min(distances)
            weights = (d_max - distances) / (d_max - d_min + epsilon)

        elif self.weight_type == "exp":
            weights = np.exp(-distances)
            
        else:
            raise ValueError("Unsupported weight type")
        return weights

    # Prediction for one test point
    def predict_one(self, test_point):
        distances = np.zeros(len(self.X_train))
        for i in range(len(self.X_train)):
            distances[i] = self.calculate_distance(self.X_train[i], test_point)

        k_indices = np.argsort(distances)[:self.k]
        k_distances = distances[k_indices]
        k_labels = self.y_train[k_indices]

        weights = self.compute_weights(k_distances)

        unique_labels = np.unique(k_labels)
        weighted_votes = {}
        for label in unique_labels:
            weighted_votes[label] = np.sum(weights[k_labels == label])

        predicted_label = max(weighted_votes, key=weighted_votes.get)
        return predicted_label

    # Prediction for multiple test points
    def predict(self, X_test):
        y_pred = []
        for x in X_test:
            y_pred.append(self.predict_one(x))
            
        y_pred = np.array(y_pred) #
        return y_pred