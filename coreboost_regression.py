import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.pipeline import make_pipeline

# Load the data
data = pd.read_csv('data/all.csv')

# Clean data
cleaned_data = data.dropna(subset=['Hours at Gym (per week)', 'Type of Apparel Purchased', 'Preferred Sports Drink Type', 'Calorie Intake', 'Dietary Preferences', 'Average Spend per Meal Order'])
cleaned_data.to_csv('data/cleaned_all.csv', index=False)

# Display the head of the dataset
#print("Cleaned Data:\n", cleaned_data.head())

# 1. Define Features (X) and Target (y)
# X will include all numeric and categorical variables
X = cleaned_data[['Average Weekly Consumption (Bottles)', 'Average Spend on Apparel ($/year)', 
                  'Preferred Sports Drink Type', 'Type of Apparel Purchased', 
                  'Calorie Intake', 'Dietary Preferences', 'Average Spend per Meal Order', 
                  'Primary Apparel Purchase Channel']]  # Independent variables
y = cleaned_data['Gym Membership Length (years)']  # Dependent variable (target)

# 2. Preprocessing (One-Hot Encoding for categorical variables and Scaling for numeric variables)
preprocessor = ColumnTransformer(
    transformers=[
        # Apply StandardScaler to numerical features
        ('num', StandardScaler(), ['Average Weekly Consumption (Bottles)', 
                                   'Average Spend on Apparel ($/year)', 
                                   'Average Spend per Meal Order', 
                                   'Calorie Intake']),
        # Apply One-Hot Encoder to categorical features
        ('cat', OneHotEncoder(), ['Preferred Sports Drink Type', 
                                  'Type of Apparel Purchased', 
                                  'Dietary Preferences', 
                                  'Primary Apparel Purchase Channel'])
    ])

# 3. Define the Model (Random Forest Regressor)
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# 4. Create a Pipeline that applies preprocessing and then fits the model
pipeline = make_pipeline(preprocessor, rf_model)

# 5. Split Data into Training and Test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train the Model
pipeline.fit(X_train, y_train)

# 7. Make Predictions
y_pred = pipeline.predict(X_test)

# 8. Evaluate the Model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display evaluation metrics
print(f"Mean Absolute Error (MAE): {mae}")
print(f"R-squared (R² Score): {r2}")

# Optional: Display the first few predictions compared to actual values
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison.head())