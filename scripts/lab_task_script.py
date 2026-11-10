import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('./dataset/Food_Delivery_Times.csv')

# Handle missing values
df = df.dropna()

# Preprocessing
X = df.drop('Delivery_Time_min', axis=1)
y = df['Delivery_Time_min']

categorical_columns = X.select_dtypes(include=['object']).columns
one_hot_encoded_columns = pd.get_dummies(X[categorical_columns], drop_first=True)
X = pd.concat([X.drop(categorical_columns, axis=1), one_hot_encoded_columns], axis=1)

# Normalization (as done in the notebook)
normalization_columns = X.select_dtypes(include=[np.number]).columns
X[normalization_columns] = (X[normalization_columns] - X[normalization_columns].mean()) / X[normalization_columns].std()

# IV. EDA - Task 1: Correlation Heatmap
# Need to include y for correlation
df_full = pd.concat([X, y], axis=1)
plt.figure(figsize=(12, 10))
sns.heatmap(df_full.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.savefig('outputs/heatmap.png')
print("Heatmap saved as outputs/heatmap.png")

# V. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# VI & VII. Train Models
# 1. Multiple Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

# 2. Decision Tree Regressor
dt_model = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)

# 3. Random Forest (Requested in X)
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# VIII & X. Model Evaluation
def evaluate_model(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return mae, rmse, r2

metrics = {}
metrics['Linear Regression'] = evaluate_model(y_test, lr_pred)
metrics['Decision Tree'] = evaluate_model(y_test, dt_pred)
metrics['Random Forest'] = evaluate_model(y_test, rf_pred)

print("\nModel Comparison Table:")
print("| Model | MAE | RMSE | R² |")
print("|---------|---------|---------|---------|")
for model_name, (mae, rmse, r2) in metrics.items():
    print(f"| {model_name} | {mae:.2f} | {rmse:.2f} | {r2:.2f} |")
