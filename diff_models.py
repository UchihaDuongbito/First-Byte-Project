import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor

# Load your dataset (replace 'your_dataset.csv' with the actual file path)
df = pd.read_csv('data/cleaned_all.csv')

# Define the target variable (y)
y = df['Hours at Gym (per week)']  # Replace 'Hours at Gym (per week)' with your actual target column

# Define all possible features
all_features = [
    'Calorie Intake', 'Dietary Preferences', 'Average Spend per Meal Order',
    'Preferred Sports Drink Type', 'Average Weekly Consumption (Bottles)', 
    'Average Spend on Apparel ($/year)', 'Type of Apparel Purchased', 
    'Primary Apparel Purchase Channel'
]

# Models to evaluate
models = {
    'Linear Regression': LinearRegression(),
    'Support Vector Machine': SVR(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor(),
    'XGBoost': XGBRegressor()
}

# Function to evaluate model performance
def evaluate_models(X_train, X_test, y_train, y_test, preprocessor):
    model_results = []
    for name, model in models.items():
        pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])
        pipeline.fit(X_train, y_train)
        predictions = pipeline.predict(X_test)
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        model_results.append((name, mae, r2))
    return model_results

# To store all results across different feature combinations
all_results = []

# Try different combinations of features
for L in range(2, len(all_features) + 1):  # Iterating over different lengths of combinations
    for subset in itertools.combinations(all_features, L):
        print(f"Evaluating combination: {subset}")
        
        # Select the subset of features
        X_selected = df[list(subset)]
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)
        
        # Identify numeric and categorical features
        num_features = [feat for feat in subset if 'Average' in feat or 'Calorie Intake' in feat]
        cat_features = [feat for feat in subset if feat not in num_features]
        
        # Preprocessing pipeline
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), num_features),
                ('cat', OneHotEncoder(), cat_features)
            ])
        
        # Evaluate models on this subset of features
        results = evaluate_models(X_train, X_test, y_train, y_test, preprocessor)
        
        # Store results for each combination of features and models
        for model_name, mae, r2 in results:
            all_results.append({
                'Combination': subset,
                'Model': model_name,
                'MAE': mae,
                'R² Score': r2
            })

# Convert results to a DataFrame for easier sorting and display
results_df = pd.DataFrame(all_results)

# Sort by R² score in descending order
sorted_results = results_df.sort_values(by='R² Score', ascending=False)

# Show the top 3 combinations and their results
print("\nTop 3 combinations by R² score:")
print(sorted_results.head(3))
