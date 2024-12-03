Electricity Usage Prediction using Random Forest Regression
Project Overview
This project uses machine learning techniques to predict electricity usage based on a publicly available dataset. It involves data preprocessing, model training, evaluation, and hyperparameter tuning. A RandomForestRegressor is employed to achieve optimal performance. The code also includes model persistence using joblib and visualization of results.

Table of Contents
Installation
Usage
Project Structure
Data Preprocessing
Model Training and Evaluation
Visualization
Contributing
License
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/electricity-usage-prediction.git
Navigate to the project directory:
bash
Copy code
cd electricity-usage-prediction
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Load the dataset:

Set the correct path for the dataset in the file_path variable within the script.
Run the script:

bash
Copy code
python main.py
The trained model will be saved as random_forest_model.joblib or best_random_forest_model.joblib.

Project Structure
bash
Copy code
electricity-usage-prediction/
│
├── recs2015_public_v4.csv      # Dataset file (sample format)
├── main.py                     # Main script
├── requirements.txt            # Dependencies
├── random_forest_model.joblib   # Saved model
├── best_random_forest_model.joblib  # Best-tuned model
└── README.md                   # Project documentation
Data Preprocessing
Loading Data:

Data is loaded from a .csv file using Pandas.
Missing Values:

Handled using backward filling (bfill).
Feature Encoding:

Categorical features are encoded using LabelEncoder.
Feature Scaling:

Features are scaled using StandardScaler.
Splitting Data:

Data is split into training and testing sets using an 80/20 ratio.
Model Training and Evaluation
Model:

A RandomForestRegressor is used with 100 estimators and a random state of 42.
Evaluation Metrics:

Mean Squared Error (MSE)
R-squared (R²)
Hyperparameter Tuning:

Uses GridSearchCV to find the best hyperparameters.
Visualization
A scatter plot is generated to compare actual vs predicted electricity usage:

Blue dots: Predictions
Red dashed line: Ideal prediction line

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License.
