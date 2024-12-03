Electricity Usage Prediction using Random Forest

This project is a machine learning pipeline designed to predict electricity usage using a Random Forest Regressor. It includes data preprocessing, model training, evaluation, hyperparameter tuning, and visualization of predictions.



-- Table of Contents --

- #dataset
- #features
- #technologies-used
- #installation
- #usage
- #model-training-and-evaluation
- #hyperparameter-tuning
- #visualization
- #results
- #contributing
- #license



-- Dataset --

The dataset used is a public dataset (recs2015_public_v4.csv), which contains various features related to electricity consumption. Make sure to set your own file path before running the script.

Key columns:
- ELECTRICITY_USAGE (Target variable)
- Categorical and numerical features related to households.



-- Features --

Data Preprocessing:
- Handles missing values and encodes categorical features using LabelEncoder.
- Scaling: Standardizes the feature set using StandardScaler.

Model Training:
- Implements a Random Forest Regressor for prediction.

Hyperparameter Tuning:
- Uses GridSearchCV for finding optimal hyperparameters.

Evaluation:
- Assesses model performance using metrics like MSE and R-squared.

Visualization:
- Plots actual vs. predicted electricity usage.



-- Technologies Used --

- Python
- Pandas
- NumPy (optional)
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib



-- Installation --

Clone this repository:

bash
git clone (link unavailable)
cd electricity-usage-prediction

Install the required dependencies:

bash
pip install -r requirements.txt

Place your dataset in the appropriate directory and update the file_path variable in the script:

file_path = 'path_to_your_dataset/recs2015_public_v4.csv'



-- Usage --

Run the script to preprocess the data, train the model, and evaluate its performance:

bash
python (link unavailable)



-- Model Training and Evaluation --

Training:
- The Random Forest model is trained using an 80-20 train-test split.

Evaluation Metrics:
- Mean Squared Error (MSE)
- R-squared (R²)

The model is saved using joblib for future predictions.



-- Hyperparameter Tuning --

A grid search is performed to find the best parameters for the Random Forest model. The following hyperparameters are tuned:
- n_estimators: Number of trees in the forest.
- max_depth: Maximum depth of the tree.
- min_samples_split: Minimum number of samples required to split a node.

Run the hyperparameter tuning process using:

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)



-- Visualization --

A scatter plot is generated to compare actual and predicted electricity usage. The red dashed line represents the ideal prediction line (y = x).

plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual Electricity Usage')
plt.ylabel('Predicted Electricity Usage')
plt.title('Actual vs Predicted Electricity Usage')
plt.show()



-- Results --

Best Model Performance:
- Mean Squared Error (MSE): mse_best
- R-squared (R²): r2_best

The model's performance improves after hyperparameter tuning.


-- Contributing --
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: git checkout -b feature-name.
3. Commit your changes: git commit -m 'Add feature'.
4. Push to the branch: git push origin feature-name.
5. Submit a pull request.


-- Members --
1. Aryan Kumar
2. Abhinav Nirwan aka UnknownCodrr
3. Aakash Sharma aka Aakash5268
4. Aman Kumar aka satoru-coder
