import pandas as pd
import numpy as np #optional [You can import it if you wish to use it]
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load data
file_path = 'C:\\Users\\vasud\\Downloads\\recs2015_public_v4.csv' #set your own path
try: 
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f'Error: The file at {file_path} was not found')
# Preview data and check for missing values
print(data.info())
print(data.isnull().sum())

# Drop unnecessary columns
columns_to_drop = ['DOEID', 'REGIONC', 'DIVISION']
data.drop(columns=columns_to_drop, inplace=True)

# Handle missing values, if any
data.fillna(method='bfill', inplace=True)

# Encode categorical columns
categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
label_encoder = LabelEncoder()
for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col].astype(str))

# Split data into features and target
target_column = 'ELECTRICITY_USAGE'
features = data.drop(columns=[target_column])
target = data[target_column]

# Scale features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(scaled_features, target, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'random_forest_model.joblib')

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared: {r2}")

# Hyperparameter tuning
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

print(f"Best Parameters: {grid_search.best_params_}")
best_model = grid_search.best_estimator_

# Save the best model
joblib.dump(best_model, 'best_random_forest_model.joblib')

# Evaluate the best model
y_pred_best = best_model.predict(X_test)
mse_best = mean_squared_error(y_test, y_pred_best)
r2_best = r2_score(y_test, y_pred_best)

print(f"Best Model - MSE: {mse_best}")
print(f"Best Model - R-squared: {r2_best}")

# Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual Electricity Usage')
plt.ylabel('Predicted Electricity Usage')
plt.title('Actual vs Predicted Electricity Usage')
plt.show()
